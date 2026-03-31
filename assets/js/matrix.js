// Matrix Rain Effect
(function () {
  const canvas = document.getElementById('matrix-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let w, h, cols, drops;
  const chars = 'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン0123456789ABCDEF><{}[]|/\\';
  const fontSize = 14;

  function init() {
    w = canvas.width = window.innerWidth;
    h = canvas.height = window.innerHeight;
    cols = Math.floor(w / fontSize);
    drops = Array(cols).fill(1).map(() => Math.random() * -100);
  }

  function draw() {
    ctx.fillStyle = 'rgba(5, 10, 14, 0.05)';
    ctx.fillRect(0, 0, w, h);

    ctx.font = `${fontSize}px 'Share Tech Mono', monospace`;

    for (let i = 0; i < cols; i++) {
      const char = chars[Math.floor(Math.random() * chars.length)];
      const x = i * fontSize;
      const y = drops[i] * fontSize;

      // Color variation
      const r = Math.random();
      if (r > 0.98) {
        ctx.fillStyle = '#ffffff';
      } else if (r > 0.9) {
        ctx.fillStyle = '#00ff9f';
      } else {
        ctx.fillStyle = '#00994d';
      }

      ctx.fillText(char, x, y);

      if (y > h && Math.random() > 0.975) {
        drops[i] = 0;
      }
      drops[i]++;
    }
  }

  init();
  window.addEventListener('resize', init);
  setInterval(draw, 40);
})();
