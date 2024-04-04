import argparse

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