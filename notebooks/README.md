# notebooks/

The lettered notebooks behind the paper's computations, A to S. They use
`qiskit.quantum_info` for the exact linear algebra and `qiskit-aer` for the
shot-based simulations; a few also talk to IBM Quantum hardware.

Every notebook is seed-locked. Given the same environment it reproduces its
numbers exactly, and if it does not, that is a finding worth reporting rather
than a nuisance to work around.

## The environment

`requirements.txt` pins what the notebooks were last run against. The versions
that matter are `qiskit==2.5.2` and `qiskit-aer==0.17.2`; the rest are whatever
those pulled in.

Ubuntu 22.04 ships Python 3.10 without the `venv` module and without
`ensurepip`, and the snap Jupyter is a Python 3.7 that cannot host Qiskit. So
the environment is built with PyPA's self-contained virtualenv zipapp, which
installs nothing system-wide and needs no `sudo`:

    curl -sL -o /tmp/virtualenv.pyz https://bootstrap.pypa.io/virtualenv.pyz
    python3 /tmp/virtualenv.pyz --python python3 .venv
    .venv/bin/pip install -r notebooks/requirements.txt

If your Python has `venv`, `python3 -m venv .venv` does the same job and you
can skip the zipapp.

`.venv/` is gitignored and lives at the repository root, one per clone.

## The Jupyter kernel

Register the environment as a kernel so the notebooks can be opened and run
in the usual way:

    .venv/bin/python -m ipykernel install --user \
        --name self-ref-2026 --display-name "Python 3 (self-ref-2026)"

Then `.venv/bin/jupyter lab` (or your own Jupyter, since the kernel is
registered under `~/.local/share/jupyter/kernels/`) and pick
**Python 3 (self-ref-2026)**.

To execute a notebook headlessly and check it still reproduces:

    .venv/bin/jupyter nbconvert --to notebook --execute \
        --ExecutePreprocessor.kernel_name=self-ref-2026 \
        --output-dir=/tmp --output check.ipynb \
        notebooks/notebook_S_graded_fanout_complex_cost_2026-09-18.ipynb

Compare the result against the committed file. Numerical output should be
identical. Three things differ harmlessly and are not regressions: consecutive
`print` calls may be split into separate stream outputs rather than merged, a
figure's `text/plain` repr may read `<Figure size 600x400 with 1 Axes>` rather
than `<Figure>`, and the embedded PNG will be re-encoded to a different byte
length. Compare the numbers, not the bytes.

## IBM Quantum hardware

Cells that run on real devices need `qiskit-ibm-runtime` and an account token.
**The token is never stored in this repository.** Save it once to your own
machine, where the Qiskit runtime keeps it under `~/.qiskit/`:

    .venv/bin/python -c "from qiskit_ibm_runtime import QiskitRuntimeService; \
        QiskitRuntimeService.save_account(channel='ibm_quantum_platform', \
        token='YOUR_TOKEN', instance='YOUR_CRN', overwrite=True)"

A hardware cell reports the backend name, the date and the transpiled depth
alongside its numbers, because a result from a real device is only meaningful
with those attached. Hardware results are not reproducible in the way the
simulator results are: the device drifts, and calibration changes between runs.
Where a notebook holds both, the simulator cell is the reproducible claim and
the hardware cell is the demonstration.
