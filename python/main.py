from sha256 import sha256_digest
import argparse
import sys
from hobbs_shaw.python.testing_suite.tester import hash

def log_hash(hash):
    print("Hash for the given input:")
    print()
    print("************************")
    print()
    print(hash)
    print()
    print("************************")


def setup_args():
    parser = argparse.ArgumentParser(
                    prog='SHA-2',
                    description='Generate SHA256/512 hashes',
                    epilog='Use help to find all supported hashes',
                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument("--sha256", action='store_true', help="Generates SHA-256 for given input")
    parser.add_argument("--sha512", action='store_true', help="Generates SHA-512 for given input")
    parser.add_argument("-s", "--string", help="string to be hashed")
    parser.add_argument("-f", "--file", help="file to be hashed")
    parser.add_argument("-b", "--binary", action='store_true', help='flag for binary file')
    parser.add_argument("-t", "--test", action='store_true', help='Test accuracy of algorithm')
    parser.add_argument("-p", "--perf", action='store_true', help='Log performance of the algorithm')
    return parser


def read_binary_file(filename):
    f = open(filename, mode="rb")
    chunk = f.read()
    f.close()
    return chunk


def main(args):
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
        print("Working on SHA512")
    else:
        print("Flag or algo doesnt exist, contact the owner of the repo")
    
if __name__ == "__main__":
    parser = setup_args()
    main(parser)
    