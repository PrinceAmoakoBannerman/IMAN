// JS: trigger on load and toggle on scroll
document.addEventListener('DOMContentLoaded', () => {
  const heroContent = document.querySelector('.hero-content');
  heroContent.classList.add('h1-visible'); // animate in on page load

  let lastY = window.pageYOffset;
  window.addEventListener('scroll', () => {
    const currentY = window.pageYOffset;
    if (currentY > lastY) {
      // scrolling down
      heroContent.classList.remove('h1-visible');
      heroContent.classList.add('h1-hidden');
    } else {
      // scrolling up
      heroContent.classList.remove('h1-hidden');
      heroContent.classList.add('h1-visible');
    }
    lastY = currentY;
  });
});


document.addEventListener('DOMContentLoaded', () => {
  // SLIDESHOW
  const slides = document.querySelectorAll('.hero .slide');
  let current = 0; // first slide already has `active` class in HTML

  setInterval(() => {
    slides[current].classList.remove('active');
    current = (current + 1) % slides.length;
    slides[current].classList.add('active');
  }, 10000); // switch every 5s

  // BUTTON HANDLERS
  document.querySelector('.watch-more').addEventListener('click', () => {
    console.log('OUR STORY clicked');
    // e.g. document.querySelector('#story').scrollIntoView({ behavior: 'smooth' });
  });
 
});

document.addEventListener('DOMContentLoaded', () => {
  const dragBtn = document.querySelector('.drag-btn');

  dragBtn.addEventListener('mousedown', () => {
    dragBtn.textContent = 'DRAGGING…';
  });
  document.addEventListener('mouseup', () => {
    dragBtn.textContent = 'DRAG >>>';
  });
});

// GALLERY 
  const track = document.querySelector('.carousel-track');
  const prevBtn = document.querySelector('.carousel-btn.prev');
  const nextBtn = document.querySelector('.carousel-btn.next');

  // Arrow‐button scrolling
  nextBtn.addEventListener('click', () => {
    track.scrollBy({ left: track.clientWidth * 0.8 + 16, behavior: 'smooth' });
  });
  prevBtn.addEventListener('click', () => {
    track.scrollBy({ left: -(track.clientWidth * 0.8 + 16), behavior: 'smooth' });
  });

  // Dragging behavior
  let isDown = false, startX, scrollLeft;
  track.addEventListener('mousedown', e => {
    isDown = true;
    track.classList.add('dragging');
    startX = e.pageX - track.offsetLeft;
    scrollLeft = track.scrollLeft;
  });
  track.addEventListener('mouseup', () => {
    isDown = false;
    track.classList.remove('dragging');
  });
  track.addEventListener('mouseleave', () => {
    isDown = false;
    track.classList.remove('dragging');
  });
  track.addEventListener('mousemove', e => {
    if (!isDown) return;
    e.preventDefault();
    const x = e.pageX - track.offsetLeft;
    const walk = (x - startX) * 1.5; // scroll-fast factor
    track.scrollLeft = scrollLeft - walk;
  });

  // Touch support
  track.addEventListener('touchstart', e => {
    isDown = true;
    startX = e.touches[0].pageX - track.offsetLeft;
    scrollLeft = track.scrollLeft;
  });
  track.addEventListener('touchend', () => isDown = false);
  track.addEventListener('touchmove', e => {
    if (!isDown) return;
    const x = e.touches[0].pageX - track.offsetLeft;
    const walk = (x - startX) * 1.5;
    track.scrollLeft = scrollLeft - walk;
  });




