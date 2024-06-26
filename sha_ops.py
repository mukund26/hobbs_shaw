from utils import string_to_int
from bitwise_ops import _right_rotate, _right_shift
from constants import MOD32, h_val, k, sha512_h, sha512_k, MOD64

def create_message_schedule(block):
    w = []
    for i in range(0, 512, 32):
        w.append(string_to_int(block[i : i + 32]))
                
    for i in range(16, 64):
        s0 = _right_rotate(w[i - 15], 7) ^ _right_rotate(w[i - 15], 18) ^ _right_shift(w[i - 15], 3)
        s1 = _right_rotate(w[i - 2], 17) ^ _right_rotate(w[i - 2], 19) ^ _right_shift(w[i - 2], 10)
        ans = (w[i - 16] + s0 + w[i - 7] + s1) % MOD32
        w.append(ans)
        
    return w


def compression(w):
    a = h_val[0]
    b = h_val[1]
    c = h_val[2]
    d = h_val[3]
    e = h_val[4]
    f = h_val[5]
    g = h_val[6]
    h = h_val[7]    
        
    for i in range(0, 64):
        s1 = _right_rotate(e, 6) ^ _right_rotate(e, 11) ^ _right_rotate(e, 25)
        ch = (e & f) ^ ((~e) & g)
        temp1 = (h + s1 + ch + k[i] + w[i]) % MOD32
        s0 = _right_rotate(a, 2) ^ _right_rotate(a, 13) ^ _right_rotate(a, 22)
        maj = (a & b) ^ (a & c) ^ (b & c)
        temp2 = (s0 + maj) % MOD32
        
        h = g
        g = f
        f = e
        e = (d + temp1) % MOD32
        d = c
        c = b
        b = a
        a = (temp1 + temp2) % MOD32
        
    h_val[0] = (h_val[0] + a) % MOD32
    h_val[1] = (h_val[1] + b) % MOD32
    h_val[2] = (h_val[2] + c) % MOD32
    h_val[3] = (h_val[3] + d) % MOD32
    h_val[4] = (h_val[4] + e) % MOD32
    h_val[5] = (h_val[5] + f) % MOD32
    h_val[6] = (h_val[6] + g) % MOD32
    h_val[7] = (h_val[7] + h) % MOD32
    
    return h_val


def sha512_create_message_schedule(block):
    w = []
    for i in range(0, 1024, 64):
        w.append(string_to_int(block[i : i + 64]))
                
    for i in range(16, 80):
        s0 = _right_rotate(w[i - 15], 1, 64) ^ _right_rotate(w[i - 15], 8, 64) ^ _right_shift(w[i - 15], 7)
        s1 = _right_rotate(w[i - 2], 19, 64) ^ _right_rotate(w[i - 2], 61, 64) ^ _right_shift(w[i - 2], 6)
        ans = (w[i - 16] + s0 + w[i - 7] + s1) % MOD64
        w.append(ans)
        
    return w


def sha512_compression(w):
    a = sha512_h[0]
    b = sha512_h[1]
    c = sha512_h[2]
    d = sha512_h[3]
    e = sha512_h[4]
    f = sha512_h[5]
    g = sha512_h[6]
    h = sha512_h[7]    
        
    for i in range(0, 80):
        s1 = _right_rotate(e, 14, 64) ^ _right_rotate(e, 18, 64) ^ _right_rotate(e, 41, 64)
        ch = (e & f) ^ ((~e) & g)
        temp1 = (h + s1 + ch + sha512_k[i] + w[i]) % MOD64
        s0 = _right_rotate(a, 28, 64) ^ _right_rotate(a, 34, 64) ^ _right_rotate(a, 39, 64)
        maj = (a & b) ^ (a & c) ^ (b & c)
        temp2 = (s0 + maj) % MOD64
        
        h = g
        g = f
        f = e
        e = (d + temp1) % MOD64
        d = c
        c = b
        b = a
        a = (temp1 + temp2) % MOD64
        
    sha512_h[0] = (sha512_h[0] + a) % MOD64
    sha512_h[1] = (sha512_h[1] + b) % MOD64
    sha512_h[2] = (sha512_h[2] + c) % MOD64
    sha512_h[3] = (sha512_h[3] + d) % MOD64
    sha512_h[4] = (sha512_h[4] + e) % MOD64
    sha512_h[5] = (sha512_h[5] + f) % MOD64
    sha512_h[6] = (sha512_h[6] + g) % MOD64
    sha512_h[7] = (sha512_h[7] + h) % MOD64
    
    return sha512_h
