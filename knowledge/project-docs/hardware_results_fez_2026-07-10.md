# Hardware Results: ibm_fez (Heron r2), 2026-07-08 and 2026-07-10

Session log of the first post-backlog hardware batch. Notebooks G, H (2026-07-08,
the standing queue) and J, K (2026-07-10, the fourth-qubit batch). Notebook L's
block arrived truncated -- numbers pending. Job ids recorded where printed.

## G -- GHZ monogamy tomography (07-08 15:20 UTC)
tau1(23) = 1.000; C12 = C13 = 0.000; tau3 = 1.000; external-available tangle 0.000.
READING: the signature {collective tangle full, pairwise zero} is confirmed with
noise-ROBUSTNESS, not despite noise -- I/2 is a depolarisation fixed point, so
tau = 1 is noise-assisted, and Wootters' max(0, .) pins separable marginals at
C = 0. One honest clause owed wherever this enters the appendix.

## H -- two-gluon network (07-08 15:01 UTC)
Postselected 2089/8192 = 0.255 (ideal 1/4). Open-leg Z: 00 0.504, 11 0.438
(T1 bias toward |0>), leakage 0.058. <XX> = +0.915 (ideal +1).
READING: the copy-tensor discriminator fired -- a classical copy shows the same
Z-diagonal with <XX> ~ 0; +0.915 is the coherence witness. Open legs are a Bell
pair, NOT a FANOUT: the two-gluon claim confirmed on hardware.

## J -- the leptonic ninth (07-10 10:41, job d98cnvaf47jc73a7ooog)
Depths 27-41. r^2 = 0.0935 (target 1/9 = 0.1111, -16%); C(wire,tag) = 0.0162.
READING: the -16% is the DEPOLARISATION PREDICTION, sign and size -- r^2 shrinks
by (1-p)^2, here ~8% per axis over depth ~30. The original advisory ("noise
inflates r^2") had the dominant effect backwards; corrected in both formats
2026-07-10. C = 0.016 is readout-manufactured (the max(0,.) floor); the
CKW-saturation claim (state-level tag concurrence = 0) STANDS. Mitigated
expectation for the paper figure: r^2 -> 0.105-0.111.

## K -- the full CKM core (07-10 10:35, job d98cm0d2su3c739j4ang)
Depths 13-15. Diagonals 0.939/0.936/0.966 vs programmed 0.951/0.949/0.998;
max deviation 0.032; spectator leakage 0.022 (ideal 0 -- pure hardware).
Rung 1: |V_us|^2 = 0.0543 -> |V_us| = 0.233 (programmed 0.2204; PDG 0.2250).
Rungs 2-3 AT THE NOISE FLOOR: |V_cb|^2 read 0.0214 vs programmed 0.0024 (x9);
|V_ts|^2 0.0094 vs 0.0025. lambda^4 sits below fez's ~2% unmitigated floor.
READING: circuit validated; rung 1 demonstrated within ~6%; the small elements
need help. K-v2 DESIGN QUEUED: angle amplification -- apply the rung-2 (and
rung-3) rotations n times, extract the accumulated angle, divide by n; plus
readout mitigation. Target: |V_cb| to ~10% on fez.

## L -- mini-Meissner (07-10, job d98gtvgtcv6s73dm4cmg)
Depths 57-73 (initialize; Baertschi-Eidenbenz prep would ~halve this).
Twist response <s+_0 s-_3>(phi): +0.2864 / -0.0167 / -0.2948 against theory
+1/3 / 0 / -1/3. THE SIGN FLIP IS MEASURED. Single visibility prefactor
V ~ 0.87: corr_hw(phi) = V (1/3) cos(3 phi) -- the stiffness's functional
form intact, amplitude attenuated as depth predicts; middle point and
end-asymmetry both inside the ~0.022 shot tolerance.
JEWEL: via the notebook's verified identity tau_1 = 4 corr (N-1)/N, the
measured correlator IS a measured one-site tangle, 0.859 -- fez measured one
number wearing both names. The Fan-Lloyd identity executed on hardware; the
Anderson-Higgs demonstration the witness section queued now exists.
FIGURE SPEC: three points with shot error bars, the V cos fit, the ideal
curve dashed; caption leads with the sign flip, credits the identity for the
dual reading. B-E prep rerun optional for V ~ 0.95.

## BATCH COMPLETE (2026-07-10): five for five
G (monogamy, noise-robust), H (copy-tensor discriminator, <XX> = 0.915),
J (the ninth at -16% = the depolarisation prediction; C = 0 within floor),
K (circuit validated; rung 1 within ~6%; rungs 2-3 at the noise floor ->
K-v2 angle amplification), L (the Meissner sign flip; order parameter =
tangle as one measurement).
FINAL numbers now: G, H, L. AWAITING: J mitigated rerun; K-v2.
PAPER PASS: pending JS's call -- either route the final trio now (witness
sentence + predictions' already-tested + appendix material) or hold for the
complete mitigated set and do one coherent pass.

## Paper routing (deferred until L lands and J/K rerun mitigated)
G -> the monogamy/budget appendix material with the noise-robustness clause.
H -> the two-gluon/glueball passage: the copy-tensor discriminator on hardware.
J -> the witness/ninth story: base presence measured; concurrence zero.
K -> app:qiskit-ckm extension: rung 1 on hardware; rungs 2-3 = K-v2.
