from constants import k, h_val, MOD
from utils import string_to_binary, string_to_int
from bitwise_ops import _right_rotate, _right_shift

def generate_sha256(msg):
    
    # add checks for string or byte data and do the needful
    # for non above data return error
    
    binary_string = string_to_binary(msg)
    
    orig_len = len(binary_string) # no of bits
    
    # add single 1 bit
    binary_string += '1'
    
    l = len(binary_string)
    x = 0
    
    # add filler zeros such that (l + 1 + k + 64) % 512 == 0
    while (l + x + 64) % 512 != 0:
        binary_string += '0'
        x += 1
        
    #append 64 bit value of no of bits in original msg
    binary_string += ''.join(bin(orig_len)[2:].zfill(64))
        
    # create 512 bit blocks
    blocks = []
    for i in range(0, len(binary_string), 512):
        blocks.append(binary_string[i : i + 512])
                
    #sha computation
    for block in blocks:
        w = []
        for i in range(0, 512, 32):
            w.append(string_to_int(block[i : i + 32]))
                    
        
        for i in range(16, 64):
            s0 = _right_rotate(w[i - 15], 7) ^ _right_rotate(w[i - 15], 18) ^ _right_shift(w[i - 15], 3)
            s1 = _right_rotate(w[i - 2], 17) ^ _right_rotate(w[i - 2], 19) ^ _right_shift(w[i - 2], 10)
            ans = (w[i - 16] + s0 + w[i - 7] + s1) % MOD
            w.append(ans)

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
            temp1 = (h + s1 + ch + k[i] + w[i]) % MOD
            s0 = _right_rotate(a, 2) ^ _right_rotate(a, 13) ^ _right_rotate(a, 22)
            maj = (a & b) ^ (a & c) ^ (b & c)
            temp2 = (s0 + maj) % MOD
            
            h = g
            g = f
            f = e
            e = (d + temp1) % MOD
            d = c
            c = b
            b = a
            a = (temp1 + temp2) % MOD
            
        h_val[0] = (h_val[0] + a) % MOD
        h_val[1] = (h_val[1] + b) % MOD
        h_val[2] = (h_val[2] + c) % MOD
        h_val[3] = (h_val[3] + d) % MOD
        h_val[4] = (h_val[4] + e) % MOD
        h_val[5] = (h_val[5] + f) % MOD
        h_val[6] = (h_val[6] + g) % MOD
        h_val[7] = (h_val[7] + h) % MOD
        
    return ((h_val[0]).to_bytes(4, 'big') + (h_val[1]).to_bytes(4, 'big') +
            (h_val[2]).to_bytes(4, 'big') + (h_val[3]).to_bytes(4, 'big') +
            (h_val[4]).to_bytes(4, 'big') + (h_val[5]).to_bytes(4, 'big') +
            (h_val[6]).to_bytes(4, 'big') + (h_val[7]).to_bytes(4, 'big'))
    
    
    
if __name__ == "__main__":
    
    # read from file or string or binary stream
    # handle args
    # handle errors
    # create multiple files for all uses
    
    print(generate_sha256("Hello world!!").hex())
