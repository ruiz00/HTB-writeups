// ── Typing Effect ──
const commands = [
  'whoami',
  'nmap -sV -sC target.htb',
  'cat /etc/passwd',
  'python3 exploit.py',
  'john --wordlist=rockyou.txt hash.txt',
  'docker run --rm -it -v /:/mnt alpine sh',
  'ls -la /root/',
];

let cmdIdx = 0, charIdx = 0, deleting = false;
const cmdEl = document.getElementById('typed-cmd');

function typeCmd() {
  if (!cmdEl) return;
  const current = commands[cmdIdx];
  if (!deleting) {
    cmdEl.textContent = current.substring(0, charIdx + 1);
    charIdx++;
    if (charIdx === current.length) {
      deleting = true;
      setTimeout(typeCmd, 1800);
      return;
    }
    setTimeout(typeCmd, 80);
  } else {
    cmdEl.textContent = current.substring(0, charIdx - 1);
    charIdx--;
    if (charIdx === 0) {
      deleting = false;
      cmdIdx = (cmdIdx + 1) % commands.length;
      setTimeout(typeCmd, 400);
      return;
    }
    setTimeout(typeCmd, 40);
  }
}
setTimeout(typeCmd, 800);

// ── Filter & Search (by difficulty) ──
const filterBtns = document.querySelectorAll('.filter-btn');
const cards = document.querySelectorAll('.writeup-card');
const searchInput = document.getElementById('search-input');

let activeFilter = 'all';

function applyFilters() {
  const query = searchInput ? searchInput.value.toLowerCase() : '';
  cards.forEach(card => {
    const diff = card.dataset.difficulty;
    const matchFilter = activeFilter === 'all' || diff === activeFilter;
    const title  = card.querySelector('.card-title')?.textContent.toLowerCase() || '';
    const tags   = Array.from(card.querySelectorAll('.tag')).map(t => t.textContent.toLowerCase()).join(' ');
    const matchSearch = !query || title.includes(query) || tags.includes(query);
    card.classList.toggle('hidden', !(matchFilter && matchSearch));
  });
}

filterBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    filterBtns.forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    activeFilter = btn.dataset.filter;
    applyFilters();
  });
});

if (searchInput) searchInput.addEventListener('input', applyFilters);

// ── Counter Animation ──
function animateCounter(el) {
  const target = parseInt(el.dataset.target);
  if (target === 0) { el.textContent = '0'; return; }
  const duration = 2000;
  const start = performance.now();
  function update(now) {
    const elapsed = now - start;
    const progress = Math.min(elapsed / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 3);
    el.textContent = Math.floor(eased * target).toLocaleString();
    if (progress < 1) requestAnimationFrame(update);
    else el.textContent = target.toLocaleString();
  }
  requestAnimationFrame(update);
}

// ── Intersection Observer for stats ──
const statsObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.querySelectorAll('.counter').forEach(animateCounter);
      statsObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.2 });

document.querySelectorAll('#stats').forEach(el => statsObserver.observe(el));

// ── Card entry animation ──
const cardObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry, i) => {
    if (entry.isIntersecting) {
      setTimeout(() => {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
      }, i * 80);
      cardObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });

cards.forEach(card => {
  card.style.opacity = '0';
  card.style.transform = 'translateY(24px)';
  card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
  cardObserver.observe(card);
});

// ── Scrollspy nav ──
const sections = document.querySelectorAll('section[id]');
const navLinks  = document.querySelectorAll('.nav-link');

const sectionObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      navLinks.forEach(link => {
        link.classList.toggle('active', link.getAttribute('href') === `#${entry.target.id}`);
      });
    }
  });
}, { threshold: 0.4 });

sections.forEach(s => sectionObserver.observe(s));

const style = document.createElement('style');
style.textContent = `.nav-link.active { color: var(--accent) !important; }
.nav-link.active::after { width: 100% !important; }`;
document.head.appendChild(style);
