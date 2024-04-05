from sha256 import sha256_digest
from sha512 import sha512_digest
import sys
from testing_suite.tester import hash, hash_sha512
from config import setup_args
from logger import log_hash
import time

def read_binary_file(filename):
    f = open(filename, mode="rb")
    chunk = f.read()
    f.close()
    return chunk


def main():
    parser = setup_args()
    args = vars(parser.parse_args())
    msg = ''
    if args['string'] is not None:
        msg = args['string']
        print(f'Hashing given string: {msg}', end='\n\n')
        
    elif args['file'] is not None:
        filename = args['file']
        if args['binary']:
            msg = read_binary_file(filename) 
        else:
            msg = open(filename).read()
        print(f'Hashing given file: {filename}', end='\n\n')
        
    else:
        print('Missing file name or string to be hashed', end='\n\n')
        parser.print_help()
        sys.exit(1)     
        
    if args['sha256']:
        expected_hash = hash(msg, args['binary'])
        calculated = sha256_digest(msg).hex()
        log_hash(calculated)
        ans = expected_hash == calculated
        print('Verifying hash: ', ans)
    elif args['sha512']:
        expected_hash = hash_sha512(msg, args['binary'])
        calculated = sha512_digest(msg).hex()
        log_hash(calculated)
        ans = expected_hash == calculated
        print('Verifying hash: ', ans)
    else:
        print("Flag or algo doesnt exist, contact the owner of the repo")
    
    
if __name__ == "__main__":
    start_time = time.time()
    main()
    print(f'Time Taken: {time.time() - start_time}')
    