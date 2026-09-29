"""
Security and health checking for Python packages.
Integrates with PyPI Safety database and package metadata.
"""

import json
import urllib.request
import urllib.parse
import subprocess
import sys
from typing import Dict, List, Optional, Tuple


class SecurityChecker:
    """Check packages for known security vulnerabilities."""
    
    SAFETY_DB_URL = "https://raw.githubusercontent.com/pyupio/safety-db/master/data/insecure_full.json"
    
    def __init__(self):
        self._vulnerability_db: Optional[Dict] = None
        self._load_vulnerability_db()
    
    def _load_vulnerability_db(self):
        """Load the vulnerability database from Safety DB."""
        try:
            with urllib.request.urlopen(self.SAFETY_DB_URL, timeout=10) as resp:
                self._vulnerability_db = json.loads(resp.read().decode('utf-8'))
        except Exception:
            self._vulnerability_db = None
    
    def check_package(self, package_name: str, version: str) -> List[Dict]:
        """
        Check if a package version has known vulnerabilities.
        
        Returns:
            List of vulnerability dictionaries with 'id', 'advisory', 'specs', 'v' fields
        """
        if not self._vulnerability_db:
            return []
        
        package_lower = package_name.lower().strip()
        vulnerabilities = []
        
        # Safety DB structure: package name -> list of vulnerabilities
        pkg_vulns = self._vulnerability_db.get(package_lower, [])
        
        for vuln in pkg_vulns:
            # Check if the current version matches any vulnerable specs
            try:
                specs = vuln.get('specs', [])
                if self._version_matches_specs(version, specs):
                    vulnerabilities.append({
                        'id': vuln.get('id', 'Unknown'),
                        'advisory': vuln.get('advisory', 'No details available'),
                        'specs': specs,
                        'cve': vuln.get('cve'),
                    })
            except Exception:
                continue
        
        return vulnerabilities
    
    def _version_matches_specs(self, version: str, specs: List[str]) -> bool:
        """Check if a version matches any of the vulnerable version specifications."""
        try:
            from packaging.specifiers import SpecifierSet
            from packaging.version import Version
            
            for spec in specs:
                if SpecifierSet(spec).contains(Version(version)):
                    return True
            return False
        except Exception:
            # Fallback: simple string matching
            for spec in specs:
                if version in spec or f"=={version}" in spec:
                    return True
            return False
    
    def get_package_info(self, package_name: str) -> Optional[Dict]:
        """Get package metadata from PyPI."""
        try:
            url = f"https://pypi.org/pypi/{urllib.parse.quote(package_name)}/json"
            with urllib.request.urlopen(url, timeout=8) as resp:
                return json.loads(resp.read().decode('utf-8'))
        except Exception:
            return None
    
    def check_package_health(self, package_name: str, version: str) -> Dict:
        """
        Comprehensive health check for a package.
        
        Returns:
            Dict with 'security', 'metadata', 'score' fields
        """
        result = {
            'package': package_name,
            'version': version,
            'vulnerabilities': [],
            'metadata': {},
            'health_score': 100,
            'warnings': [],
        }
        
        # Check for vulnerabilities
        vulns = self.check_package(package_name, version)
        result['vulnerabilities'] = vulns
        if vulns:
            result['health_score'] -= len(vulns) * 20
            result['warnings'].append(f"{len(vulns)} known vulnerability/vulnerabilities found")
        
        # Get package metadata
        info = self.get_package_info(package_name)
        if info:
            package_info = info.get('info', {})
            result['metadata'] = {
                'summary': package_info.get('summary', ''),
                'author': package_info.get('author', ''),
                'license': package_info.get('license', 'Unknown'),
                'home_page': package_info.get('home_page', ''),
                'project_urls': package_info.get('project_urls', {}),
            }
            
            # Check license
            license_text = package_info.get('license', '').lower()
            if not license_text or license_text == 'unknown':
                result['warnings'].append("No license information")
                result['health_score'] -= 5
        else:
            result['warnings'].append("Could not fetch package metadata")
            result['health_score'] -= 10
        
        result['health_score'] = max(0, min(100, result['health_score']))
        
        return result


class DependencyResolver:
    """Resolve and check for dependency conflicts."""
    
    def __init__(self, pip_command=None):
        self.pip_command = pip_command or [sys.executable, '-m', 'pip']
    
    def get_installed_packages(self) -> Dict[str, str]:
        """Get all currently installed packages."""
        packages = {}
        try:
            result = subprocess.run(
                self.pip_command + ['list', '--format=json'],
                capture_output=True,
                text=True,
                timeout=30
            )
            if result.returncode == 0:
                data = json.loads(result.stdout)
                for pkg in data:
                    packages[pkg['name'].lower()] = pkg['version']
        except Exception:
            pass
        return packages
    
    def check_dependency_tree(self, package_name: str) -> Tuple[bool, List[str]]:
        """
        Check if installing a package would cause conflicts.
        
        Returns:
            Tuple of (has_conflicts, conflict_messages)
        """
        conflicts = []
        
        try:
            # Use pip's dependency resolver in dry-run mode
            result = subprocess.run(
                self.pip_command + ['install', '--dry-run', '--report', '-', package_name],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            # Check stderr for conflict warnings
            if result.stderr:
                if 'conflict' in result.stderr.lower() or 'incompatible' in result.stderr.lower():
                    for line in result.stderr.splitlines():
                        if 'conflict' in line.lower() or 'incompatible' in line.lower():
                            conflicts.append(line.strip())
            
            # Also check stdout for JSON report (pip 22.2+)
            if result.stdout and result.stdout.startswith('{'):
                try:
                    report = json.loads(result.stdout)
                    if 'install' in report:
                        for item in report.get('install', []):
                            metadata = item.get('metadata', {})
                            if metadata.get('conflicts'):
                                conflicts.append(f"Conflict in {item.get('metadata', {}).get('name', 'unknown')}")
                except Exception:
                    pass
            
        except subprocess.TimeoutExpired:
            conflicts.append("Dependency check timed out")
        except Exception as e:
            conflicts.append(f"Could not check dependencies: {e}")
        
        return len(conflicts) > 0, conflicts
    
    def get_package_dependencies(self, package_name: str) -> List[str]:
        """Get direct dependencies of a package from PyPI."""
        try:
            url = f"https://pypi.org/pypi/{urllib.parse.quote(package_name)}/json"
            with urllib.request.urlopen(url, timeout=8) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                info = data.get('info', {})
                requires_dist = info.get('requires_dist', [])
                if requires_dist:
                    deps = []
                    for req in requires_dist:
                        # Parse requirement string (e.g., "numpy>=1.19.0")
                        dep_name = req.split('[')[0].split('>')[0].split('<')[0].split('=')[0].split('!')[0].strip()
                        if dep_name and not any(marker in req for marker in ['extra ==', '; extra']):
                            deps.append(dep_name)
                    return deps
        except Exception:
            pass
        return []


def check_conflicts_batch(packages: List[str], pip_command=None) -> Dict[str, List[str]]:
    """
    Check multiple packages for conflicts in batch.
    
    Returns:
        Dict mapping package names to list of conflict warnings
    """
    resolver = DependencyResolver(pip_command)
    results = {}
    
    for package in packages:
        has_conflicts, conflicts = resolver.check_dependency_tree(package)
        if has_conflicts:
            results[package] = conflicts
    
    return results
