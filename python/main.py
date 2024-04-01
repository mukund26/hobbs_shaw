from sha256 import sha256_digest
import argparse
import sys

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
    return parser


def main(args):
    args = vars(parser.parse_args())
    msg = ''
    if args['string'] is not None:
        msg = args['string']
        print(f'Hashing given string: {msg}')
        
    elif args['file'] is not None:
        filename = args['file'] # can handle file read better 
        with open(filename) as f:
            msg += f.read()
        print(f'Hashing given file: {filename}', end='\n\n')
        
    else:
        print('Missing file name or string to be hashed', end='\n\n') # add color
        parser.print_help()
        sys.exit(1)     
        
    if args['sha256']:
        log_hash(sha256_digest(msg).hex())
    elif args['sha512']:
        print("Working on SHA512")
    else:
        print("Flag or algo doesnt exist, contact the owner of the repo")
    
if __name__ == "__main__":
    parser = setup_args()
    main(parser)
    