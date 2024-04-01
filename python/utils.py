def string_to_binary(msg):
    binary = []
    for ch in msg:
        binary.append(bin(ord(ch))[2:].zfill(8))
    return ''.join(binary)


def string_to_int(binary_str):
    return int(binary_str, 2)


def fill_zeros(n):
    # x = 0
    # add filler zeros such that (l + 1 + k + 64) % 512 == 0
    # while (l + x + 64) % 512 != 0:
    #     binary_string += '0'
    #     x += 1
    return '0' * n


def create_blocks(binary_string, block_size = 512):
    blocks = []
    for i in range(0, len(binary_string), block_size):
        blocks.append(binary_string[i : i + block_size])
    return blocks