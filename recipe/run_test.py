import sys

# We want to fail the test on unraisable exceptions, but we can't just
# exit() from unraisablehook since the SystemExit will also be
# swallowed
had_unraisable = False
def unraisablehook(unraisable):
    global had_unraisable
    had_unraisable = True
    sys.__unraisablehook__(unraisable)

sys.unraisablehook = unraisablehook

import numpy as np
import pyfftw.builders
from pyfftw.interfaces.numpy_fft import fftn
r = np.random.randn(32, 32, 32)

# the following transform will fail if MKL FFT routines are being linked to
# instead of the FFTW ones.  (MKL doesn't support FFT of only 1
# dimension of a 3D array).
# see:  https://github.com/pyFFTW/pyFFTW/issues/40
fftn(r, axes=(0, ))

sys.exit(1 if had_unraisable else 0)
