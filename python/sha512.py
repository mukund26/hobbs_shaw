from constants import BLOCK_SIZE_SHA512
from utils import create_blocks
from sha_ops import sha512_create_message_schedule, sha512_compression
from preprocess import convert_input_to_binary_string

def sha512_digest(msg):

    binary_string = convert_input_to_binary_string(msg)
    
    orig_len = len(binary_string) # no of bits
    
    binary_string += '1'
    
    l = len(binary_string)
    
    x = (BLOCK_SIZE_SHA512 - (l + 128) % BLOCK_SIZE_SHA512) % BLOCK_SIZE_SHA512
    
    binary_string += '0' * x
        
    binary_string += ''.join(bin(orig_len)[2:].zfill(128))
            
    blocks = create_blocks(binary_string, BLOCK_SIZE_SHA512)
                    
    #sha computation
    for block in blocks:
        w = sha512_create_message_schedule(block)
        h_val = sha512_compression(w)
                
    return ((h_val[0]).to_bytes(8, 'big') + (h_val[1]).to_bytes(8, 'big') +
            (h_val[2]).to_bytes(8, 'big') + (h_val[3]).to_bytes(8, 'big') +
            (h_val[4]).to_bytes(8, 'big') + (h_val[5]).to_bytes(8, 'big') +
            (h_val[6]).to_bytes(8, 'big') + (h_val[7]).to_bytes(8, 'big'))
