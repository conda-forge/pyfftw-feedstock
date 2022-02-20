import numpy as np

import pyfftw
import pyfftw.builders
from pyfftw.interfaces.numpy_fft import fftn

# the following transform will fail if MKL FFT routines are being linked to
# instead of the FFTW ones.  (MKL doesn't support FFT of only 1
# dimension of a 3D array).
# see:  https://github.com/pyFFTW/pyFFTW/issues/40
r = np.random.randn(32, 32, 32)
fftn(r, axes=(0, ))

# the following transform will fail if static linking is broken as in
# https://github.com/pyFFTW/pyFFTW/issues/294
arr = np.random.randint(1, 500, (128, 128)).astype(np.complex64)
out = pyfftw.FFTW(arr, np.empty_like(arr), axes=(0, 1))()
