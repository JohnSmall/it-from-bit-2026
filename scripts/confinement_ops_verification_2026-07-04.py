"""Executable verification for the confinement section's two op resolutions
(2026-07-04): prop:energy-locus (the binding admits no invariant locus) and
the glueball class dictionary (op:glueball-spectrum, class half).

PART 1 -- energy locus: (1a) pre-fusion correlation wholly pairwise;
(1b) full fusion -> exactly GHZ3, success 1/4, tau3=1, pairwise 0;
(1c) single-vertex fusion -> exactly GHZ3 x Bell, success 1/2;
(1d) external exclusion in each presentation (I(leg:non-partner)=0).

PART 2 -- glueball classes: (2a) vertex assignments induce exactly the
even-parity edge patterns (K3 cycle parity); (2b) the Frobenius fusion
transmits precisely those four, prob 1/4 each, annihilating every
vertex-inconsistent pattern; (2c) the four outputs are the four mutually
orthogonal GHZ-type pair states, the flipped position = vertex opposite the
aligned edge (class-resolving); (2d) antiparticle members transmit under one
antipode on any edge (position-free); (2e) the d/f identity against explicit
Gell-Mann matrices: Tr(TaTbTc) +/- reversed = d/2, i f/2.
Run: python3 confinement_ops_verification_2026-07-04.py
"""
import numpy as np
from itertools import product as iproduct

ok_all = True
def report(name, ok):
    global ok_all; ok_all &= ok; print(("PASS " if ok else "FAIL ") + name)

B  = np.array([1,0,0,1],complex)/np.sqrt(2); Bm = np.array([0,1,-1,0],complex)/np.sqrt(2)
Y  = np.array([[0,-1j],[1j,0]]); GHZ = np.zeros(8,complex); GHZ[0]=GHZ[7]=1/np.sqrt(2)
mu = np.zeros((2,2,2)); mu[0,0,0]=1; mu[1,1,1]=1

class Net:
    def __init__(s,v,l): s.t=v.reshape([2]*len(l)); s.lab=list(l)
    def fuse(s,a,b,new):
        ia,ib=s.lab.index(a),s.lab.index(b)
        s.t=np.tensordot(mu,np.moveaxis(s.t,[ia,ib],[0,1]),axes=([0,1],[0,1]))
        s.lab=[new]+[x for x in s.lab if x not in (a,b)]; return s
    def vec(s,order):
        return np.moveaxis(s.t,[s.lab.index(l) for l in order],range(len(order))).reshape(-1)

def tri(bits,dress=(0,0,0)):
    e=[]
    for b,d in zip(bits,dress):
        v=(B if b==0 else Bm).reshape(2,2)
        if d: v=Y@v
        e.append(v.reshape(-1))
    return Net(np.kron(np.kron(e[0],e[1]),e[2]),['a1','b1','b2','c1','c2','a2'])
full=lambda n: n.fuse('a2','a1','A').fuse('b1','b2','Bq').fuse('c1','c2','Cq').vec(['A','Bq','Cq'])

def rho(psi,keep,n):
    psi=psi.reshape([2]*n); ax=[i for i in range(n) if i not in keep]
    r=np.tensordot(psi,psi.conj(),axes=(ax,ax)); d=2**len(keep); return r.reshape(d,d)
def S(r):
    ev=np.linalg.eigvalsh(r); ev=ev[ev>1e-12]; return float(-(ev*np.log2(ev)).sum())
def concurrence(r2):
    yy=np.kron([[0,-1j],[1j,0]],[[0,-1j],[1j,0]])
    ev=np.sqrt(np.abs(np.sort(np.linalg.eigvals(r2@yy@r2.conj()@yy).real)[::-1]))
    return max(0,ev[0]-ev[1]-ev[2]-ev[3])
def tau3(psi):
    a=psi.reshape(2,2,2)
    d1=a[0,0,0]**2*a[1,1,1]**2+a[0,0,1]**2*a[1,1,0]**2+a[0,1,0]**2*a[1,0,1]**2+a[1,0,0]**2*a[0,1,1]**2
    d2=a[0,0,0]*a[1,1,1]*(a[0,1,1]*a[1,0,0]+a[1,0,1]*a[0,1,0]+a[1,1,0]*a[0,0,1]) \
      +a[0,1,1]*a[1,0,0]*(a[1,0,1]*a[0,1,0]+a[1,1,0]*a[0,0,1])+a[1,0,1]*a[0,1,0]*a[1,1,0]*a[0,0,1]
    d3=a[0,0,0]*a[1,1,0]*a[1,0,1]*a[0,1,1]+a[1,1,1]*a[0,0,1]*a[0,1,0]*a[1,0,0]
    return float(4*abs(d1-2*d2+4*d3))

print("== PART 1: prop:energy-locus ==")
pre = tri([0,0,0]).vec(['a1','b1','b2','c1','c2','a2'])
cs=[concurrence(rho(pre,[0,1],6)),concurrence(rho(pre,[2,3],6)),concurrence(rho(pre,[4,5],6))]
report("(1a) pre-fusion pairwise: edge concurrences all 1", np.allclose(cs,1))
mi_np = S(rho(pre,[0],6))+S(rho(pre,[2,3,4,5],6))-S(rho(pre,[0,2,3,4,5],6))
report("(1a') pre-fusion: I(leg : non-partner) = 0", abs(mi_np)<1e-9)
out = full(tri([0,0,0]))
report("(1b) full fusion: success 1/4, output exactly GHZ3",
       np.isclose(np.linalg.norm(out)**2,0.25) and np.isclose(abs(GHZ.conj()@out)**2,0.25))
outn=out/np.linalg.norm(out)
report("(1b') tau3 = 1 and pairwise concurrences 0",
       np.isclose(tau3(outn),1) and all(concurrence(rho(outn,p,3))<1e-9 for p in ([0,1],[0,2],[1,2])))
n1 = tri([0,0,0]).fuse('a2','a1','A'); v=n1.vec(['A','b1','c2','b2','c1'])
report("(1c) one-vertex fusion: success 1/2, exactly GHZ3 x Bell",
       np.isclose(np.linalg.norm(v)**2,0.5) and np.isclose(abs(np.kron(GHZ,B).conj()@(v/np.linalg.norm(v)))**2,1))

# (1f) the lockstep trade-off: external entangling of one quark destroys GHZ fidelity monotonically
GHZ_D = np.kron(GHZ, np.array([1,0],complex))          # GHZ_ABC x |0>_D
def couple(theta):
    XX = np.kron(np.array([[0,1],[1,0]]), np.array([[0,1],[1,0]]))
    U = np.cos(theta)*np.eye(4) + 1j*np.sin(theta)*XX   # acts on (q1, D)
    p = GHZ_D.reshape([2]*4)                            # (q1,q2,q3,D)
    p = np.moveaxis(p,[0,3],[0,1]).reshape(4,4)         # (q1,D) x (q2,q3)
    p = (U @ p).reshape([2,2,2,2])
    return np.moveaxis(p,[0,1],[0,3]).reshape(-1)       # back to (q1,q2,q3,D)
Fs, Es = [], []
def H2(x):
    x = min(max(x,1e-15),1-1e-15); return -(x*np.log2(x)+(1-x)*np.log2(1-x))
for th in np.linspace(0, np.pi/4, 25):
    psi = couple(th)
    rABC = rho(psi,[0,1,2],4); F = float((GHZ.conj() @ rABC @ GHZ).real)
    E = S(rho(psi,[3],4)); Fs.append(F); Es.append(E)
mono = all(Fs[i+1] <= Fs[i]+1e-9 for i in range(len(Fs)-1)) and all(Es[i+1] >= Es[i]-1e-9 for i in range(len(Es)-1))
exact = max(abs(Es[i]-H2(Fs[i])) for i in range(len(Fs)))
report("(1f) lockstep trade-off: F falls 1->1/2 as external entropy rises 0->1, monotone, and "
       "EXACTLY S_D = H2(F) (max dev %.1e)" % exact,
       mono and np.isclose(Fs[0],1) and Es[0]<1e-9 and np.isclose(Fs[-1],0.5) and np.isclose(Es[-1],1) and exact<1e-9)

# (1g) the other reading of the ledger: W's unspent ninth, the external ceiling, the migration
Wst = np.zeros(8, complex); Wst[[1,2,4]] = 1/np.sqrt(3)
tR0 = 4*np.linalg.det(rho(Wst,[0],3)).real
tAB0 = concurrence(rho(Wst,[0,1],3))**2; tAC0 = concurrence(rho(Wst,[0,2],3))**2
report("(1g-i) W ledger: tau_1(rest)=8/9 = 4/9 + 4/9 + 0; slack = 1/9",
       np.isclose(tR0,8/9) and np.isclose(tAB0,4/9) and np.isclose(tAC0,4/9) and np.isclose(1-tR0,1/9))
WD = np.kron(Wst, np.array([1,0],complex))
def couple_W(theta):
    XX = np.kron(np.array([[0,1],[1,0]]), np.array([[0,1],[1,0]]))
    U = np.cos(theta)*np.eye(4) + 1j*np.sin(theta)*XX
    p = WD.reshape([2]*4); p = np.moveaxis(p,[0,3],[0,1]).reshape(4,4)
    p = (U @ p).reshape([2]*4)
    return np.moveaxis(p,[0,1],[0,3]).reshape(-1)
best, ckw_ok = 0.0, True
for th in np.linspace(0, np.pi/2, 61):
    psi = couple_W(th)
    t1D = concurrence(rho(psi,[0,3],4))**2
    t1B = concurrence(rho(psi,[0,1],4))**2
    t1C = concurrence(rho(psi,[0,2],4))**2
    t1R = 4*np.linalg.det(rho(psi,[0],4)).real
    ckw_ok &= (t1R >= t1B + t1C + t1D - 1e-9)
    best = max(best, t1D)
report("(1g-ii) four-party CKW held at every coupling; external ceiling attained: max tau_1D = 1/9",
       ckw_ok and np.isclose(best, 1/9, atol=1e-6))
psi = couple_W(np.pi/4)
t1D = concurrence(rho(psi,[0,3],4))**2; t1B = concurrence(rho(psi,[0,1],4))**2
t1C = concurrence(rho(psi,[0,2],4))**2; t1R = 4*np.linalg.det(rho(psi,[0],4)).real
report("(1g-iii) migration at maximal coupling: internals -> 0, tau_1(rest) -> 1, residual = 8/9",
       t1B < 1e-9 and t1C < 1e-9 and np.isclose(t1R,1,atol=1e-6) and np.isclose(t1R - t1D, 8/9, atol=1e-6))

# (1h) the weak vertex on a confined quark: frame-flip legal and exact; pair-forming forbidden
Xg = np.array([[0,1],[1,0]],complex)
q_after = np.kron(np.kron(np.eye(2), Xg), np.eye(2)) @ GHZ          # local flip on B
full5 = np.kron(q_after, B)                                          # quark x lepton Bell
cross = max(concurrence(rho(full5,[q,l],5))**2 for q in (0,1,2) for l in (3,4))
ok_h = np.isclose(tau3(q_after),1) and cross < 1e-12 and S(rho(full5,[0,1,2],5)) < 1e-9
ok_h &= np.isclose(concurrence(rho(full5,[3,4],5)), 1)
th = 0.1
p = np.kron(GHZ, np.array([1,0],complex)).reshape([2]*4)
XX = np.kron(Xg,Xg); U = np.cos(th)*np.eye(4) + 1j*np.sin(th)*XX
p = np.moveaxis(p,[1,3],[0,1]).reshape(4,4); p = (U@p).reshape([2]*4)
p = np.moveaxis(p,[0,1],[1,3]).reshape(-1)
F = float((GHZ.conj() @ rho(p,[0,1,2],4) @ GHZ).real)
ok_h &= np.isclose(F, np.cos(th)**2) and S(rho(p,[0,1,2],4)) > 1e-3
report("(1h) weak vertex: frame-flip exact (tau3=1, quark x leptons product, pair entanglement on "
       "the leptons); pair-forming coupling degrades F = cos^2(theta) at first order", ok_h)

# (1i) the absent gate: the GHZ<->W converter exists, is exact both ways, and its ledger
Wv = np.zeros(8,complex); Wv[[1,2,4]] = 1/np.sqrt(3)
assert abs(GHZ.conj()@Wv) < 1e-14
K = np.outer(Wv,GHZ.conj()) - np.outer(GHZ,Wv.conj())
Uc = np.eye(8) + K + (K@K)                                   # exp((pi/2)K): sin=1, 1-cos=1
ok_i = np.linalg.norm(Uc.conj().T@Uc - np.eye(8)) < 1e-12
ok_i &= np.allclose(Uc@GHZ, Wv) and np.allclose(Uc.conj().T@Wv, GHZ)
ok_i &= np.isclose(tau3(Wv),0,atol=1e-12) and np.isclose(concurrence(rho(Wv,[0,1],3))**2, 4/9)
ok_i &= np.isclose(4*np.linalg.det(rho(Wv,[0],3)).real, 8/9)
interior = all(tau3((np.eye(8)+np.sin(th)*K+(1-np.cos(th))*(K@K))@GHZ) > 1e-6
               for th in np.linspace(0.05, np.pi/2-0.05, 9))
ok_i &= interior
report("(1i) absent gate: converter unitary, exact both ways; ledger flip (tau3 1->0, pairwise "
       "4/9, one-to-rest 8/9); tau3 > 0 at every interior point (W on the boundary stratum)", ok_i)

# (1g-iv) the two-ninths identity: slack = 1 - 4 det(rho) = r^2, for W and for random pure states
def bloch_r2(r2m):
    import numpy as _np
    X=_np.array([[0,1],[1,0]]); Y=_np.array([[0,-1j],[1j,0]]); Z=_np.array([[1,0],[0,-1]])
    return sum(float(_np.trace(r2m@P).real)**2 for P in (X,Y,Z))
ok_id = True
Wq = np.zeros(8,complex); Wq[[1,2,4]] = 1/np.sqrt(3)
for psi in [Wq] + [ (lambda p: p/np.linalg.norm(p))(np.random.default_rng(k).normal(size=8)
                    + 1j*np.random.default_rng(k+50).normal(size=8)) for k in range(4) ]:
    rA = rho(psi,[0],3)
    slack = 1 - 4*np.linalg.det(rA).real
    ok_id &= np.isclose(slack, bloch_r2(rA), atol=1e-10)
ok_id &= np.isclose(1 - 4*np.linalg.det(rho(Wq,[0],3)).real, 1/9)
report("(1g-iv) two-ninths identity: slack = 1 - 4 det(rho) = r^2 (random states + W's exact 1/9)", ok_id)

# (1g-v) the access ladder: Bell locked wire 0 (but r->1 after measurement); lepton 1/9; GHZ 0
Bp = np.array([1,0,0,1],complex)/np.sqrt(2)
rB = rho(Bp,[0],2); slack_B = 1 - 4*np.linalg.det(rB).real
post = np.array([1,0],complex)
r2_post = bloch_r2(np.outer(post,post.conj()))
Wl = np.zeros(8,complex); Wl[[1,2,4]] = 1/np.sqrt(3)
ok_l = np.isclose(slack_B, 0, atol=1e-12) and np.isclose(r2_post, 1)
ok_l &= np.isclose(1 - 4*np.linalg.det(rho(Wl,[0],3)).real, 1/9)
ok_l &= np.isclose(1 - 4*np.linalg.det(rho(GHZ,[0],3)).real, 0, atol=1e-12)
report("(1g-v) access ladder: Bell locked wire slack 0, post-measurement r^2 = 1; lepton 1/9; GHZ 0", ok_l)

print("\n== PART 2: glueball classes ==")
def edges(chi): return (chi[0]^chi[1], chi[1]^chi[2], chi[2]^chi[0])
induced = sorted(set(edges(chi) for chi in iproduct([0,1],repeat=3)))
even = sorted(b for b in iproduct([0,1],repeat=3) if sum(b)%2==0)
report("(2a) vertex assignments induce exactly the even-parity edge patterns", induced==even)
pairstate = {}
for flip in range(4):  # 0: none; 1..3: qubit flipped
    s=np.zeros(8,complex)
    i0 = 0 if flip==0 else 1<<(3-flip)
    s[i0]=s[7-i0]=1/np.sqrt(2); pairstate[flip]=s
trans_ok, orth_ok = True, True
outs={}
for bits in iproduct([0,1],repeat=3):
    out = full(tri(list(bits))); p=np.linalg.norm(out)**2
    if sum(bits)%2==0:
        trans_ok &= np.isclose(p,0.25); outs[bits]=out/np.linalg.norm(out)
    else:
        trans_ok &= p<1e-12
report("(2b) fusion transmits exactly the four classes at 1/4; annihilates all odd patterns", trans_ok)
# class -> aligned edge -> opposite vertex (A,B,C ~ flip 1,2,3); edges order (AB,BC,CA)
expect = {(0,0,0):0, (0,1,1):3, (1,0,1):1, (1,1,0):2}   # aligned edge -> flip at the OPPOSITE vertex: AB->C, BC->A, CA->B
for bits,fl in expect.items():
    orth_ok &= np.isclose(abs(pairstate[fl].conj()@outs[bits])**2,1)
G = np.array([[abs(outs[b1].conj()@outs[b2])**2 for b2 in expect] for b1 in expect])
report("(2c) four outputs = the four orthogonal GHZ-type pair states (class read off output)",
       orth_ok and np.allclose(G,np.eye(4)))
anti_ok=True
for pat in [(1,1,1),(0,0,1),(0,1,0),(1,0,0)]:
    for k in range(3):
        dr=[0,0,0]; dr[k]=1
        anti_ok &= np.isclose(np.linalg.norm(full(tri(list(pat),tuple(dr))))**2,0.25)
report("(2d) antiparticle members transmit under one antipode on ANY edge (position-free)", anti_ok)
l=np.zeros((8,3,3),complex)
l[0,0,1]=l[0,1,0]=1; l[1,0,1]=-1j; l[1,1,0]=1j; l[2,0,0]=1; l[2,1,1]=-1
l[3,0,2]=l[3,2,0]=1; l[4,0,2]=-1j; l[4,2,0]=1j; l[5,1,2]=l[5,2,1]=1
l[6,1,2]=-1j; l[6,2,1]=1j; l[7,0,0]=l[7,1,1]=1/np.sqrt(3); l[7,2,2]=-2/np.sqrt(3)
T=l/2; rng=np.random.default_rng(3); ok=True
for _ in range(40):
    a,b,c=rng.integers(0,8,3)
    d_=2*np.trace(T[a]@(T[b]@T[c]+T[c]@T[b])).real
    f_=(-2j*np.trace(T[a]@(T[b]@T[c]-T[c]@T[b]))).real
    ok &= np.isclose(np.trace(T[a]@T[b]@T[c]),0.25*(d_+1j*f_),atol=1e-10)
    ok &= np.isclose(np.trace(T[a]@T[c]@T[b]),0.25*(d_-1j*f_),atol=1e-10)
report("(2e) d/f identity: the two cyclic orderings' even/odd parts are exactly d/2 and i f/2", ok)
# (2f) neutral-gate compositions preserve species class (prop:neutral-blind support)
rng2 = np.random.default_rng(5)
def rand_diag_AB():
    ph = np.exp(1j*rng2.uniform(0,2*np.pi,4))
    return np.kron(np.diag(ph), np.eye(2))              # diagonal on (A,B), identity on C
def rand_U_C():
    a = rng2.normal(size=(2,2))+1j*rng2.normal(size=(2,2)); q,_ = np.linalg.qr(a)
    return np.kron(np.eye(4), q)
W3 = np.zeros(8,complex); W3[[1,2,4]] = 1/np.sqrt(3)
inv_ok = True
for base,(t3,cpat) in {"GHZ":(1.0,"zero"),"W":(0.0,"pos")}.items():
    psi = (GHZ if base=="GHZ" else W3).copy()
    for _ in range(6):
        psi = (rand_diag_AB() @ psi); psi = (rand_U_C() @ psi); psi/=np.linalg.norm(psi)
    t = tau3(psi); cs = [concurrence(rho(psi,p,3)) for p in ([0,1],[0,2],[1,2])]
    inv_ok &= np.isclose(t, t3, atol=1e-7)
    inv_ok &= (max(cs) < 1e-7) if cpat=="zero" else (min(cs) > 0.2)
report("(2f) neutral-gate compositions (A-B diagonals + C-unitaries) preserve the species class", inv_ok)
print("\nALL CHECKS PASS" if ok_all else "\nSOME CHECKS FAILED")
