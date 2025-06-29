document.addEventListener('DOMContentLoaded', function() {
  // Header scroll effect
  const header = document.querySelector('header');
  window.addEventListener('scroll', function() {
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });

  // Animate stats counter
  const statNumbers = document.querySelectorAll('.stat-number');
  if (statNumbers.length > 0) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateValue(entry.target, 0, parseInt(entry.target.getAttribute('data-count')), 2000);
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });

    statNumbers.forEach(stat => {
      observer.observe(stat);
    });
  }

  // Parallax effect for hero banner
  const parallaxBg = document.querySelector('.parallax-background');
  if (parallaxBg) {
    window.addEventListener('scroll', function() {
      const scrollPosition = window.pageYOffset;
      parallaxBg.style.transform = `translateZ(-1px) scale(1.1) translateY(${scrollPosition * 0.5}px)`;
    });
  }

  // Floating elements animation
  const floatingElements = document.querySelectorAll('.feature-card, .step');
  floatingElements.forEach(el => {
    el.addEventListener('mousemove', (e) => {
      const xAxis = (window.innerWidth / 2 - e.pageX) / 25;
      const yAxis = (window.innerHeight / 2 - e.pageY) / 25;
      el.style.transform = `rotateY(${xAxis}deg) rotateX(${yAxis}deg)`;
    });

    el.addEventListener('mouseenter', () => {
      el.style.transition = 'all 0.3s ease';
    });

    el.addEventListener('mouseleave', () => {
      el.style.transition = 'all 0.5s ease';
      el.style.transform = 'rotateY(0deg) rotateX(0deg)';
    });
  });
});

// Helper function for number animation
function animateValue(obj, start, end, duration) {
  let startTimestamp = null;
  const step = (timestamp) => {
    if (!startTimestamp) startTimestamp = timestamp;
    const progress = Math.min((timestamp - startTimestamp) / duration, 1);
    obj.innerHTML = Math.floor(progress * (end - start) + start);
    if (progress < 1) {
      window.requestAnimationFrame(step);
    }
  };
  window.requestAnimationFrame(step);
}