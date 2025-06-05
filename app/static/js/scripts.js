document.addEventListener('DOMContentLoaded', function() {
    const carousel = document.getElementById('achievementsCarousel');
    if (!carousel) return;

    const track = carousel.querySelector('.carousel-track');
    const slides = Array.from(track.querySelectorAll('.carousel-slide'));
    const dots = Array.from(document.querySelectorAll('.dot'));
    const prevButton = carousel.querySelector('.carousel-arrow-left');
    const nextButton = carousel.querySelector('.carousel-arrow-right');

    let currentSlide = 0;
    let isMoving = false;
    const slideWidth = carousel.offsetWidth;

    // Initialize first slide and add active class
    slides[0].classList.add('active');

    function updateDots() {
        dots.forEach((dot, index) => {
            dot.classList.toggle('active', index === currentSlide);
        });
    }

    function moveToSlide(index) {
        if (isMoving) return;
        if (index < 0) index = slides.length - 1;
        if (index >= slides.length) index = 0;

        isMoving = true;
        
        // Remove active class from current slide
        slides[currentSlide].classList.remove('active');
        
        // Update track transform
        track.style.transform = `translateX(-${index * slideWidth}px)`;
        
        // Update current slide
        currentSlide = index;
        
        // Add active class to new slide
        slides[currentSlide].classList.add('active');
        
        // Update dots
        updateDots();

        // Reset isMoving after transition
        setTimeout(() => {
            isMoving = false;
        }, 450); // Match CSS transition duration
    }

    // Event Listeners
    prevButton.addEventListener('click', () => moveToSlide(currentSlide - 1));
    nextButton.addEventListener('click', () => moveToSlide(currentSlide + 1));

    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => moveToSlide(index));
    });

    // Optional: Auto advance slides
    let autoAdvance = setInterval(() => moveToSlide(currentSlide + 1), 20000);

    // Pause auto-advance on hover
    carousel.addEventListener('mouseenter', () => clearInterval(autoAdvance));
    carousel.addEventListener('mouseleave', () => {
        autoAdvance = setInterval(() => moveToSlide(currentSlide + 1), 20000);
    });

    // Handle keyboard navigation
    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowLeft') {
            moveToSlide(currentSlide - 1);
        } else if (e.key === 'ArrowRight') {
            moveToSlide(currentSlide + 1);
        }
    });

    // Handle resize
    let resizeTimer;
    window.addEventListener('resize', () => {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(() => {
            // Update slide width and position on resize
            const newSlideWidth = carousel.offsetWidth;
            track.style.transition = 'none';
            track.style.transform = `translateX(-${currentSlide * newSlideWidth}px)`;
            setTimeout(() => {
                track.style.transition = '';
            }, 50);
        }, 250);
    });

    // Handle touch events for mobile
    let touchStartX = 0;
    let touchEndX = 0;

    carousel.addEventListener('touchstart', (e) => {
        touchStartX = e.touches[0].clientX;
    }, false);

    carousel.addEventListener('touchmove', (e) => {
        touchEndX = e.touches[0].clientX;
    }, false);

    carousel.addEventListener('touchend', () => {
        const swipeDistance = touchEndX - touchStartX;
        if (Math.abs(swipeDistance) > 50) { // Minimum swipe distance
            if (swipeDistance > 0) {
                moveToSlide(currentSlide - 1); // Swipe right
            } else {
                moveToSlide(currentSlide + 1); // Swipe left
            }
        }
    }, false);
});