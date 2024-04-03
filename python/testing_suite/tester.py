import hashlib
import binascii

def hash(block_string, bin):
    if bin:
        resp = hashlib.sha256(block_string).hexdigest()
    else:
        resp = hashlib.sha256(block_string.encode()).hexdigest()
    print(f'Expected Hash: {resp}')
    return resp