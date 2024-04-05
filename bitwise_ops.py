def _right_rotate(num, val, size = 32):
    return num >> val | num << (size - val)

def _right_shift(num, val):
    return num >> val