"""Exact counterchecks for the independent reading; no randomness or hidden state.

Octonion multiplication uses Cayley--Dickson Convention A, as in the paper.
These checks test specific implications, not the entire physical programme.
"""

from fractions import Fraction as F


def conjugate(x):
    return [x[0]] + [-v for v in x[1:]]


def multiply(x, y):
    if len(x) == 1:
        return [x[0] * y[0]]
    half = len(x) // 2
    a, b = x[:half], x[half:]
    c, d = y[:half], y[half:]
    ac, db = multiply(a, c), multiply(conjugate(d), b)
    da, bc = multiply(d, a), multiply(b, conjugate(c))
    return [u - v for u, v in zip(ac, db)] + [u + v for u, v in zip(da, bc)]


def basis(k):
    return [int(i == k) for i in range(8)]


def reduced_density(state, keep, n):
    """Sparse unnormalised real amplitudes; normalise exactly on tracing."""
    norm = sum(v * v for v in state.values())
    result = [[F(0) for _ in range(2 ** len(keep))] for _ in range(2 ** len(keep))]
    traced = [k for k in range(n) if k not in keep]
    for a, va in state.items():
        for b, vb in state.items():
            if any(a[k] != b[k] for k in traced):
                continue
            ia = sum(a[k] << (len(keep) - 1 - j) for j, k in enumerate(keep))
            ib = sum(b[k] << (len(keep) - 1 - j) for j, k in enumerate(keep))
            result[ia][ib] += F(va * vb, norm)
    return result


print('Independent review counterchecks: exact arithmetic, Convention A, no randomness')

# The stated toggle is a swap; the proposed pair is not its fixed point.
lamp = (complex(0.5, 0.5), complex(0.5, -0.5))
assert lamp[::-1] != lamp
print('Lamp: swap((1+i)/2, (1-i)/2) differs from the proposed vector; residual = (-i, +i).')

# p0=3x^2-2x^3, p1=1-p0 is a polynomial, positive, phase-blind rule.
x = F(1, 4)
p0 = 3 * x * x - 2 * x * x * x
p1 = 3 * (1 - x) ** 2 - 2 * (1 - x) ** 3
assert p0 + p1 == 1 and p0 != x
print(f'Born countermodel: x={x}; p0=3x^2-2x^3={p0}; p1={p1}; sum={p0+p1}.')

# The appendix embedding uses J=L_e1, so global i acts on both octonions.
for i, j, k in [(1, 2, 3), (1, 4, 5), (1, 7, 6), (2, 4, 6), (2, 5, 7), (3, 4, 7), (3, 6, 5)]:
    assert multiply(basis(i), basis(j)) == basis(k)
o1, o2 = basis(0), basis(6)
before = multiply(o1, conjugate(o2))
after = multiply(multiply(basis(1), o1), conjugate(multiply(basis(1), o2)))
assert before == [-v for v in basis(6)] and after == basis(6)
print('GHZ Hopf image H=2*o1*conj(o2), normalised: H(GHZ)=-e6; H(i*GHZ)=+e6.')
print('The specified full Hopf map does not descend to complex rays; the C-fraction remains zero.')

ghz4 = {(0, 0, 0, 0): 1, (1, 1, 1, 1): 1}
tangles = []
for k in range(4):
    rho = reduced_density(ghz4, [k], 4)
    tangles.append(4 * (rho[0][0] * rho[1][1] - rho[0][1] * rho[1][0]))
assert tangles == [F(1)] * 4
print('GHZ4 one-to-rest tangles: ' + ', '.join(str(t) for t in tangles) + '; all maximal.')

# A pure W state has only product extensions with an exterior.
w = {(0, 0, 1): 1, (0, 1, 0): 1, (1, 0, 0): 1}
w_plus = {bits + (outside,): value for bits, value in w.items() for outside in (0, 1)}
pair = reduced_density(w_plus, [0, 3], 4)
rho_a = reduced_density(w, [0], 3)
assert pair == [[rho_a[a // 2][b // 2] * F(1, 2) for b in range(4)] for a in range(4)]
print('Pure W tensor |+>: rho_AE = rho_A tensor rho_E exactly; no exterior correlations.')
print('Any correlated extension must change the pure internal ABC state; 1/9 is not unused purity.')

# Distinguish the invariant qutrit baryon from a GHZ tensor.
charges = (1, -1, 0)
ghz_charges = [3 * q for q in charges]
epsilon_charges = sum(charges)
assert ghz_charges == [3, -3, 0] and epsilon_charges == 0
print('Colour generator diag(1,-1,0): qutrit GHZ component charges = 3,-3,0; epsilon singlet = 0.')
print('The ordinary qutrit GHZ tensor is not an SU(3) singlet; a physical encoding needs an intertwiner.')

# Delta has a perfect inverse on its image; tracing a copy is a different map.
delta = [[F(int(row == 3 * col)) for col in range(2)] for row in range(4)]
left_inverse_product = [[sum(delta[k][a] * delta[k][b] for k in range(4)) for b in range(2)] for a in range(2)]
assert left_inverse_product == [[1, 0], [0, 1]]
print('Copy isometry: Delta^dagger Delta = I exactly; its restriction to its image is invertible.')
print('Irreversibility requires discarded access or coarse-graining, not non-surjectivity alone.')
print('All counterchecks passed; no paper or ledger status changed.')
