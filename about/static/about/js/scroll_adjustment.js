document.addEventListener("DOMContentLoaded", function() {
    if (window.location.hash) {
        setTimeout(function() {
            window.scrollTo(window.scrollX, window.scrollY - 500);
        }, 10);
    }
});

// For within page navigation
document.querySelectorAll('a[href^="#contact-us"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        let target = document.querySelector(this.getAttribute('href'));
        const headerHeight = document.querySelector('header').offsetHeight;
        if (target) {

            console.log(target.offsetTop, headerHeight);

            window.scrollTo({
                top: target.offsetTop - headerHeight,
                behavior: 'smooth'
            });
        } else {

            console.log('Target element not found:', this.getAttribute('href'));
        }
    });
});