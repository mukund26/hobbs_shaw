def string_to_binary(msg):
    binary = []
    for ch in msg:
        binary.append(bin(ord(ch))[2:].zfill(8))
    return ''.join(binary)


def string_to_int(binary_str):
    return int(binary_str, 2)