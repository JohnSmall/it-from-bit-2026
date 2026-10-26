/* hopf-tower.js -- the Wigner's-friend chain on the Cayley-Dickson ladder.
 *
 * No dependencies, no build step, no network. Mount it with:
 *
 *     <link rel="stylesheet" href="hopf-tower.css">
 *     <div id="tower"></div>
 *     <script src="hopf-tower.js"></script>
 *     <script>HopfTower.mount(document.getElementById('tower'));</script>
 *
 * mount(el, opts) returns a handle with .next() .prev() .go(i) .play()
 * .pause() .destroy(). Options: {autoplay:true, dwell:7000, start:0}.
 *
 * The physics is the paper's, from Section "Where the chain goes next:
 * one more rung, then copies":
 *
 *   F's chart of S           S^3  -> S^2,  fibre S^1,  C,  one wire
 *   W's chart of {S,F}       S^7  -> S^4,  fibre S^3,  H,  two wires
 *   O_W's chart of {S,F,W}   S^15 -> S^8,  fibre S^7,  O,  three wires (last)
 *   the fourth observer      no fibration: the sedenions have zero divisors
 *                            and admit no S^31 -> S^16
 *
 * Aut(S) = G_2 x S_3 (Brown): the identity component is unchanged from the
 * octonions and the whole gain is a component group, an order-three
 * automorphism. That discrete choice among three is the generation label.
 * dim Der(A_n) = 0, 3, 14, 14, 14 for n = 1..5, flat at dim g_2 from the
 * octonions on. So the increments are a force, a force, a label, and then
 * the same finite permutation of copies at every step.
 */
(function (root) {
  'use strict';

  var RUNGS = [
    { alg: 'ℂ', who: 'F', long: 'the friend, charting S',
      wires: 'one wire', map: 'S³ → S²', fibre: 'S¹',
      tint: 'friend', adds: 'a force', mode: 'hopf', lat: [[0.72, 4]] },
    { alg: 'ℍ', who: 'W', long: 'Wigner, charting {S, F}',
      wires: 'two wires', map: 'S⁷ → S⁴', fibre: 'S³',
      tint: 'wigner', adds: 'a force', mode: 'hopf', lat: [[0.72, 4], [1.30, 6]] },
    { alg: '𝕆', who: 'O_W', long: 'the observer of Wigner, charting {S, F, W}',
      wires: 'three wires', map: 'S¹⁵ → S⁸', fibre: 'S⁷',
      tint: 'accent', adds: 'a force', mode: 'hopf', lat: [[0.55, 3], [0.95, 5], [1.35, 7]] },
    { alg: '𝕊', who: 'O_O_W', long: 'the fourth wire: the sedenions',
      wires: 'four wires', map: 'no fibration', fibre: '—',
      tint: 'accent', adds: 'a label', mode: 'stop' },
    { alg: '𝕋', who: '…', long: 'the fifth wire, and every wire after it',
      wires: 'five wires on', map: 'no fibration', fibre: '—',
      tint: 'dead', adds: 'copies', mode: 'copies' }
  ];

  var CAPTION = [
    'The friend charts the system. His own global phase is the <b>S¹ fibre</b>: ' +
    'gauge-private, with nothing observable in it to duplicate. What a copy takes is the base.',
    'Wigner charts the friend and the system together. Two wires, and the friend’s private ' +
    'phase is now <b>a recoverable fibre one rung up</b>. Gauge here, interferable above.',
    'The observer of Wigner charts all three. Three wires, the octonions, ' +
    '<b>and this is the last fibration the division algebras supply</b>.',
    'A fourth observer is a fourth wire, the sedenions. They have zero divisors and admit ' +
    '<b>no map S³¹ → S¹⁶</b>, so the promotion has no fourth instance. ' +
    'What the doubling adds is finite: Aut(𝕊) = G₂ × S₃, a third of a ' +
    'turn, and that discrete choice among three is the generation label.',
    'Every further doubling adds one more S₃ and nothing else. The derivation algebra is ' +
    '𝔤₂ from the octonions onward, flat at 14. The chain is <b>unbounded in ' +
    'length and bounded in type</b>: a force, a force, a label, then copies.'
  ];

  var DIMS = [0, 3, 14, 14, 14];
  var TINTS = { friend: '#4fb3d9', wigner: '#e0893b', accent: '#c45b8c', dead: '#6c6a68' };
  var DIM = '#8b8782';

  function el(tag, cls, html) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (html != null) n.innerHTML = html;
    return n;
  }

  /* One Hopf fibre over the base point (theta, phi), stereographed to R^3.
     z1 = cos(th/2) e^{it}, z2 = sin(th/2) e^{i(t-phi)} maps to
     (sin th e^{i phi}, cos th), so this is the fibre over the point we mean. */
  function fibre(theta, phi, n, spin) {
    var pts = [], i, t, c = Math.cos(theta / 2), s = Math.sin(theta / 2), d;
    for (i = 0; i <= n; i++) {
      t = (i / n) * Math.PI * 2 + spin;
      d = 1 - s * Math.sin(t - phi);
      if (Math.abs(d) < 1e-4) d = 1e-4;
      pts.push([c * Math.cos(t) / d, c * Math.sin(t) / d, s * Math.cos(t - phi) / d]);
    }
    return pts;
  }

  function project(p, yaw, pitch, scale, cx, cy) {
    var cosY = Math.cos(yaw), sinY = Math.sin(yaw),
        cosP = Math.cos(pitch), sinP = Math.sin(pitch),
        x = p[0] * cosY - p[1] * sinY,
        y = p[0] * sinY + p[1] * cosY,
        z = p[2],
        y2 = y * cosP - z * sinP,
        z2 = y * sinP + z * cosP,
        depth = 3.6 / (3.6 + z2);
    return [cx + x * scale * depth, cy - y2 * scale * depth, depth];
  }

  function Painter(canvas) {
    this.c = canvas;
    this.ctx = canvas.getContext('2d');
    this.t = 0;
    this.rung = 0;
    this.enter = 0;
  }

  Painter.prototype.size = function () {
    var r = this.c.getBoundingClientRect(),
        dpr = Math.min(window.devicePixelRatio || 1, 2);
    if (!r.width || !r.height) return false;
    var w = Math.round(r.width * dpr), h = Math.round(r.height * dpr);
    if (this.c.width !== w || this.c.height !== h) { this.c.width = w; this.c.height = h; }
    return true;
  };

  Painter.prototype.draw = function (dt, reduced) {
    if (!this.size()) return;
    if (!reduced) this.t += dt;
    this.enter = Math.min(1, this.enter + dt * 1.6);
    var ctx = this.ctx, W = this.c.width, H = this.c.height,
        cx = W / 2, cy = H / 2, S = Math.min(W, H) * 0.30,
        r = RUNGS[this.rung], tint = TINTS[r.tint],
        ease = this.enter * this.enter * (3 - 2 * this.enter);
    ctx.clearRect(0, 0, W, H);
    ctx.lineJoin = 'round'; ctx.lineCap = 'round';
    if (r.mode === 'hopf') this.hopf(cx, cy, S, r, ease);
    else if (r.mode === 'stop') this.stop(cx, cy, S, tint, ease);
    else this.copies(cx, cy, S, ease);
  };

  Painter.prototype.hopf = function (cx, cy, S, r, ease) {
    var ctx = this.ctx, yaw = this.t * 0.22, pitch = 0.46, self = this;
    var bands = r.lat, total = 0, drawn = 0, b, j;
    for (b = 0; b < bands.length; b++) total += bands[b][1];
    ctx.lineWidth = Math.max(1.4, S * 0.016);
    for (b = 0; b < bands.length; b++) {
      for (j = 0; j < bands[b][1]; j++) {
        if (drawn / total > ease) break;
        var pts = fibre(bands[b][0], (j / bands[b][1]) * Math.PI * 2, 128, self.t * 0.5),
            k, p, first = true;
        ctx.beginPath();
        ctx.strokeStyle = bands.length === 1 ? TINTS[r.tint]
          : ['#4fb3d9', '#9a7bd0', '#c45b8c'][b % 3];
        ctx.globalAlpha = 0.85;
        for (k = 0; k < pts.length; k++) {
          p = project(pts[k], yaw, pitch, S * 0.62, cx, cy);
          if (first) { ctx.moveTo(p[0], p[1]); first = false; } else ctx.lineTo(p[0], p[1]);
        }
        ctx.stroke();
        drawn++;
      }
    }
    ctx.globalAlpha = 1;
  };

  Painter.prototype.stop = function (cx, cy, S, tint, ease) {
    /* no fourth fibration: a broken arrow, and the one discrete third of a turn */
    var ctx = this.ctx, i, th, R = S * 0.52;
    ctx.globalAlpha = ease;
    ctx.setLineDash([S * 0.09, S * 0.07]);
    ctx.strokeStyle = DIM; ctx.lineWidth = Math.max(1.2, S * 0.012);
    ctx.beginPath(); ctx.arc(cx, cy, R, 0, Math.PI * 2); ctx.stroke();
    ctx.setLineDash([]);
    var spin = this.t * 0.7, cols = ['#4fb3d9', '#e0893b', '#c45b8c'];
    for (i = 0; i < 3; i++) {
      th = -Math.PI / 2 + (i * 2 * Math.PI) / 3 + Math.floor(spin) * (2 * Math.PI / 3)
           + (2 * Math.PI / 3) * (function (x) { return x * x * (3 - 2 * x); })(Math.min(1, (spin % 1) * 2.2));
      ctx.beginPath();
      ctx.fillStyle = cols[i];
      ctx.arc(cx + R * Math.cos(th), cy + R * Math.sin(th), Math.max(4, S * 0.075), 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.globalAlpha = 1;
  };

  Painter.prototype.copies = function (cx, cy, S, ease) {
    /* dim Der(A_n) = 0, 3, 14, 14, 14 -- flat at dim g_2 */
    var ctx = this.ctx, i, n = DIMS.length,
        bw = S * 0.30, gap = S * 0.17,
        x0 = cx - ((n * bw + (n - 1) * gap) / 2),
        base = cy + S * 0.72, unit = (S * 1.22) / 14,
        cols = ['#4fb3d9', '#e0893b', '#c45b8c', '#6c6a68', '#6c6a68'],
        labels = ['ℂ', 'ℍ', '𝕆', '𝕊', '𝕋'];
    ctx.globalAlpha = ease;
    ctx.textAlign = 'center';
    for (i = 0; i < n; i++) {
      var h = Math.max(DIMS[i] * unit, S * 0.015), x = x0 + i * (bw + gap);
      ctx.fillStyle = cols[i];
      ctx.fillRect(x, base - h, bw, h);
      ctx.fillStyle = '#e8e6e3';
      ctx.font = (S * 0.17) + 'px ui-sans-serif, system-ui, sans-serif';
      ctx.fillText(String(DIMS[i]), x + bw / 2, base - h - S * 0.10);
      ctx.fillStyle = cols[i];
      ctx.font = 'italic ' + (S * 0.19) + 'px ui-sans-serif, system-ui, sans-serif';
      ctx.fillText(labels[i], x + bw / 2, base + S * 0.23);
    }
    var y = base - 14 * unit;
    ctx.strokeStyle = '#c45b8c'; ctx.lineWidth = Math.max(1.2, S * 0.012);
    ctx.setLineDash([S * 0.08, S * 0.06]);
    ctx.beginPath(); ctx.moveTo(x0 + 2 * (bw + gap) - gap * 0.4, y);
    ctx.lineTo(x0 + n * bw + (n - 1) * gap, y); ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle = '#c45b8c';
    ctx.font = (S * 0.13) + 'px ui-sans-serif, system-ui, sans-serif';
    ctx.fillText('flat at dim 𝔤₂ = 14', cx + S * 0.30, y - S * 0.16);
    ctx.globalAlpha = 1;
  };

  function mount(host, opts) {
    if (!host) throw new Error('HopfTower.mount: no host element');
    opts = opts || {};
    var dwell = opts.dwell || 7000,
        reduced = window.matchMedia &&
                  window.matchMedia('(prefers-reduced-motion: reduce)').matches,
        idx = Math.min(RUNGS.length - 1, Math.max(0, opts.start || 0)),
        playing = opts.autoplay !== false && !reduced,
        raf = null, last = 0, acc = 0, dead = false;

    host.classList.add('hopf-tower');
    host.innerHTML = '';
    host.appendChild(el('p', 'hopf-tower__head', 'The chain of observers, rung by rung'));
    host.appendChild(el('p', 'hopf-tower__sub',
      'System → friend → Wigner → the observer of Wigner → and on. ' +
      'Each new wire is one rung of the Cayley–Dickson ladder.'));

    var stage = el('div', 'hopf-tower__stage');
    var wrap = el('div', 'hopf-tower__canvas-wrap');
    var canvas = el('canvas', 'hopf-tower__canvas');
    canvas.setAttribute('role', 'img');
    wrap.appendChild(canvas); stage.appendChild(wrap);

    var ladder = el('div', 'hopf-tower__ladder'), rungEls = [];
    RUNGS.forEach(function (r, i) {
      var row = el('div', 'hopf-tower__rung');
      row.setAttribute('data-tint', r.tint);
      row.appendChild(el('span', 'hopf-tower__alg', r.alg));
      row.appendChild(el('span', 'hopf-tower__who',
        r.wires + '<small>' + r.long + '</small>'));
      var m = el('span', 'hopf-tower__map',
        r.map + (r.fibre !== '—' ? '  ·  fibre ' + r.fibre : ''));
      if (r.fibre === '—') m.setAttribute('data-none', '1');
      row.appendChild(m);
      ladder.appendChild(row); rungEls.push(row);
    });
    stage.appendChild(ladder);
    host.appendChild(stage);

    var cap = el('p', 'hopf-tower__caption');
    cap.setAttribute('aria-live', 'polite');
    host.appendChild(cap);

    var bar = el('div', 'hopf-tower__bar');
    var bPrev = el('button', 'hopf-tower__btn', '‹ back');
    var bPlay = el('button', 'hopf-tower__btn', playing ? 'pause' : 'play');
    var bNext = el('button', 'hopf-tower__btn', 'next ›');
    bar.appendChild(bPrev); bar.appendChild(bPlay); bar.appendChild(bNext);
    var dots = el('div', 'hopf-tower__dots'), dotEls = [];
    RUNGS.forEach(function (r, i) {
      var d = el('button', 'hopf-tower__dot');
      d.type = 'button';
      d.setAttribute('aria-label', 'rung ' + (i + 1) + ': ' + r.alg);
      d.addEventListener('click', function () { go(i); pause(); });
      dots.appendChild(d); dotEls.push(d);
    });
    bar.appendChild(dots); host.appendChild(bar);

    var prog = el('div', 'hopf-tower__progress'); var progI = el('i');
    prog.appendChild(progI); host.appendChild(prog);

    var painter = new Painter(canvas);

    function render() {
      rungEls.forEach(function (row, i) {
        row.setAttribute('data-on', i <= idx ? '1' : '0');
        row.setAttribute('data-current', i === idx ? '1' : '0');
      });
      dotEls.forEach(function (d, i) { d.setAttribute('data-on', i === idx ? '1' : '0'); });
      cap.innerHTML = CAPTION[idx];
      canvas.setAttribute('aria-label', RUNGS[idx].long + '. ' + RUNGS[idx].map + '.');
      bPrev.disabled = idx === 0;
      bNext.disabled = idx === RUNGS.length - 1;
      painter.rung = idx; painter.enter = 0; acc = 0;
    }
    function go(i) {
      i = Math.max(0, Math.min(RUNGS.length - 1, i));
      if (i !== idx) { idx = i; render(); }
    }
    function next() { go(idx + 1 >= RUNGS.length ? 0 : idx + 1); }
    function prev() { go(idx - 1); }
    function play() { playing = true; bPlay.textContent = 'pause'; }
    function pause() { playing = false; bPlay.textContent = 'play'; progI.style.width = '0%'; }

    bPrev.addEventListener('click', function () { prev(); pause(); });
    bNext.addEventListener('click', function () { next(); pause(); });
    bPlay.addEventListener('click', function () { playing ? pause() : play(); });
    host.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') { next(); pause(); e.preventDefault(); }
      if (e.key === 'ArrowLeft') { prev(); pause(); e.preventDefault(); }
    });
    host.tabIndex = host.tabIndex || 0;

    function frame(now) {
      if (dead) return;
      var dt = last ? Math.min(0.05, (now - last) / 1000) : 0;
      last = now;
      painter.draw(dt, reduced);
      if (playing) {
        acc += dt * 1000;
        progI.style.width = Math.min(100, (acc / dwell) * 100) + '%';
        if (acc >= dwell) next();
      }
      raf = window.requestAnimationFrame(frame);
    }

    render();
    raf = window.requestAnimationFrame(frame);

    return {
      next: next, prev: prev, go: go, play: play, pause: pause,
      get index() { return idx; },
      destroy: function () {
        dead = true;
        if (raf) window.cancelAnimationFrame(raf);
        host.innerHTML = '';
        host.classList.remove('hopf-tower');
      }
    };
  }

  var api = { mount: mount, rungs: RUNGS };
  if (typeof module === 'object' && module.exports) module.exports = api;
  root.HopfTower = api;
})(typeof window !== 'undefined' ? window : this);
