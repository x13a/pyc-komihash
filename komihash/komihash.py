import cython
from cython.cimports import ckomihash

@cython.ccall
@cython.exceptval(0, check=True)
def komihash(key: bytes, seed: cython.ulonglong = 0) -> cython.ulonglong:
    return ckomihash.komihash(cython.cast(cython.p_char, key), len(key), seed)

@cython.ccall
@cython.exceptval(0, check=True)
def komirand(seed1: cython.ulonglong, seed2: cython.ulonglong) -> cython.ulonglong:
    return ckomihash.komirand(
        cython.cast(cython.p_ulonglong, cython.address(seed1)), 
        cython.cast(cython.p_ulonglong, cython.address(seed2)),
    )
