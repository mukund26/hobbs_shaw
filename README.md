> A simple SHA-2 implementation in python which gives hash for string or a file.
> It also handles byte stream.
> It calculates SHA-256 and SHA-512 at the time

# Author - Mukund Agarwal

## Usage

* Example

```python
python main.py -s "Hello World!!" --sha256
```

* For help
```python
usage: SHA-2 [-h] [--sha256] [--sha512] [-s STRING] [-f FILE]

Generate SHA256/512 hashes

options:
  -h, --help            show this help message and exit
  --sha256              Generates SHA-256 for given input (default: False)
  --sha512              Generates SHA-512 for given input (default: False)
  -s STRING, --string STRING
                        string to be hashed (default: None)
  -f FILE, --file FILE  file to be hashed (default: None)

Use help to find all supported hashes
```

## For Algo refer: [SHA-256 Wiki](https://en.wikipedia.org/wiki/SHA-2)

## For more refer:

- https://blog.boot.dev/cryptography/how-sha-2-works-step-by-step-sha-256/
- https://github.com/mukund26/softwareEnggGuide/blob/main/sha256-384-512.pdf
