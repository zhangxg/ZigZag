import pyximport
import numpy

pyximport.install(
    setup_args={"include_dirs": numpy.get_include()},
    language_level=3,
    reload_support=True,
)

from zigzag.core import *

PEAK = 1
VALLEY = -1
