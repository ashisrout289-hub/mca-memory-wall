// 1. Typing Animation for the Batchmate Message
const message = "It all started with awkward first meetings, unknown faces and names, but slowly those strangers became friends and then turned into family. From simple “hi” to calling each other bhai and yaar, we never realized when the bond became so strong. The endless masti, backchodi and laughter in classrooms made every day unforgettable. We had our share of jhagde, but they never lasted long because our friendship was stronger. class time gossip, last-minute assignments, proxy attendance, and exam stress with last-night preparation—somehow we managed everything together. From fun moments and celebrations to helping each other in tough times, every memory became special. And now, as this journey ends, it’s hard to accept that these moments will never come back. We came as strangers in 2024, but we leave in 2026 as a family, you all are always present in my heart. ✨ LOVE YOU ❤️";
const textContainer = document.getElementById('animated-message');
let i = 0;

function typeWriter() {
    if (i < message.length) {
        textContainer.innerHTML += message.charAt(i);
        i++;
        setTimeout(typeWriter, 50);
    }
}

// 2. Loving Background Particles
function createHeart() {
    const hearts = ['❤️', '💖', '💗', '✨', '🌸'];
    const heart = document.createElement('div');
    heart.classList.add('floating-heart');
    heart.innerText = hearts[Math.floor(Math.random() * hearts.length)];
    heart.style.left = Math.random() * 100 + "vw";
    heart.style.fontSize = (Math.random() * 1 + 1) + "rem";
    
    const duration = Math.random() * 3 + 4;
    heart.style.animationDuration = duration + "s";
    
    document.body.appendChild(heart);
    setTimeout(() => heart.remove(), duration * 1000);
}
setInterval(createHeart, 400);

// 3. Scroll Reveal & Start Typing
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('reveal');
            // If it's the message card, start typing
            if (entry.target.querySelector('#animated-message')) {
                setTimeout(typeWriter, 1000);
            }
        }
    });
}, { threshold: 0.2 });

document.querySelectorAll('.card').forEach(card => observer.observe(card));

// 4. Form and Music Logic
function nextStep(step) {
    document.querySelectorAll('.form-step').forEach(s => s.style.display = 'none');
    document.getElementById('step' + step).style.display = 'block';
}

const music = document.getElementById('bgMusic');
const vid = document.getElementById('mainVideo');

window.addEventListener('click', () => {
    if(music.paused) { music.play(); music.volume = 0.3; }
}, {once: true});

vid.onplay = () => music.pause();
vid.onpause = () => music.play();