window.onload = function () {
    const images = document.querySelectorAll('img');
    images.forEach(function (img) {
        img.style.opacity = 0;
        img.style.transition = "opacity 1s ease-in-out";
        img.onload = () => { img.style.opacity = 1; };
    });
};
