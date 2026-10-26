#!/usr/bin/env python3
"""render_wigners_friend_hopf_video_2026-10-21T1000.py

A short explainer video for Section~\ref{sec:wigners-friend}, "Wigner's friend
in the Hopf picture". Every claim on screen is taken from
paper1/wigners_friend_in_the_hopf_picture_2026-06-13.tex; nothing is invented
for the animation. The four facts it has to carry:

  1. The S^1 fibre of S^1 -> S^3 -> S^2 is the global phase: the friend's
     gauge-private self-ignorance. The base S^2 is gauge-invariant and is what
     a copy can duplicate. FANOUT copies a base-point; the operation commits to
     a fibre-point, and the gap between the two is the gauge character of the
     fibre.
  2. For two qubits the relevant fibration is quaternionic, S^3 -> S^7 -> S^4
     (Mosseri-Dandoloff), and measurement carries the joint state from the
     surface of the entanglement ball to its interior.
  3. The two accounts are bound by C^2 + r^2 = 1. The friend is at the surface
     (r=1, pure); Wigner is in the interior (r<1, mixed). Same state on S^7,
     two charts.
  4. Objectivity is redundancy: R=1 is the friend's relative fact, reversible
     by Wigner; R >> 1 is an objective fact. One axis, two ends.

Closing beat: the ball has a unique centre and no point beyond it, so a
Popescu-Rohrlich box would need r^2 = -2. The Tsirelson bound is the roundness
of the ball.

No randomness, no hidden state: every frame is a pure function of its index.
Output is H.264 via ffmpeg. `--preview N` renders frame N to a PNG instead,
which is how the layout was checked without paying for a full encode.
"""
import argparse
import subprocess
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "media" / "wigners_friend_hopf_2026-10-21.mp4"
FPS = 30

INK = "#e8e6e3"
DIM = "#8b8782"
BG = "#121316"
FRIEND = "#4fb3d9"      # the private chart: phase, fibre, surface
WIGNER = "#e0893b"      # the public chart: record, base, interior
ACCENT = "#c45b8c"

# (name, seconds) -- the cut list
SCENES = [("title", 7), ("paradox", 11), ("hopf", 17), ("plunge", 16),
          ("charts", 12), ("ladder", 12), ("tsirelson", 10), ("close", 6)]
BOUNDS, _t = [], 0
for _n, _s in SCENES:
    BOUNDS.append((_n, _t, _t + _s * FPS))
    _t += _s * FPS
TOTAL = _t


def ease(x):
    """Smoothstep on [0,1]; keeps motion off the linear ramp."""
    x = np.clip(x, 0.0, 1.0)
    return x * x * (3.0 - 2.0 * x)


def fade(local, n, hold=0.12):
    """Opacity envelope: fade in, hold, fade out."""
    f = local / n
    a = np.clip(f / hold, 0, 1)
    b = np.clip((1 - f) / hold, 0, 1)
    return float(min(a, b))


def hopf_fibre(theta, phi, n=400, twist=0.0):
    """The S^1 fibre over the base point (theta, phi), stereographed to R^3.

    z1 = cos(theta/2) e^{i t}, z2 = sin(theta/2) e^{i(t - phi)} satisfies
    (2 z1 conj(z2), |z1|^2 - |z2|^2) = (sin theta e^{i phi}, cos theta),
    which is the Hopf map onto the intended base point.
    """
    t = np.linspace(0, 2 * np.pi, n) + twist
    z1 = np.cos(theta / 2) * np.exp(1j * t)
    z2 = np.sin(theta / 2) * np.exp(1j * (t - phi))
    x1, x2, x3, x4 = z1.real, z1.imag, z2.real, z2.imag
    d = 1.0 - x4
    d = np.where(np.abs(d) < 1e-6, 1e-6, d)
    return x1 / d, x2 / d, x3 / d


def sphere(ax, r=1.0, c=DIM, alpha=0.10, n=26):
    u = np.linspace(0, 2 * np.pi, n * 2)
    v = np.linspace(0, np.pi, n)
    ax.plot_surface(r * np.outer(np.cos(u), np.sin(v)),
                    r * np.outer(np.sin(u), np.sin(v)),
                    r * np.outer(np.ones_like(u), np.cos(v)),
                    color=c, alpha=alpha, linewidth=0, shade=False)


def wire(ax, r=1.0, c=DIM, alpha=0.30, n=13):
    u = np.linspace(0, 2 * np.pi, 49)
    for th in np.linspace(0.001, np.pi - 0.001, n // 2 + 2)[1:-1]:
        ax.plot(r * np.sin(th) * np.cos(u), r * np.sin(th) * np.sin(u),
                r * np.cos(th) * np.ones_like(u), color=c, lw=0.7, alpha=alpha)
    v = np.linspace(0, np.pi, 33)
    for ph in np.linspace(0, 2 * np.pi, n, endpoint=False):
        ax.plot(r * np.sin(v) * np.cos(ph), r * np.sin(v) * np.sin(ph),
                r * np.cos(v), color=c, lw=0.7, alpha=alpha)


def bare3d(ax, lim):
    ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim); ax.set_zlim(-lim, lim)
    ax.set_axis_off()
    ax.patch.set_alpha(0.0)
    ax.set_facecolor("none")
    for pane in (ax.xaxis, ax.yaxis, ax.zaxis):
        try:
            pane.set_pane_color((0, 0, 0, 0))
        except Exception:
            pass
    try:
        ax.set_box_aspect((1, 1, 1))
    except Exception:
        pass


def text(fig, x, y, s, size=20, c=INK, a=1.0, weight="normal", ha="center", style="normal"):
    if a <= 0.01:
        return
    fig.text(x, y, s, color=c, fontsize=size, alpha=a, ha=ha, va="center",
             weight=weight, style=style, family="DejaVu Sans")


# --------------------------------------------------------------------------
# scenes
# --------------------------------------------------------------------------

def sc_title(fig, k, n):
    a = fade(k, n, 0.18)
    text(fig, .5, .62, "Wigner's friend", 54, INK, a, "bold")
    text(fig, .5, .50, "in the Hopf picture", 54, FRIEND, a, "bold")
    text(fig, .5, .36, "one state, two charts, and the redundancy ladder", 23, DIM,
         fade(max(0, k - 30), max(1, n - 30), 0.18))


def sc_paradox(fig, k, n):
    a = fade(k, n, 0.10)
    text(fig, .5, .88, "The problem", 26, ACCENT, a, "bold")
    ax = fig.add_axes([.08, .30, .84, .46]); ax.set_axis_off()
    ax.set_xlim(0, 10); ax.set_ylim(0, 5)
    s = ease((k - 10) / 45)
    if s > 0:
        ax.add_patch(plt.Circle((2.1, 2.6), .52, color=INK, alpha=.85 * a * s))
        ax.text(2.1, 2.6, "S", ha="center", va="center", fontsize=22, color=BG, weight="bold", alpha=a * s)
        ax.text(2.1, 1.75, "a qubit", ha="center", fontsize=15, color=DIM, alpha=a * s)
    s = ease((k - 50) / 45)
    if s > 0:
        ax.add_patch(plt.Circle((5.0, 2.6), .52, color=FRIEND, alpha=.85 * a * s))
        ax.text(5.0, 2.6, "F", ha="center", va="center", fontsize=22, color=BG, weight="bold", alpha=a * s)
        ax.text(5.0, 1.75, "the friend, who measures it", ha="center", fontsize=15, color=FRIEND, alpha=a * s)
        ax.annotate("", (4.4, 2.6), (2.7, 2.6),
                    arrowprops=dict(arrowstyle="-|>", color=INK, lw=2.0, alpha=a * s))
    s = ease((k - 95) / 45)
    if s > 0:
        ax.add_patch(plt.Circle((8.0, 2.6), .52, color=WIGNER, alpha=.85 * a * s))
        ax.text(8.0, 2.6, "W", ha="center", va="center", fontsize=22, color=BG, weight="bold", alpha=a * s)
        ax.text(8.0, 1.75, "Wigner, outside the lab", ha="center", fontsize=15, color=WIGNER, alpha=a * s)
        ax.plot([6.5, 6.5], [.7, 4.5], color=DIM, lw=1.4, ls=(0, (5, 4)), alpha=a * s)
        ax.text(6.5, 4.75, "the lab wall", ha="center", fontsize=13, color=DIM, alpha=a * s)
    s = fade(max(0, k - 150), max(1, n - 150), 0.14)
    text(fig, .5, .20, "For the friend the measurement is over and the outcome is definite.", 20, FRIEND, s)
    text(fig, .5, .13, "For Wigner the lab is still one undivided superposition.", 20, WIGNER, s)


def sc_hopf(fig, k, n):
    a = fade(k, n, 0.10)
    text(fig, .5, .93, "What a copy can carry, and what it cannot", 26, ACCENT, a, "bold")
    ax = fig.add_axes([.01, .13, .54, .76], projection="3d")
    bare3d(ax, 2.15)
    ax.view_init(elev=28, azim=(k * 0.30) % 360)
    # fibres over a ring of base points: the linked circles of S^1 -> S^3 -> S^2
    # three latitudes on the base; the fibres over each form a linked torus.
    # theta is kept below ~1.4 so 1 - x4 stays off zero and the projection
    # does not throw a fibre out of frame.
    lat = [(0.72, 5), (1.30, 7)]
    drawn = 0
    budget = int(np.clip((k - 15) / 5.5, 0, 12))
    for li, (th, cnt) in enumerate(lat):
        for j in range(cnt):
            if drawn >= budget:
                break
            ph = 2 * np.pi * j / cnt
            X, Y, Z = hopf_fibre(th, ph)
            ax.plot(X, Y, Z, color=plt.cm.cool(0.08 + 0.72 * li), lw=2.3, alpha=0.9 * a)
            drawn += 1
    text(fig, .28, .10, "each ring is one fibre: a whole circle of global phase", 16, DIM, a)
    # the base sphere
    ax2 = fig.add_axes([.57, .24, .36, .54], projection="3d")
    bare3d(ax2, 1.15)
    ax2.view_init(elev=28, azim=(k * 0.30) % 360)
    wire(ax2, 1.0, DIM, 0.30)
    s = ease((k - 90) / 60)
    if s > 0:
        for li, (th, cnt) in enumerate([(0.72, 5), (1.30, 7)]):
            for j in range(cnt):
                ph = 2 * np.pi * j / cnt
                ax2.scatter([np.sin(th) * np.cos(ph)], [np.sin(th) * np.sin(ph)],
                            [np.cos(th)], color=plt.cm.cool(0.08 + 0.72 * li), s=48,
                            alpha=a * s, depthshade=False)
    text(fig, .73, .84, "the base  $S^{2}$", 19, INK, a * max(s, .25))
    b = fade(max(0, k - 170), max(1, n - 170), 0.12)
    text(fig, .73, .15, "gauge-invariant.\nthis is what a copy duplicates.", 17, WIGNER, b)
    text(fig, .28, .04, "gauge-private. nothing observable to duplicate.", 17, FRIEND, b)


def _ball(fig, rect, r, azim, show_surface=True):
    """The two-qubit entanglement ball, with the state point at radius r."""
    ax = fig.add_axes(rect, projection="3d")
    bare3d(ax, 1.30)
    ax.view_init(elev=14, azim=azim)
    if show_surface:
        wire(ax, 1.0, DIM, 0.26)
    ax.plot([0], [0], [0], marker="+", color=DIM, ms=9, mew=1.2)
    x = r * np.cos(np.radians(26)); y = r * np.sin(np.radians(26))
    ax.plot([0, x], [0, y], [0, 0], color=DIM, lw=1.2, ls=(0, (3, 3)))
    col = FRIEND if r > 0.92 else (WIGNER if r < 0.999 else FRIEND)
    ax.scatter([x], [y], [0], color=col, s=140, depthshade=False, zorder=10)
    return ax


def sc_plunge(fig, k, n):
    a = fade(k, n, 0.10)
    text(fig, .5, .93, "The measurement is a plunge", 26, ACCENT, a, "bold")
    text(fig, .5, .86, "two qubits:  $S^{3}\\rightarrow S^{7}\\rightarrow S^{4}$,  "
                       "and the base is a ball", 18, DIM, a)
    s = ease((k - 55) / 150)
    r = 1.0 - s                      # surface -> centre
    C = np.sqrt(max(0.0, 1 - r * r))
    _ball(fig, [.30, .16, .40, .62], r, (k * 0.26) % 360)
    text(fig, .5, .115, "$C^{2}+r^{2}=1$", 30, INK, a)
    text(fig, .18, .46, "$r$ = Bloch radius\n%.2f" % r, 19, FRIEND, a)
    text(fig, .82, .46, "$C$ = concurrence\n%.2f" % C, 19, WIGNER, a)
    if r > 0.97:
        text(fig, .5, .045, "the friend's end: pure, on the surface", 18, FRIEND, a)
    elif C > 0.97:
        text(fig, .5, .045, "the centre: maximally entangled", 18, WIGNER, a)
    else:
        text(fig, .5, .045, "the discrepancy in radius is exactly the concurrence", 18, DIM, a)


def sc_charts(fig, k, n):
    a = fade(k, n, 0.10)
    text(fig, .5, .93, "Not rival claims. Two charts on one manifold.", 26, ACCENT, a, "bold")
    az = (k * 0.26) % 360
    _ball(fig, [.05, .26, .40, .56], 1.0, az)
    _ball(fig, [.55, .26, .40, .56], 0.0, az)
    text(fig, .25, .84, "the friend's chart", 22, FRIEND, a, "bold")
    text(fig, .75, .84, "Wigner's chart", 22, WIGNER, a, "bold")
    b = fade(max(0, k - 45), max(1, n - 45), 0.12)
    text(fig, .25, .22, "$r=1$, pure, on the surface\nprivate, phase-carrying", 18, FRIEND, b)
    text(fig, .75, .22, "$r<1$, mixed, in the interior\npublic, record-bearing", 18, WIGNER, b)
    c = fade(max(0, k - 120), max(1, n - 120), 0.14)
    text(fig, .5, .09, "the same state on $S^{7}$. the FANOUT boundary lies between them,", 19, INK, c)
    text(fig, .5, .035, "so a fact exists relative to $F$ and not relative to $W$.", 19, INK, c)


def sc_ladder(fig, k, n):
    a = fade(k, n, 0.10)
    text(fig, .5, .93, "Objectivity is redundancy", 26, ACCENT, a, "bold")
    ax = fig.add_axes([.08, .26, .84, .52]); ax.set_axis_off()
    ax.set_xlim(0, 12); ax.set_ylim(0, 5)
    ax.annotate("", (11.3, 1.0), (0.7, 1.0),
                arrowprops=dict(arrowstyle="-|>", color=DIM, lw=1.8, alpha=a))
    ax.text(0.7, 0.45, "$R=1$", fontsize=18, color=FRIEND, alpha=a)
    ax.text(11.3, 0.45, "$R\\gg 1$", fontsize=18, color=WIGNER, ha="right", alpha=a)
    grown = ease((k - 30) / 190)
    nfrag = int(grown * 26)
    rng = np.linspace(0, 1, 26)
    for i in range(nfrag):
        f = rng[i]
        ax.add_patch(plt.Circle((0.9 + f * 10.2, 2.4 + 0.95 * np.sin(i * 2.1)),
                                0.17, color=plt.cm.cool(1 - f), alpha=0.85 * a))
    ax.text(0.9, 4.45, "one copy:\nthe friend's relative fact,\nreversible by Wigner",
            fontsize=15, color=FRIEND, alpha=a, va="top")
    b = fade(max(0, k - 150), max(1, n - 150), 0.12)
    ax.text(11.3, 4.45, "copied into many fragments:\nno one can practically un-copy it.\n"
                        "operationally, an objective fact",
            fontsize=15, color=WIGNER, alpha=b, va="top", ha="right")
    text(fig, .5, .14, "FANOUT is graded not because the operation is fuzzy,", 19, INK, b)
    text(fig, .5, .08, "but because redundancy $R$ runs continuously. One axis, two ends.", 19, INK, b)


def sc_tsirelson(fig, k, n):
    a = fade(k, n, 0.10)
    text(fig, .5, .93, "And the ball has no point beyond its centre", 26, ACCENT, a, "bold")
    ax = fig.add_axes([.30, .22, .40, .58], projection="3d")
    bare3d(ax, 2.0)
    ax.view_init(elev=14, azim=(k * 0.26) % 360)
    wire(ax, 1.0, DIM, 0.26)
    ax.plot([0], [0], [0], marker="+", color=DIM, ms=10, mew=1.3)
    ax.scatter([0], [0], [0], color=WIGNER, s=130, depthshade=False)
    s = ease((k - 90) / 70)
    if s > 0:
        ax.scatter([-1.55], [0], [0], color=ACCENT, s=130, marker="X",
                   depthshade=False, alpha=a * s)
        ax.plot([0, -1.55], [0, 0], [0, 0], color=ACCENT, lw=1.4,
                ls=(0, (3, 3)), alpha=a * s)
    text(fig, .5, .145, "a PR box needs $C^{2}=3$, so $r^{2}=-2$:", 20, ACCENT,
         fade(max(0, k - 95), max(1, n - 95), 0.12))
    text(fig, .5, .085, "two units past the centre, where the ball does not reach.", 20, ACCENT,
         fade(max(0, k - 110), max(1, n - 110), 0.12))
    text(fig, .5, .025, "the Tsirelson bound is the roundness of the sphere", 18, DIM,
         fade(max(0, k - 140), max(1, n - 140), 0.12))


def sc_close(fig, k, n):
    a = fade(k, n, 0.20)
    text(fig, .5, .60, "one state, two charts,", 32, INK, a)
    text(fig, .5, .50, "and a boundary that is graded, not sharp", 32, FRIEND, a)
    text(fig, .5, .30, "It from Bit via Gödel  ·  Paper 1, § Wigner's friend in the Hopf picture",
         17, DIM, fade(max(0, k - 25), max(1, n - 25), 0.20))


RENDER = {"title": sc_title, "paradox": sc_paradox, "hopf": sc_hopf,
          "plunge": sc_plunge, "charts": sc_charts, "ladder": sc_ladder,
          "tsirelson": sc_tsirelson, "close": sc_close}


def draw(fig, k):
    fig.clear()
    fig.patch.set_facecolor(BG)
    for name, a, b in BOUNDS:
        if a <= k < b:
            RENDER[name](fig, k - a, b - a)
            break
    # progress hairline
    p = k / TOTAL
    fig.add_artist(plt.Line2D([0, p], [0.004, 0.004], color=FRIEND, lw=2.2,
                              alpha=.55, transform=fig.transFigure))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--preview", type=int, default=None,
                    help="render this one frame to media/preview_<n>.png and stop")
    ap.add_argument("--scale", type=float, default=1.0, help="1.0 = 1280x720")
    args = ap.parse_args()

    fig = plt.figure(figsize=(12.8 * args.scale, 7.2 * args.scale), dpi=100)
    fig.patch.set_facecolor(BG)

    if args.preview is not None:
        draw(fig, args.preview)
        p = OUT.parent / ("preview_%04d.png" % args.preview)
        fig.savefig(p, facecolor=BG)
        print("wrote", p.relative_to(ROOT))
        return

    OUT.parent.mkdir(parents=True, exist_ok=True)
    w = FFMpegWriter(fps=FPS, bitrate=4200, codec="libx264",
                     extra_args=["-pix_fmt", "yuv420p", "-preset", "medium"])
    print("frames %d  (%.1f s at %d fps)" % (TOTAL, TOTAL / FPS, FPS))
    with w.saving(fig, str(OUT), dpi=100):
        for k in range(TOTAL):
            draw(fig, k)
            w.grab_frame(facecolor=BG)
            if k % 60 == 0:
                print("  %4d / %d  (%3.0f%%)" % (k, TOTAL, 100 * k / TOTAL), flush=True)
    print("wrote", OUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
