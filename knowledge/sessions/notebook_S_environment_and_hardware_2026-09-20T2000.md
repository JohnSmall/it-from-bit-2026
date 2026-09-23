# Session note: a persistent environment for the notebooks, and notebook S on hardware

Date: 2026-09-20T2000. Session: Claude Code (Opus 5), housekeeping.
Companion to `graded_fanout_complex_cost_2026-09-18T0830.md`, which is the
argument; this note is the environment and the device run.

## 1. The environment

Notebook S had been executed in a throwaway venv with a kernel-free runner and
that venv was gone, so its outputs were real but not reproducible by anyone.
This builds a persistent one.

Ubuntu 22.04's Python 3.10 has neither `venv` nor `ensurepip`, and there is no
`virtualenv`, `conda`, `pipx` or `uv` on the machine; the snap Jupyter is a
Python 3.7 that cannot host Qiskit. Rather than install system packages, the
environment is built from PyPA's self-contained virtualenv zipapp, which needs
no `sudo` and installs nothing system-wide:

    curl -sL -o /tmp/virtualenv.pyz https://bootstrap.pypa.io/virtualenv.pyz
    python3 /tmp/virtualenv.pyz --python python3 .venv
    .venv/bin/pip install -r notebooks/requirements.txt

Confirmed afterwards that system Python is untouched: `qiskit`, `qiskit_aer`,
`qiskit_ibm_runtime` and `ipykernel` all absent from it. The whole footprint is
`.venv/` (686 MB, gitignored, in the repository root), a 28 KB kernel spec
under `~/.local/share/jupyter/kernels/self-ref-2026`, and a 14 MB virtualenv
cache. `rm -rf .venv ~/.local/share/jupyter/kernels/self-ref-2026` undoes it.

Versions, matching the 2026-09-18 run:

    python 3.10.12   qiskit 2.5.2   qiskit-aer 0.17.2   numpy 2.2.6   matplotlib 3.10.9
    qiskit-ibm-runtime 0.49.0

A kernel was registered as `self-ref-2026` and the notebook re-executed through
it with `jupyter nbconvert --execute`.

**Every one of the six original code cells reproduces its numbers exactly.**
Three differences appeared and none is numerical: two consecutive `print` calls
land as separate stream outputs rather than one merged output, the figure's
`text/plain` repr reads `<Figure size 600x400 with 1 Axes>` where the old
runner wrote `<Figure>`, and the embedded PNG re-encodes to a different byte
length (49,804 base64 characters against 57,412). The seed-locking holds: the
mutual-information rows, the cost table and the Aer results are identical
character for character.

The recipe, the kernel registration and those three harmless differences are
recorded in `notebooks/README.md`, with `notebooks/requirements.txt` pinning 27
packages.

## 2. The IBM instance, and a trap worth recording

The CRN supplied for the account turned out to name `bb-quantum`, a
**pay-as-you-go** instance capped at six seconds of QPU time, all six already
spent on 12 June. The first submission was refused:

    409 Conflict, code 1218: "Instance time limit exceeded"

The account carries four instances:

| name | plan |
|---|---|
| `use-sparingly` | pay-as-you-go (eu-de) |
| `open-instance` | **open** |
| `bb-quantum` | pay-as-you-go, 6 s cap |
| `fable_1` | pay-as-you-go |

The 10 minutes visible in the IBM UI belong to `open-instance`. JS repointed
`~/.qiskit/qiskit-ibm.json` at it and the run went ahead.

The cap did the job it was there for. Had `bb-quantum` been uncapped the job
would have run and been billed. Anything here that submits to hardware should
name the open instance explicitly rather than rely on the saved default, since
three of the four instances cost money. The token itself is never in this
repository; it lives in `~/.qiskit/qiskit-ibm.json`, mode 0600.

## 3. The hardware cell

Added after the Aer cell in section 5 by
`scripts/patch_notebook_S_hardware_cell_2026-09-20T1000.py`: the same
phase-only test on a real device. $R = 6$ fragments, $\phi = 0$ so the copies
carry phase and no distinguishability, $\theta_k = 1$ each, 20,000 shots,
forward and with the phases undone. Optimisation level 1, which keeps the six
controlled rotations as twenty-one two-qubit gates instead of collapsing them
to a single phase; level 0 preserves more structure but at depth 247 against
72, and the extra depth is decoherence rather than physics.

Exact stdout:

```
backend ibm_marrakesh   job dao3stopqrnc7399f8vg   2026-09-20 20:13 UTC
sum theta/2 = 3.0000, shots = 20000
  forward  depth  72, 21 two-qubit gates: P(+) measured = 0.1270   formula = 0.0050   shortfall = +0.1219
  reversed depth 138, 48 two-qubit gates: P(+) measured = 0.7855   formula = 1.0000   shortfall = -0.2145
```

13 seconds of the 600 consumed.

### What it shows

Both figures are degraded, and both are degraded *towards* $0.5$, which is what
total loss of coherence would give. Read against that baseline rather than
against the ideal, the phase survives the device plainly: the forward case sits
at 0.127 where coherent interference predicts 0.005 and decoherence predicts
0.5, so most of the interference is intact; the reversal recovers 0.786 of the
way back where a decohered system would have stayed at 0.5. The imaginary cost
is relative, observable and reversible on real hardware, which is the claim the
simulator cell makes. It is simply not free of the device.

The markdown note added beneath the cell says the rest: every controlled
rotation is a physical two-qubit gate on a machine of finite coherence, so some
phase leaks into the environment of the device itself before the final $H$ can
bring it back, and that leakage is a real cost paid to an environment the model
does not carry. The model's fragments are the only environment it knows about
and it assumes the copies are otherwise perfect. The gap between the two cells
is the size of the term left out.

This is a demonstration, not a second proof. A device result is not
reproducible the way the simulator result is — the machine drifts and is
recalibrated — so the backend, the job id, the date and the transpiled depth
are printed with the numbers and belong with any figure quoted from them.

## 4. Proposed ledger entries

Not written to any ledger. For JS to accept, amend or reject.

### results_ledger.md, dated 2026-09-20

- **ESTABLISHED** `[PROPOSED]` The phase carried by graded FANOUT copies is
  observable and reversible on hardware, not only in simulation. On
  `ibm_marrakesh`, six phase-only copies with $\theta_k = 1$ give
  $P(+) = 0.1270$ against the closed form $0.0050$ and a fully decohered
  $0.5$; undoing the phases returns $0.7855$ against $1.0000$. Job
  `dao3stopqrnc7399f8vg`, 20,000 shots, depths 72 and 138.
- **STRUCTURAL** `[PROPOSED]` Device decoherence is a real-cost term the model
  omits. The model treats the $R$ fragments as the entire environment and the
  copies as otherwise perfect; a real device has an environment of its own, and
  the shortfalls above measure what that costs at this depth. Any hardware
  demonstration of the complex-cost picture will show it.

## 5. Not done

- Nothing in `paper1/` was touched; this is v2 material.
- No ledger was edited.
- The notebook's `kernelspec` now names `self-ref-2026` rather than the generic
  `python3`, so it opens against the right environment. That is a metadata
  change to a file that was previously unexecuted-then-executed elsewhere, and
  it is the only edit to the notebook beyond the two inserted cells.
- The other work in the tree from the Fable session — the new project
  documents, scripts, bib batches and the `paper1/` edits — is untouched and
  not part of this.
