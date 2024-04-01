def _right_rotate(num, val):
    return num >> val | num << (32 - val)

def _right_shift(num, val):
    return num >> val