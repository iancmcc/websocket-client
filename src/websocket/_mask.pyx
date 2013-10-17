#cython: boundscheck=False
#cython: wraparound=False

def mask(str mask_key, str data):
    cdef int i, l, x
    cdef object m, d
    cdef str s
    m = bytearray(mask_key)
    d = bytearray(data)
    l = len(d)
    for i in range(l):
        x = i % 4
        d[i] ^= m[x]
    s = str(d)
    return s
