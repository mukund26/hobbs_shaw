from constants import BLOCK_SIZE_SHA256
from utils import create_blocks
from sha_ops import create_message_schedule, compression
from preprocess import convert_input_to_binary_string

def sha256_digest(msg):

    binary_string = convert_input_to_binary_string(msg)
    
    orig_len = len(binary_string) # no of bits

    # add single 1 bit
    binary_string += '1'
    
    l = len(binary_string)
    
    # calculate no of zeros
    x = (BLOCK_SIZE_SHA256 - (l + 64) % BLOCK_SIZE_SHA256) % BLOCK_SIZE_SHA256
    
    binary_string += '0' * x
        
    #append 64 bit value of no of bits in original msg
    binary_string += ''.join(bin(orig_len)[2:].zfill(64))
    
    print("Total bits hashed: ", len(binary_string), end='\n\n')
        
    # create 512 bit blocks
    blocks = create_blocks(binary_string, BLOCK_SIZE_SHA256)
                
    #sha computation
    for block in blocks:
        w = create_message_schedule(block)
        h_val = compression(w)
        
    return ((h_val[0]).to_bytes(4, 'big') + (h_val[1]).to_bytes(4, 'big') +
            (h_val[2]).to_bytes(4, 'big') + (h_val[3]).to_bytes(4, 'big') +
            (h_val[4]).to_bytes(4, 'big') + (h_val[5]).to_bytes(4, 'big') +
            (h_val[6]).to_bytes(4, 'big') + (h_val[7]).to_bytes(4, 'big'))
