#!/usr/bin/env python3
"""b_anomaly_lepton_universality_2026-11-07T1900.py

What the framework says about the B-meson "anomalies" of Alda, Guasch and
Penaranda (arXiv:2105.05095, LCWS2021 proceedings): R_K, R_K* (b -> s l l)
and R_D, R_D* (b -> c tau nu). Three parts, pure numpy, fixed seed.

  A. Lepton universality in the register model. The gauge gates of the
     vertex dictionary act on the gauge qubits tensored with the identity
     on the generation label (prop:fcnc, prop:neutral-blind). A toy of the
     b -> s l l process -- a quark register with a CKM-rotated charged
     gate and a neutral gate, a lepton register with neutral gates only --
     gives a rate independent of the lepton generation for every random
     gate word, including loop-like sums of words. Then the Lean-checked
     identity V^dag (c 1) V = c 1 against a generation-dependent coupling
     D = diag(C^e, C^mu, C^tau) taken from the paper's Scenario VII fit:
     non-universality produces lepton-flavour-violating off-diagonals
     under a generic basis rotation (Glashow, Guadagnoli and Lane 2015),
     universality never does.
  B. The data against R = 1, which is the framework's prediction (the
     same as the Standard Model's at the gauge level): LHCb 2021 R_K and
     LHCb 2022 R_K, R_K* in two q^2 bins; HFLAV 2023 R(D), R(D*) with
     their correlation. Asymmetric errors symmetrised by the larger side;
     a theory uncertainty of 0.01 on R = 1 (Bordone, Isidori and Pattori
     2016). Numbers as quoted in the sources named in the session note.
  C. The paper's lepton-flavoured fit decomposed into the part the
     framework can carry (the S_3-invariant, generation-blind part) and
     the part it cannot (the traceless part).

Convention A is not needed here (no octonions). Seed 20261107.
"""
import numpy as np

rng = np.random.default_rng(20261107)
FAILS = []


def check(name, ok, detail=""):
    tag = "PASS" if ok else "FAIL"
    if not ok:
        FAILS.append(name)
    print(f"  [{tag}] {name}" + (f"  ({detail})" if detail else ""))


def haar_unitary(n):
    z = (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))) / np.sqrt(2)
    q, r = np.linalg.qr(z)
    return q * (np.diag(r) / np.abs(np.diag(r)))


# ---------------------------------------------------------------------------
print("=== Part A: lepton universality is the identity on the generation label ===")
# Registers: quark gauge space (dim 2: the B qubit, weak isospin) x quark generation (3)
#            lepton gauge space (dim 2) x lepton generation (3)
I2, I3 = np.eye(2), np.eye(3)
raise_op = np.array([[0, 0], [1, 0]], dtype=complex)        # T_3 raise on the B qubit
V_ckm = haar_unitary(3)                                     # a generic unitary stands in for the CKM rotation


def kron(*ms):
    out = np.array([[1.0 + 0j]])
    for m in ms:
        out = np.kron(out, m)
    return out


def charged_gate_quark():
    """T_3 raise (x) CKM on the quark register, identity on the lepton register."""
    return kron(raise_op, V_ckm, I2, I3)


def neutral_gate(which):
    """A random gauge gate on the gauge qubit of one register, identity on both generation labels."""
    g = haar_unitary(2)
    return kron(g, I3, I2, I3) if which == "quark" else kron(I2, I3, g, I3)


def random_word(n_gates):
    """A random product of charged (quark) and neutral (quark or lepton) gates."""
    W = np.eye(36, dtype=complex)
    for _ in range(n_gates):
        kind = rng.choice(["charged", "nq", "nl"])
        G = charged_gate_quark() if kind == "charged" else neutral_gate("quark" if kind == "nq" else "lepton")
        W = G @ W
    return W


def rate_by_lepton(W, quark_in, quark_gen_in, quark_gen_out):
    """Sum over all final gauge states of |<q_out, s ; gauge, l | W | q_in, b ; gauge_in, l>|^2 for each lepton generation l.
    The lepton generation is the same in and out (no lepton flavour change): this is the b -> s l+ l- toy."""
    rates = []
    for l in range(3):
        total = 0.0
        for gq_in in range(2):
            for gl_in in range(2):
                psi = np.zeros(36, dtype=complex)
                psi[np.ravel_multi_index((gq_in, quark_gen_in, gl_in, l), (2, 3, 2, 3))] = 1.0
                out = W @ psi
                # project onto quark generation quark_gen_out and lepton generation l, any gauge state
                out = out.reshape(2, 3, 2, 3)
                total += np.sum(np.abs(out[:, quark_gen_out, :, l]) ** 2)
        rates.append(total)
    return np.array(rates)


b, s = 2, 1
max_spread = 0.0
for trial in range(200):
    W = random_word(int(rng.integers(2, 9)))
    if trial % 3 == 0:                                  # loop-like: a sum of two words (interference), renormalised
        W = (W + random_word(int(rng.integers(2, 9)))) / 2
    r = rate_by_lepton(W, None, b, s)
    if r.max() > 1e-12:
        max_spread = max(max_spread, (r.max() - r.min()) / r.max())
check("b -> s l l toy: rate independent of lepton generation for 200 random gate words (incl. 67 two-word sums)",
      max_spread < 1e-12, f"max relative spread {max_spread:.1e}")

# What it takes to move R_K off 1: a coupling that sees the lepton label AND interferes with the universal path.
D_alda = np.diag([-0.25, 0.211, -0.3])                     # Scenario VII central values, C_lq^e, C_lq^mu, C_lq^tau (Alda et al. Table 1)
W_sm = neutral_gate("lepton") @ charged_gate_quark() @ neutral_gate("quark")
# (i) a label-diagonal unitary phase, alone: rates unchanged, the label is a classical tag here
G_phase = kron(I2, I3, I2, np.diag(np.exp(1j * np.diag(D_alda))))
r_phase = rate_by_lepton(G_phase @ W_sm, None, b, s)
check("a generation-dependent phase gate alone leaves every rate unchanged (no second path to interfere with)",
      (r_phase.max() - r_phase.min()) / r_phase.max() < 1e-12, f"spread {(r_phase.max()-r_phase.min())/r_phase.max():.1e}")
# (ii) a generation-dependent amplitude added to the universal one, A_l = A_SM (1 + C^l): the Wilson-coefficient toy
W_np = W_sm + kron(I2, I3, I2, D_alda) @ W_sm
r_np = rate_by_lepton(W_np, None, b, s)
ratio_mu_e = r_np[1] / r_np[0]
expected = abs(1 + D_alda[1, 1]) ** 2 / abs(1 + D_alda[0, 0]) ** 2
print(f"  universal amplitude plus a label-dependent one: rates {np.round(r_np, 4)}, R_(mu/e) = {ratio_mu_e:.4f} = |1 + C^mu|^2 / |1 + C^e|^2 = {expected:.4f}")
check("toy R_K moves off 1 exactly by the interference of a generation-dependent amplitude", abs(ratio_mu_e - expected) < 1e-12)
print("  -> R_K != 1 needs an amplitude that acts on the generation label; the dictionary's gates all act as the identity there")
print("     (prop:fcnc, prop:neutral-blind), so the framework predicts R_K = R_K* = 1 at the gauge level, with only lepton masses to break it")

# The Lean identity and its failure for non-universal couplings
c = rng.normal()
worst_univ, offdiag_nonuniv = 0.0, []
for _ in range(2000):
    V = haar_unitary(3)
    M = V.conj().T @ (c * I3) @ V
    worst_univ = max(worst_univ, np.max(np.abs(M - c * I3)))
    N = V.conj().T @ D_alda @ V
    offdiag_nonuniv.append(abs(N[0, 1]))                 # the e-mu entry: a mu -> e (B -> K mu e) coupling
offdiag_nonuniv = np.array(offdiag_nonuniv)
check("V^dag (c 1) V = c 1 for 2000 Haar-random V (prop:fcnc)", worst_univ < 1e-13, f"max deviation {worst_univ:.1e}")
print(f"  V^dag D V for D = diag(-0.25, 0.211, -0.3): |e-mu entry| median {np.median(offdiag_nonuniv):.4f}, "
      f"90th percentile {np.percentile(offdiag_nonuniv, 90):.4f}, max {offdiag_nonuniv.max():.4f}; zero only on the aligned set")
print(f"  (the maximum possible |e-mu| entry is (max D - min D)/2 = {(D_alda.max()-D_alda.min())/2:.4f})")

# ---------------------------------------------------------------------------
print()
print("=== Part B: the data against R = 1 (framework = SM at the gauge level) ===")
TH = 0.01                                                 # theory uncertainty on R = 1 in the SM (Bordone, Isidori, Pattori 2016)


def pull(val, err_lo, err_hi, sys_lo, sys_hi, sm=1.0, th=TH):
    """Pull of a measurement from sm, symmetrising asymmetric errors by the larger side, theory error in quadrature."""
    stat = max(err_lo, err_hi)
    syst = max(sys_lo, sys_hi)
    sig = np.sqrt(stat ** 2 + syst ** 2 + th ** 2)
    return (val - sm) / sig, sig


print("  LHCb 2021 (Nature Physics 18, 277), R_K central bin 1.1 < q^2 < 6 GeV^2:")
p, sig = pull(0.846, 0.039, 0.042, 0.012, 0.013)
print(f"    R_K = 0.846 +0.042/-0.039 +0.013/-0.012  -> pull from 1: {p:+.2f} sigma (sigma_tot {sig:.3f}; LHCb quote 3.1 sigma with their likelihood)")

print("  LHCb 2022/2023 (PRL 131, 051803; PRD 108, 032002), four bins:")
data_2022 = [
    ("R_K   low     0.1 < q^2 < 1.1", 0.994, 0.082, 0.090, 0.027, 0.029),
    ("R_K*  low     0.1 < q^2 < 1.1", 0.927, 0.087, 0.093, 0.035, 0.036),
    ("R_K   central 1.1 < q^2 < 6.0", 0.949, 0.041, 0.042, 0.022, 0.022),
    ("R_K*  central 1.1 < q^2 < 6.0", 1.027, 0.068, 0.072, 0.026, 0.027),
]
chi2 = 0.0
for name, val, lo, hi, slo, shi in data_2022:
    p, sig = pull(val, lo, hi, slo, shi)
    chi2 += p ** 2
    print(f"    {name}: {val:.3f}  -> pull {p:+.2f} sigma")
from math import exp
p_value = exp(-chi2 / 2) * (1 + chi2 / 2)                 # chi^2 survival function for 4 dof
print(f"    chi^2 against R = 1 over four bins: {chi2:.2f} for 4 dof, p = {p_value:.2f}")
check("LHCb 2022 four bins consistent with R = 1 (p > 0.05)", p_value > 0.05, f"p = {p_value:.2f}")
# the low R_K* bin's SM expectation is about 0.98 (LHCb PRD); the shift is immaterial
p_alt, _ = pull(0.927, 0.087, 0.093, 0.035, 0.036, sm=0.98)
print(f"    (R_K* low bin against the SM's 0.98 instead of 1: pull {p_alt:+.2f} sigma)")

print("  HFLAV 2023 averages (arXiv:2411.18639v2, Fig. in sec. 6.6): R(D) = 0.342 +/- 0.026, R(D*) = 0.287 +/- 0.012, rho = -0.39;")
print("    SM: R(D) = 0.298 +/- 0.004, R(D*) = 0.254 +/- 0.005 (HFLAV's own SM averages)")
delta = np.array([0.342 - 0.298, 0.287 - 0.254])
s1, s2 = np.hypot(0.026, 0.004), np.hypot(0.012, 0.005)
rho = -0.39
C = np.array([[s1 ** 2, rho * s1 * s2], [rho * s1 * s2, s2 ** 2]])
chi2_rd = float(delta @ np.linalg.solve(C, delta))
p_rd = exp(-chi2_rd / 2)                                   # 2 dof
# equivalent two-sided Gaussian sigma
from math import sqrt, erfc
def sigma_from_p(pv, lo=0.0, hi=10.0):
    for _ in range(100):
        mid = (lo + hi) / 2
        if erfc(mid / sqrt(2)) > pv:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2
print(f"    chi^2 = {chi2_rd:.1f} for 2 dof, p = {p_rd:.1e}, i.e. {sigma_from_p(p_rd):.1f} sigma with the experimental correlation only "
      f"(HFLAV quotes 3.1 sigma with the SM correlation included)")
print(f"    individual pulls: R(D) {delta[0]/s1:+.2f} sigma, R(D*) {delta[1]/s2:+.2f} sigma")
print("    LHCb 2023 alone (PRL 131, 111802): R(D*) = 0.281 +/- 0.018 +/- 0.024, R(D0) = 0.441 +/- 0.060 +/- 0.066, 1.9 sigma combined (their statement)")
print("    Belle II 2024 (arXiv:2401.02840): R(D*) = 0.262 +0.041/-0.039 +0.035/-0.032, consistent with the SM (their statement)")
check("R(D), R(D*) tension with R = SM is above 3 sigma on HFLAV 2023 numbers (the framework predicts none: open falsifier)",
      sigma_from_p(p_rd) > 3.0, f"{sigma_from_p(p_rd):.1f} sigma")

# ---------------------------------------------------------------------------
print()
print("=== Part C: the paper's fit decomposed into what the framework can and cannot carry ===")
for label, vec in [("Scenario IV (e, mu)", np.array([-0.25, 0.24, 0.0])),
                   ("Scenario VII (e, mu, tau)", np.array([-0.25, 0.211, -0.3]))]:
    univ = vec.mean()
    traceless = vec - univ
    print(f"  {label}: C_lq = {vec}")
    print(f"    S_3-invariant (generation-blind) part: {univ:+.3f} x (1,1,1)   -- the only shape a dictionary gate can have")
    print(f"    traceless (LFU-violating) part: {np.round(traceless, 3)}, norm {np.linalg.norm(traceless):.3f} "
          f"vs invariant norm {abs(univ)*np.sqrt(3):.3f}")
print("  The paper's own LFU scenario VIII (C^e = C^mu = C^tau) has pull 0.55 sigma from the SM; its IX (e = -mu = tau) has 5.54 sigma:")
print("  the 2021 anomaly lived entirely in the traceless part, which is the part no gate of the dictionary can produce.")
print("  Post-2022: Alguero et al. 2023 find the LFUV fits at 1.2-1.5 sigma and a universal C9 shift of about -1.2 at 4.6-5.8 sigma;")
print("  Ciuchini et al. 2023 find the same data consistent with the SM once charm-loop rescattering is fitted (C9^NP,mu 95% HPDI [-1.06, 1.01]).")
print("  A universal C9 shift is generation-blind and so is not forbidden by prop:fcnc; but as new physics it would need a new neutral")
print("  mediator, which rem:no-fifth-force excludes, so within the framework it can only be Standard-Model dynamics (the charm loop).")

print()
print("B ANOMALY LEPTON UNIVERSALITY: " + ("PASS" if not FAILS else "FAIL " + ", ".join(FAILS)))
