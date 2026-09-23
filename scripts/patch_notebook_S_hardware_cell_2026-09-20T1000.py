#!/usr/bin/env python3
"""Add an IBM hardware cell to notebook S, after the Aer cell in section 5.

The Aer cell shows the phase-only test in simulation: R = 6 fragments, phi = 0
so the copies carry phase and no distinguishability, theta_k = 1 each, and the
system read in the X basis gives P(+) = (1 + cos(sum theta / 2)) / 2 = 0.0050,
returning to 1.0000 when the phases are undone. That is the notebook's claim
that the imaginary cost is real, relative and reversible.

This adds the same test on a real device. It is a demonstration, not a second
proof: the simulator cell is the reproducible claim and stays exactly as it is.
A device result is not reproducible in that sense -- the machine drifts and is
recalibrated between runs -- so the cell reports the backend, the date and the
transpiled depth alongside the numbers, and those three belong with any figure
quoted from it.

Optimisation level 1: it keeps the six controlled rotations as twenty-one
two-qubit gates rather than collapsing them to a single phase, which is the
point, while not inflating the depth the way level 0 does (247 against 72).

Two cells are inserted after the Aer cell: the code, and a markdown note that
device decoherence is a real-cost term the model does not carry.

Anchors matched exactly once. A .bak is written, and the script refuses to run
twice.
"""

import json
import shutil
import sys

NB = "notebooks/notebook_S_graded_fanout_complex_cost_2026-09-18.ipynb"
MARK = "QiskitRuntimeService"

CODE = r"""# --- the same phase-only test on a real device -------------------------------
# A demonstration, not a second proof: the Aer cell above is the reproducible
# claim. Needs qiskit-ibm-runtime and a saved account; see notebooks/README.md.
import datetime
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2

R_HW, TH_HW, SHOTS_HW = 6, 1.0, 20000

def hw_circuit(undo=False):
    qc = QuantumCircuit(R_HW + 1, 1)
    qc.h(0)
    for k in range(R_HW):
        qc.cry(0.0, 0, k + 1)      # phi = 0: phase only, no distinguishability
        qc.crz(TH_HW, 0, k + 1)
    if undo:
        for k in range(R_HW):
            qc.crz(-TH_HW, 0, k + 1)
    qc.h(0)
    qc.measure(0, 0)
    return qc

service = QiskitRuntimeService()
backend = service.backend("ibm_marrakesh")
pm = generate_preset_pass_manager(optimization_level=1, backend=backend)

isa = {tag: pm.run(hw_circuit(undo)) for tag, undo in (("forward", False), ("reversed", True))}
sampler = SamplerV2(mode=backend)
job = sampler.run([isa["forward"], isa["reversed"]], shots=SHOTS_HW)
print("backend %s   job %s   %s UTC" % (backend.name, job.job_id(),
                                        datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M")))
result = job.result()

half_sum = 0.5 * R_HW * TH_HW
print("sum theta/2 = %.4f, shots = %d" % (half_sum, SHOTS_HW))
for i, tag in enumerate(("forward", "reversed")):
    counts = result[i].data.c.get_counts()
    p_plus = counts.get("0", 0) / SHOTS_HW
    expected = 0.5 * (1 + math.cos(half_sum)) if tag == "forward" else 1.0
    print("  %-8s depth %3d, %2d two-qubit gates: P(+) measured = %.4f   formula = %.4f   shortfall = %+.4f"
          % (tag, isa[tag].depth(),
             sum(1 for ins in isa[tag].data if ins.operation.num_qubits == 2),
             p_plus, expected, p_plus - expected))
"""

NOTE = r"""The device does not reach either figure, and the gap is the point. Every
controlled rotation is a physical two-qubit gate on a machine with finite
coherence, so some of the phase leaks into the environment of the device itself
before the final $H$ can bring it back. That leakage is a real cost, paid to an
environment the model does not carry: the model's fragments are the only
environment it knows about, and it assumes the copies are otherwise perfect.
The simulator, which has no such environment, returns the closed forms. The
difference between the two cells is the size of the term that has been left
out."""


def main():
    nb = json.load(open(NB, encoding="utf-8"))
    if any(MARK in "".join(c["source"]) for c in nb["cells"]):
        sys.exit("REFUSING: a hardware cell is already present")

    idx = [i for i, c in enumerate(nb["cells"])
           if c["cell_type"] == "code" and "AerSimulator" in "".join(c["source"])]
    if len(idx) != 1:
        sys.exit("REFUSING: found %d Aer cells, expected 1" % len(idx))
    at = idx[0] + 1

    before = len(nb["cells"])
    nb["cells"][at:at] = [
        {"cell_type": "code", "metadata": {}, "execution_count": None,
         "outputs": [], "source": CODE},
        {"cell_type": "markdown", "metadata": {}, "source": NOTE},
    ]
    if len(nb["cells"]) != before + 2:
        sys.exit("REFUSING: cell count did not rise by two")
    if "AerSimulator" not in "".join(nb["cells"][idx[0]]["source"]):
        sys.exit("REFUSING: the Aer cell was disturbed")

    shutil.copy2(NB, NB + ".bak")
    with open(NB, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    print("inserted the hardware cell and its note after cell %d; %d cells now"
          % (idx[0], len(nb["cells"])))


if __name__ == "__main__":
    main()
