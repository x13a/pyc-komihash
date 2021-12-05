import cython
from cython.cimports import ckomihash

@cython.ccall
@cython.exceptval(0, check=True)
def hash64(key: bytes, seed: cython.ulonglong = 0) -> cython.ulonglong:
    return ckomihash.komihash(cython.cast(cython.p_char, key), len(key), seed)

@cython.cclass
class Rand:

    _seed1: cython.ulonglong
    _seed2: cython.ulonglong

    def __cinit__(self, seed1, seed2):
        self._seed1 = seed1
        self._seed2 = seed2
    
    @cython.ccall
    @cython.exceptval(0, check=True)
    def rand(self) -> cython.ulonglong:
        return ckomihash.komirand(cython.address(self._seed1), cython.address(self._seed2))
