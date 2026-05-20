/**
 * main.js - JavaScript principal del proyecto NeuroIA
 * Maneja animaciones, scroll effects y comportamiento dinámico del navbar.
 */

document.addEventListener('DOMContentLoaded', function () {

    // === NAVBAR SCROLL EFFECT ===
    const navbar = document.getElementById('mainNavbar');
    if (navbar) {
        window.addEventListener('scroll', function () {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }

    // === SCROLL ANIMATIONS (Intersection Observer) ===
    const animatedElements = document.querySelectorAll('.animate-on-scroll');
    if (animatedElements.length > 0) {
        const observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

        animatedElements.forEach(function (el) {
            observer.observe(el);
        });
    }

    // === AUTO-DISMISS ALERTS ===
    const alerts = document.querySelectorAll('.neon-alert');
    alerts.forEach(function (alert) {
        setTimeout(function () {
            var bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
            if (bsAlert) bsAlert.close();
        }, 5000);
    });

    // === 3D CARD TILT EFFECT ===
    const cards3d = document.querySelectorAll('.card-3d, .text-box-glass');
    cards3d.forEach(function (card) {
        card.addEventListener('mousemove', function (e) {
            var rect = card.getBoundingClientRect();
            var x = e.clientX - rect.left;
            var y = e.clientY - rect.top;
            var centerX = rect.width / 2;
            var centerY = rect.height / 2;
            var rotateX = (y - centerY) / 30;
            var rotateY = (centerX - x) / 30;
            card.style.transform = 'perspective(1000px) rotateX(' + rotateX + 'deg) rotateY(' + rotateY + 'deg) translateY(-5px)';
            card.style.boxShadow = (centerX - x)/5 + 'px ' + (centerY - y)/5 + 'px 30px rgba(0,255,136,0.2)';
        });
        card.addEventListener('mouseleave', function () {
            card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) translateY(0)';
            card.style.boxShadow = '';
        });
    });

    // === MAGNETIC BUTTONS ===
    const magneticBtns = document.querySelectorAll('.btn-lg');
    magneticBtns.forEach(btn => {
        btn.addEventListener('mousemove', function(e) {
            const rect = btn.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;
            btn.style.transform = `translate(${x * 0.3}px, ${y * 0.3}px)`;
        });
        btn.addEventListener('mouseleave', function() {
            btn.style.transform = `translate(0, 0)`;
        });
    });

    // === HERO PARALLAX ===
    var heroImage = document.getElementById('hero-image');
    if (heroImage) {
        window.addEventListener('scroll', function () {
            var scrolled = window.scrollY;
            heroImage.style.transform = 'translateY(' + (scrolled * 0.15) + 'px)';
        });
    }

    // === PARTICLES BACKGROUND ===
    var particlesContainer = document.getElementById('hero-particles');
    if (particlesContainer) {
        for (var i = 0; i < 30; i++) {
            var particle = document.createElement('div');
            particle.style.cssText = 'position:absolute;width:' + (Math.random() * 4 + 1) + 'px;height:' + (Math.random() * 4 + 1) + 'px;background:' + (Math.random() > 0.5 ? 'rgba(0,255,136,0.3)' : 'rgba(255,79,216,0.3)') + ';border-radius:50%;top:' + (Math.random() * 100) + '%;left:' + (Math.random() * 100) + '%;animation:particleFloat ' + (Math.random() * 10 + 5) + 's ease-in-out infinite;animation-delay:' + (Math.random() * 5) + 's;';
            particlesContainer.appendChild(particle);
        }
        // Add particle animation
        var style = document.createElement('style');
        style.textContent = '@keyframes particleFloat{0%,100%{transform:translate(0,0);opacity:0.3;}25%{transform:translate(' + (Math.random()*40-20) + 'px,' + (Math.random()*40-20) + 'px);opacity:0.8;}50%{transform:translate(' + (Math.random()*60-30) + 'px,' + (Math.random()*60-30) + 'px);opacity:0.4;}75%{transform:translate(' + (Math.random()*40-20) + 'px,' + (Math.random()*40-20) + 'px);opacity:0.7;}}';
        document.head.appendChild(style);
    }

});
