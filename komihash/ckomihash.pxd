from libc.stdint cimport uint64_t

cdef extern from "../komihash_c/komihash.h":
    uint64_t komihash(const void* const msg, size_t msg_len, const uint64_t seed)
    uint64_t komirand(uint64_t* const seed1, uint64_t* const seed2)
