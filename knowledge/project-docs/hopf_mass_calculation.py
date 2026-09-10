import numpy as np

# ===========================================================
# Part 1: Koide formula verification and angle extraction
# ===========================================================

# Measured charged lepton masses (MeV)
m_e = 0.51099895
m_mu = 105.6583755
m_tau = 1776.86

print("=" * 70)
print("PART 1: KOIDE FORMULA AND ANGLE EXTRACTION")
print("=" * 70)

# Verify Koide formula
numerator = m_e + m_mu + m_tau
denominator = (np.sqrt(m_e) + np.sqrt(m_mu) + np.sqrt(m_tau))**2
koide_ratio = numerator / denominator
print(f"\nKoide ratio: {koide_ratio:.8f}")
print(f"Expected:    {2/3:.8f}")
print(f"Deviation:   {abs(koide_ratio - 2/3):.2e}")

# Extract Koide angle delta
# Parametrisation: sqrt(m_i) = M(1 + sqrt(2) cos(delta + 2*pi*i/3))
# where i=0 is tau (heaviest), i=1 is electron (lightest), i=2 is muon
sqrt_masses = np.array([np.sqrt(m_tau), np.sqrt(m_e), np.sqrt(m_mu)])
M = np.sum(sqrt_masses) / 3  # Since cos terms sum to zero

print(f"\nM = {M:.6f} MeV^(1/2)")

# From tau: cos(delta) = (sqrt(m_tau)/M - 1)/sqrt(2)
cos_delta = (sqrt_masses[0]/M - 1) / np.sqrt(2)
delta_measured = np.arccos(cos_delta)

print(f"\nMeasured Koide angle: {delta_measured:.8f} rad")
print(f"2/9 =                {2/9:.8f} rad")
print(f"Deviation:            {abs(delta_measured - 2/9):.2e} rad")
print(f"Relative deviation:   {abs(delta_measured - 2/9)/(2/9)*100:.4f}%")

# ===========================================================
# Part 2: Predictions from delta = 2/9
# ===========================================================

print("\n" + "=" * 70)
print("PART 2: MASS PREDICTIONS FROM delta = 2/9")
print("=" * 70)

delta = 2/9

# Predict sqrt(masses) — need M from one measured mass or from overall scale
# Using M extracted from data (this is the one free dimensional parameter)
sqrt_m_pred = np.array([
    M * (1 + np.sqrt(2) * np.cos(delta)),           # tau
    M * (1 + np.sqrt(2) * np.cos(delta + 2*np.pi/3)), # electron
    M * (1 + np.sqrt(2) * np.cos(delta + 4*np.pi/3))  # muon
])

m_pred = sqrt_m_pred**2
labels = ['tau', 'electron', 'muon']
m_actual = [m_tau, m_e, m_mu]

print(f"\n{'Particle':<12} {'Predicted (MeV)':<18} {'Measured (MeV)':<18} {'Ratio':<10}")
print("-" * 58)
for i in range(3):
    ratio = m_pred[i] / m_actual[i]
    print(f"{labels[i]:<12} {m_pred[i]:<18.6f} {m_actual[i]:<18.6f} {ratio:<10.6f}")

# ===========================================================
# Part 3: Geometric origin of 2/9
# ===========================================================

print("\n" + "=" * 70)
print("PART 3: GEOMETRIC INTERPRETATION OF 2/9")
print("=" * 70)

# Candidate geometric ratios
print("\nCandidate geometric origins:")
print(f"  dim(C)/dim(O+1)  = 2/9 = {2/9:.8f}  ← dim of preferred C / dim of S^8+1")
print(f"  dim(C)/dim(Spin(9) vector) = 2/9")
print(f"  1/(3+1/2)        = 2/7 = {2/7:.8f}  ← not matching")
print(f"  sin^2(theta_W)/2 = {0.25/2:.8f}  ← not matching")

# The relationship between delta_K and the Weinberg angle
theta_W_tree = np.arcsin(np.sqrt(1/4))
print(f"\n  Tree-level Weinberg angle: {theta_W_tree:.6f} rad = {np.degrees(theta_W_tree):.2f} deg")
print(f"  Koide angle:               {2/9:.6f} rad = {np.degrees(2/9):.2f} deg")
print(f"  Ratio theta_W/delta_K:     {theta_W_tree/(2/9):.6f}")
print(f"  pi/2 * (2/9):              {np.pi/2 * 2/9:.6f}")

# ===========================================================
# Part 4: Octonion structure and associator
# ===========================================================

print("\n" + "=" * 70)
print("PART 4: OCTONION ASSOCIATOR COMPUTATION")
print("=" * 70)

# Octonion multiplication table using Baez convention
# Fano plane lines (oriented): (1,2,4), (2,3,5), (3,4,6), (4,5,7), (5,6,1), (6,7,2), (7,1,3)
# e_i * e_j = e_k for (i,j,k) cyclic on a line, -e_k for anti-cyclic

fano_lines = [
    (1,2,4), (2,3,5), (3,4,6), (4,5,7), (5,6,1), (6,7,2), (7,1,3)
]

# Build multiplication table for imaginary units
# mult[i][j] = (sign, index) meaning e_i * e_j = sign * e_index
# For i=j: e_i * e_i = -1 (represented as (−1, 0))
mult = {}
for i in range(1,8):
    for j in range(1,8):
        if i == j:
            mult[(i,j)] = (-1, 0)  # e_i^2 = -1
        else:
            mult[(i,j)] = (0, 0)   # default, will be filled

for line in fano_lines:
    a, b, c = line
    # Cyclic: a*b = c, b*c = a, c*a = b
    mult[(a,b)] = (1, c)
    mult[(b,c)] = (1, a)
    mult[(c,a)] = (1, b)
    # Anti-cyclic: b*a = -c, c*b = -a, a*c = -b
    mult[(b,a)] = (-1, c)
    mult[(c,b)] = (-1, a)
    mult[(a,c)] = (-1, b)

def oct_mult_basis(i, j):
    """Multiply basis elements e_i and e_j. Returns (coefficient, index).
    Index 0 means real part."""
    if i == 0 and j == 0:
        return (1, 0)
    elif i == 0:
        return (1, j)
    elif j == 0:
        return (1, i)
    else:
        return mult[(i,j)]

# Full octonion multiplication
# An octonion is represented as a list of 8 real numbers [a0, a1, ..., a7]
def oct_multiply(a, b):
    """Multiply two octonions represented as 8-component arrays."""
    result = np.zeros(8)
    for i in range(8):
        for j in range(8):
            if abs(a[i]) < 1e-15 or abs(b[j]) < 1e-15:
                continue
            if i == 0 and j == 0:
                result[0] += a[0] * b[0]
            elif i == 0:
                result[j] += a[0] * b[j]
            elif j == 0:
                result[i] += a[i] * b[0]
            else:
                sign, idx = mult[(i,j)]
                result[idx] += sign * a[i] * b[j]
    return result

def associator(a, b, c):
    """Compute [a,b,c] = (ab)c - a(bc)"""
    ab = oct_multiply(a, b)
    bc = oct_multiply(b, c)
    ab_c = oct_multiply(ab, c)
    a_bc = oct_multiply(a, bc)
    return ab_c - a_bc

def oct_norm(a):
    return np.sqrt(np.sum(a**2))

# Compute associator for all triples of distinct basis elements
print("\nAssociator magnitudes for basis element triples:")
print(f"{'Triple':<15} {'|[ei,ej,ek]|':<15} {'On same Fano line?'}")
print("-" * 48)

fano_set = set()
for line in fano_lines:
    fano_set.add(frozenset(line))

# Check a selection of triples
test_triples = [
    (1,2,4), (2,3,5), (3,4,6),  # On Fano lines
    (1,2,3), (1,2,5), (1,3,4),  # Not on Fano lines
    (1,5,7), (2,4,7), (3,5,7),  # Not on Fano lines
]

for triple in test_triples:
    i, j, k = triple
    ei = np.zeros(8); ei[i] = 1
    ej = np.zeros(8); ej[j] = 1
    ek = np.zeros(8); ek[k] = 1
    assoc = associator(ei, ej, ek)
    mag = oct_norm(assoc)
    on_line = frozenset(triple) in fano_set
    print(f"({i},{j},{k})        {mag:<15.4f} {'Yes' if on_line else 'No'}")

# ===========================================================
# Part 5: Holonomy approach via Berry phase on S^8
# ===========================================================

print("\n" + "=" * 70)
print("PART 5: GENERATION MASSES FROM TRIALITY DECOMPOSITION")
print("=" * 70)

# The three generations correspond to three decompositions of S^15
# related by Spin(8) triality. The preferred complex direction e_1
# breaks the triality symmetry.
#
# The three Fano lines through e_1 are:
# Line A: {1,2,4} - contains e_1, e_2, e_4
# Line B: {7,1,3} - contains e_1, e_3, e_7
# Line C: {5,6,1} - contains e_1, e_5, e_6
#
# Each line defines a quaternionic subalgebra.
# The mass of generation g is related to the "associator cost"
# of the corresponding subalgebra interacting with the others.

print("\nThree Fano lines through e_1 (preferred complex direction):")
lines_through_1 = []
for line in fano_lines:
    if 1 in line:
        lines_through_1.append(line)
        print(f"  {line}")

# For each pair of lines, compute the associator between 
# elements from different lines
print("\nCross-line associators (measuring inter-generation mixing):")
for i, line_i in enumerate(lines_through_1):
    for j, line_j in enumerate(lines_through_1):
        if j <= i:
            continue
        # Get the non-e1 elements from each line
        other_i = [x for x in line_i if x != 1]
        other_j = [x for x in line_j if x != 1]
        
        for a in other_i:
            for b in other_j:
                ea = np.zeros(8); ea[a] = 1
                eb = np.zeros(8); eb[b] = 1
                e1 = np.zeros(8); e1[1] = 1
                
                # Associator [e1, ea, eb] - mixing between preferred direction
                # and elements from two different generation lines
                assoc = associator(e1, ea, eb)
                mag = oct_norm(assoc)
                print(f"  [e1, e{a}, e{b}]: magnitude = {mag:.4f}, "
                      f"direction = {assoc[assoc != 0]}")

# ===========================================================
# Part 6: Mass from "octonionic distance" to preferred direction
# ===========================================================

print("\n" + "=" * 70)
print("PART 6: GENERATION MASS FROM OCTONIONIC GEOMETRY")
print("=" * 70)

# Different approach: the mass of generation g is proportional to the
# "octonionic curvature" seen by that generation's quaternionic subalgebra.
#
# For each Fano line L through e_1, consider the quaternionic subalgebra
# H_L = span{1, e_a, e_b, e_c} where {a,b,c} = L.
#
# The "complementary" space is the span of the other 4 imaginary units.
# The interaction between H_L and its complement, mediated by the
# associator, gives the mass.
#
# For generation g with Fano line L_g, define:
# M_g = sum over (i in L_g, j not in L_g) of |[e_1, e_i, e_j]|^2

print("\nGeneration mass from cross-subalgebra associator sums:")
print()

gen_masses_assoc = []
for g, line in enumerate(lines_through_1):
    elements_in = [x for x in line if x != 1]  # non-e1 elements in this line
    elements_out = [x for x in range(2,8) if x not in line]  # elements not in this line (excluding e1)
    
    mass_sq = 0
    details = []
    for i in elements_in:
        for j in elements_out:
            ei = np.zeros(8); ei[i] = 1
            ej = np.zeros(8); ej[j] = 1
            e1 = np.zeros(8); e1[1] = 1
            assoc = associator(e1, ei, ej)
            mag_sq = np.sum(assoc**2)
            mass_sq += mag_sq
            if mag_sq > 0:
                details.append(f"[e1,e{i},e{j}]²={mag_sq:.1f}")
    
    gen_masses_assoc.append(mass_sq)
    print(f"Generation {g+1} (line {line}): M² = {mass_sq:.1f}")
    print(f"  Components: {', '.join(details)}")
    print()

print("Result: All three generation mass-squareds are EQUAL.")
print("The basis-element associator does not distinguish generations.")
print("This means the mass hierarchy must come from a more subtle effect.")

# ===========================================================
# Part 7: Holonomy via curvature integration
# ===========================================================

print("\n" + "=" * 70)
print("PART 7: HOLONOMY VIA AREA ON S^8")
print("=" * 70)

# The three decompositions of S^15 give three different "coordinate patches"
# on S^8. In each patch, the Zitterbewegung loop of a massive fermion
# traces a great circle. But the THREE great circles are not equivalent
# because the round metric on S^8 is not triality-invariant.
#
# Under Spin(8) triality, the three 8-dim representations are:
# 8_v (vector), 8_s (positive spinor), 8_c (negative spinor)
#
# The octonionic Hopf fibration naturally uses 8_v for the base S^8.
# The three decompositions correspond to choosing which of 8_v, 8_s, 8_c
# is the base.
#
# The key: the Spin(7) holonomy of S^7 (the fibre) acts differently
# on 8_v, 8_s, 8_c. Specifically:
# - 8_v decomposes under Spin(7) as 1 + 7
# - 8_s decomposes under Spin(7) as 8 (the spin representation)
# - 8_c decomposes under Spin(7) as 8 (the conjugate spin representation)  
#
# Wait, Spin(7) has:
# - 8_v of Spin(8) -> 1 + 7 under Spin(7)
# - 8_s of Spin(8) -> 8 (spin rep of Spin(7))
# - 8_c of Spin(8) -> 8 (same spin rep, since Spin(7) has no triality)
#
# So the three decompositions are NOT all equivalent under Spin(7):
# one gives 1+7, the other two give 8+8.

print("""
Under Spin(7) (the structure group of the S^7 fibre):
  8_v → 1 ⊕ 7  (vector of Spin(8) decomposes with a singlet)
  8_s → 8       (spinor remains irreducible)
  8_c → 8       (conjugate spinor remains irreducible)

The decomposition using 8_v as base (the "natural" one) sees a 
SINGLET direction on S^8. This singlet is the "north pole" — the
point where the fibre degenerates. The great circles on S^8 that 
pass through or near this singlet have different holonomy than 
those that avoid it.

For the three generations:
  Gen 1 (8_v base): loop passes through the singlet — MINIMAL holonomy
  Gen 2 (8_s base): loop avoids singlet — INTERMEDIATE holonomy  
  Gen 3 (8_c base): loop avoids singlet — MAXIMAL holonomy

The distinction between Gen 2 and Gen 3 comes from the preferred
complex direction breaking the 8_s ↔ 8_c symmetry.
""")

# The holonomy of a loop on S^n that encloses area A is related to
# the curvature. For the round S^8 of radius R, the sectional 
# curvature is K = 1/R^2, and the holonomy of a small loop enclosing
# area A is proportional to K*A = A/R^2.
#
# For the octonionic Hopf fibration with total space S^15 of unit radius,
# the base S^8 has the Fubini-Study metric with curvature varying
# between 1 and 4 (for the complex and quaternionic cases; the 
# octonionic case is more subtle due to non-associativity).

# The Berry phase for a loop at latitude theta on S^2 enclosing
# solid angle Omega = 2*pi*(1-cos(theta)) is phi = Omega/2.
# 
# For the quaternionic Hopf fibration S^3 → S^7 → S^4, the analogous
# phase is an SU(2) holonomy.
#
# For the octonionic case, let's compute the holonomy for loops
# at different "latitudes" on S^8, corresponding to different amounts
# of the singlet direction.

# The octonionic Hopf fibration has base S^8 with coordinates
# that can be written in terms of the octonionic projective line OP^1.
# A point on S^8 is specified by a unit imaginary octonion plus a
# real parameter. 
#
# The "north pole" is the singlet direction (pure real, e_0 direction).
# A loop at "colatitude" theta on S^8 encloses a region with area
# proportional to the volume of a 7-cap of angular radius theta.

# Volume of spherical cap on S^n of angular radius theta:
def sphere_cap_volume(n, theta):
    """Volume of cap on unit S^n of angular radius theta."""
    from scipy import integrate
    def integrand(t):
        return np.sin(t)**((n-1)) if n > 1 else 1
    vol, _ = integrate.quad(integrand, 0, theta)
    return vol

# Total volume of S^n
def sphere_volume(n):
    return sphere_cap_volume(n, np.pi)

# For S^8:
print("Spherical cap areas on S^8:")
print(f"  Total S^8 volume: {sphere_volume(8):.6f}")
print(f"  (Normalised to 1)\n")

total_vol = sphere_volume(8)

# Three canonical latitudes for three generations
# Gen 1: near the singlet (north pole) — small loop
# Gen 2: intermediate latitude
# Gen 3: near the equator — large loop
#
# The three latitudes should be related by the triality angle 2*pi/3
# projected onto the colatitude of S^8.
#
# In the Koide parametrisation, the three phases are 
# delta, delta + 2*pi/3, delta + 4*pi/3
# These map to colatitudes on S^8 via some function.
#
# The simplest mapping: the Zitterbewegung frequency is proportional
# to the holonomy, which is proportional to the enclosed area.

# Attempt: mass proportional to enclosed solid angle on S^8
# For a great circle at colatitude theta, the enclosed area is
# the cap area up to theta.

# Map the Koide angles to colatitudes
# theta_g = pi/2 * (1 + sqrt(2) * cos(delta + 2*pi*g/3)) 
# normalised so theta ranges from 0 to pi

# Actually, let's try the simplest hypothesis:
# mass_g ∝ (holonomy of loop_g)^2
# holonomy_g ∝ cap_volume(S^8, theta_g) 
# where theta_g encodes the generation

# If the three loops are related by triality (2pi/3 rotations)
# and the preferred complex direction breaks the symmetry by angle delta,
# then the colatitudes are:
# theta_g = arccos(cos(delta + 2*pi*g/3) / max_cos)

# Let me try a direct approach: compute what holonomy ratios
# would give the correct mass ratios.

print("=" * 70)
print("PART 8: REQUIRED HOLONOMY RATIOS vs MEASURED MASS RATIOS")
print("=" * 70)

print(f"\nCharged lepton mass ratios (normalised to tau):")
print(f"  m_e/m_tau  = {m_e/m_tau:.8f}")
print(f"  m_mu/m_tau = {m_mu/m_tau:.8f}")
print(f"  m_tau/m_tau = 1")

print(f"\nSquare root ratios (if mass ∝ holonomy²):")
print(f"  sqrt(m_e/m_tau)  = {np.sqrt(m_e/m_tau):.8f}")
print(f"  sqrt(m_mu/m_tau) = {np.sqrt(m_mu/m_tau):.8f}")

print(f"\nKoide parametrisation with delta = 2/9:")
delta = 2/9
for g, name in enumerate(['tau (g=0)', 'electron (g=1)', 'muon (g=2)']):
    phase = delta + 2*np.pi*g/3
    sqrt_ratio = (1 + np.sqrt(2)*np.cos(phase)) / (1 + np.sqrt(2)*np.cos(delta))
    print(f"  {name}: sqrt(m_g/m_tau) = {sqrt_ratio:.8f}")

# ===========================================================
# Part 9: Extending to quarks via GHZ contextuality
# ===========================================================

print("\n" + "=" * 70)
print("PART 9: QUARK MASSES FROM GHZ CONTEXTUALITY")
print("=" * 70)

# For quarks, the Koide formula should be modified because 
# GHZ entanglement extraction is contextual.
# The contextuality introduces the Cabibbo angle as an additional
# phase shift.
#
# Hypothesis: for quarks, the Koide angle is shifted by theta_C
# delta_quark = 2/9 + theta_C
# where sin(theta_C) = 1/4 (our tree-level prediction)

theta_C = np.arcsin(1/4)
delta_quark = 2/9 + theta_C  # shifted Koide angle for quarks

print(f"\nCabibbo angle (tree level): {theta_C:.6f} rad = {np.degrees(theta_C):.2f} deg")
print(f"Quark Koide angle: delta_q = 2/9 + theta_C = {delta_quark:.6f} rad")

# Apply Koide formula to up-type quarks (u, c, t)
m_u = 2.16  # MeV (MS-bar at 2 GeV)
m_c = 1270  # MeV
m_t = 172760  # MeV (pole mass)

print(f"\nUp-type quark masses:")
print(f"  m_u = {m_u} MeV, m_c = {m_c} MeV, m_t = {m_t} MeV")

# Check Koide ratio for up-type quarks
koide_up = (m_u + m_c + m_t) / (np.sqrt(m_u) + np.sqrt(m_c) + np.sqrt(m_t))**2
print(f"  Koide ratio: {koide_up:.6f} (cf 2/3 = {2/3:.6f})")

# Extract the effective Koide angle
sqrt_m_up = np.array([np.sqrt(m_t), np.sqrt(m_u), np.sqrt(m_c)])
M_up = np.sum(sqrt_m_up) / 3
cos_delta_up = (sqrt_m_up[0]/M_up - 1) / np.sqrt(2)
if abs(cos_delta_up) <= 1:
    delta_up_measured = np.arccos(cos_delta_up)
    print(f"  Measured Koide angle: {delta_up_measured:.6f} rad")
    print(f"  Predicted (2/9 + theta_C): {delta_quark:.6f} rad")
    print(f"  Deviation: {abs(delta_up_measured - delta_quark):.4f} rad")

# Down-type quarks
m_d = 4.67  # MeV
m_s = 93.4  # MeV
m_b = 4180  # MeV

print(f"\nDown-type quark masses:")
print(f"  m_d = {m_d} MeV, m_s = {m_s} MeV, m_b = {m_b} MeV")

koide_down = (m_d + m_s + m_b) / (np.sqrt(m_d) + np.sqrt(m_s) + np.sqrt(m_b))**2
print(f"  Koide ratio: {koide_down:.6f} (cf 2/3 = {2/3:.6f})")

sqrt_m_down = np.array([np.sqrt(m_b), np.sqrt(m_d), np.sqrt(m_s)])
M_down = np.sum(sqrt_m_down) / 3
cos_delta_down = (sqrt_m_down[0]/M_down - 1) / np.sqrt(2)
if abs(cos_delta_down) <= 1:
    delta_down_measured = np.arccos(cos_delta_down)
    print(f"  Measured Koide angle: {delta_down_measured:.6f} rad")
    print(f"  Predicted (2/9 + theta_C): {delta_quark:.6f} rad")
    print(f"  Deviation: {abs(delta_down_measured - delta_quark):.4f} rad")

# ===========================================================
# Part 10: Summary comparison with alternative angles
# ===========================================================

print("\n" + "=" * 70)
print("PART 10: SUMMARY OF ALL KOIDE ANGLES")
print("=" * 70)

# Also try delta_quark = 2/9 + sin^2(theta_W) * pi/2 and other combos
# Or delta_quark = 2/9 * (1 + some correction)

# Let's also try the "sqrt(2) * alpha" approach, where the quark angle
# picks up a factor from the strong coupling

print(f"\nComparison of Koide angles:")
print(f"  {'Sector':<25} {'Measured':<12} {'2/9':<12} {'2/9+θ_C':<12}")
print(f"  {'Charged leptons':<25} {delta_measured:<12.6f} {2/9:<12.6f} {'—':<12}")
if abs(cos_delta_up) <= 1:
    print(f"  {'Up-type quarks':<25} {delta_up_measured:<12.6f} {2/9:<12.6f} {delta_quark:<12.6f}")
if abs(cos_delta_down) <= 1:
    print(f"  {'Down-type quarks':<25} {delta_down_measured:<12.6f} {2/9:<12.6f} {delta_quark:<12.6f}")

# Neutrino masses (from oscillation data)
print(f"\nNeutrino sector (using squared mass differences):")
print(f"  Δm²₂₁ = 7.53e-5 eV² (solar)")
print(f"  Δm²₃₁ = 2.453e-3 eV² (atmospheric, normal ordering)")

# For neutrinos with Koide delta = 2/9 and alpha = sqrt(2)
# (our earlier prediction), need to handle differently since
# absolute masses unknown. Using our prediction sum = 2.6 meV:
m_nu_sum = 0.0026  # eV, our prediction
dm21_sq = 7.53e-5  # eV^2
dm31_sq = 2.453e-3  # eV^2

# If Koide holds for neutrinos with delta = 2/9:
# Try to find consistent set
print(f"\n  If Koide with delta=2/9 and sum m_nu = 2.6 meV:")
# M_nu = sum(sqrt(m_i))/3
# We need to solve for the three masses
# This requires numerical solution given the constraints
# m1 + m2 + m3 = 0.0026
# m2^2 - m1^2 = 7.53e-5
# m3^2 - m1^2 = 2.453e-3

# These are overdetermined with Koide as additional constraint
# Just report the prediction for now
print(f"  (Detailed neutrino mass prediction deferred - requires")
print(f"   joint solution of Koide + oscillation constraints)")

print("\n" + "=" * 70)
print("CONCLUSIONS")
print("=" * 70)
print(f"""
1. The Koide angle for charged leptons is δ = 2/9 to 5 significant
   figures. This reproduces all three charged lepton masses from a 
   single geometric parameter with zero free dimensionless parameters
   (M is the one free dimensional parameter).

2. 2/9 = dim(ℂ)/dim(S⁸+point) has a natural octonionic interpretation
   as the ratio of the preferred complex direction's dimension to the 
   total dimension of the octonionic projective line OP¹ = S⁸ ∪ {{∞}}.

3. The basis-element associator has uniform magnitude (= 2) for all 
   non-Fano-line triples. The mass hierarchy therefore does NOT come 
   from associator magnitudes between basis elements, but from the 
   Koide angle breaking the triality symmetry. The associator's role 
   is to make the three bracketings INEQUIVALENT (giving different 
   masses), while the Koide angle determines HOW inequivalent.

4. For quarks, the Koide ratio deviates from 2/3, indicating that 
   the simple Koide formula needs modification. The GHZ contextuality 
   argument suggests a shift by the Cabibbo angle, but the numerical 
   match requires further work.

5. The key open calculation: derive δ = 2/9 from the holonomy of the 
   octonionic Hopf connection. This would close the loop between the 
   entanglement transfer dynamics and the fermion mass spectrum.
""")

