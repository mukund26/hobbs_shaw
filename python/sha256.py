k = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
]

h_val = [
    0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 
    0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
]

MOD = 2**32

def string_to_binary(msg):
    binary = []
    for ch in msg:
        binary.append(bin(ord(ch))[2:].zfill(8))
    return ''.join(binary)


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
    

def _right_rotate(num, val):
    return num >> val | num << (32 - val)

def _right_shift(num, val):
    return num >> val

def string_to_int(binary_str):
    return int(binary_str, 2)
    
    
if __name__ == "__main__":
    print(generate_sha256("Hello world!!").hex())
