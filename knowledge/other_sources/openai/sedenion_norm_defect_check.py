#!/usr/bin/env python3
"""Check the real sedenion norm-defect/associator identity.

Convention:
    (a,b)(c,d) = (ac - conjugate(d)b, da + b conjugate(c)).
    [a,b,c] = (ab)c - a(bc).
    Delta(x,y) = ||x||^2 ||y||^2 - ||xy||^2.

Identity:
    Delta((a,b),(c,d)) = -2 <[a,b,c], d>.

Requires Python 3 and NumPy. All main checks use exact int64 arithmetic
with coefficient ranges small enough to avoid overflow.
The random tests are verification, not a replacement for the proof.
"""
from itertools import product
import numpy as np

def conjugate(x):
    out = np.array(x, copy=True)
    out[1:] *= -1
    return out

def cd_product(x, y):
    x, y = np.asarray(x), np.asarray(y)
    n = x.size
    if x.shape != y.shape or x.ndim != 1 or n < 1 or n & (n-1):
        raise ValueError("Equal one-dimensional power-of-two lengths required.")
    if n == 1:
        return x*y
    h = n//2
    a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate((
        cd_product(a,c) - cd_product(conjugate(d),b),
        cd_product(d,a) + cd_product(b,conjugate(c))
    ))

def table(n):
    basis = np.eye(n, dtype=np.int64)
    return np.array([[cd_product(u,v) for v in basis] for u in basis])

OCTONIONS = table(8)
SEDENIONS = table(16)

def multiply(x,y):
    if len(x) != len(y) or len(x) not in (8,16):
        raise ValueError("Expected two octonions or two sedenions.")
    t = OCTONIONS if len(x) == 8 else SEDENIONS
    return np.einsum("i,j,ijk->k",x,y,t)

def norm2(x):
    return np.dot(x,x)

def associator(a,b,c):
    return multiply(multiply(a,b),c)-multiply(a,multiply(b,c))

def defect(x,y):
    return norm2(x)*norm2(y)-norm2(multiply(x,y))

def associator_expression(x,y):
    a,b,c,d = x[:8],x[8:],y[:8],y[8:]
    return -2*np.dot(associator(a,b,c),d)

def hopf_candidate(x,y):
    return np.r_[norm2(x)-norm2(y), 2*multiply(x,conjugate(y))]

def main():
    e = np.eye(8,dtype=np.int64)
    x = np.r_[e[1],e[2]]
    for sign in (-1,1):
        y = np.r_[e[4],sign*e[7]]
        print(f"d = {sign:+d} e7: xy = {multiply(x,y)}")
        print(f"  Delta = {defect(x,y)}, associator expression = "
              f"{associator_expression(x,y)}")
        assert defect(x,y) == associator_expression(x,y)

    # Exhaustive equality of the four-linear cross-term coefficients.
    for i,j,k,l in product(range(8),repeat=4):
        a,b,c,d = e[i],e[j],e[k],e[l]
        cross = 2*(np.dot(multiply(a,c),multiply(conjugate(d),b))
                   - np.dot(multiply(d,a),multiply(b,conjugate(c))))
        rhs = -2*np.dot(associator(a,b,c),d)
        assert cross == rhs, (i,j,k,l,cross,rhs)
    print("PASS: all 4096 four-linear coefficient checks.")

    rng = np.random.default_rng(20260925)
    for _ in range(2000):
        x = rng.integers(-5,6,size=16,dtype=np.int64)
        y = rng.integers(-5,6,size=16,dtype=np.int64)
        assert defect(x,y) == associator_expression(x,y)
    print("PASS: 2000 exact-integer sample pairs.")

    for _ in range(200):
        x = rng.integers(-3,4,size=16,dtype=np.int64)
        y = rng.integers(-3,4,size=16,dtype=np.int64)
        expected = (norm2(x)+norm2(y))**2 - 4*defect(x,y)
        assert norm2(hopf_candidate(x,y)) == expected
    print("PASS: 200 Hopf-candidate norm checks.")

    x = np.r_[e[1],e[2]]/2
    y = np.r_[e[4],-e[7]]/2
    assert norm2(x)+norm2(y) == 1
    assert norm2(hopf_candidate(x,y)) == 0
    print("PASS: normalized S^31 input has zero Hopf-candidate image.")

if __name__ == "__main__":
    main()
