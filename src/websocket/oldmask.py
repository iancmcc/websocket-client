import array

def mask(mask_key, data):
    m = array.array('B', mask_key)
    d = array.array('B', data)
    for i in xrange(len(d)):
        d[i] ^= m[i % 4]
    return d.tostring()

