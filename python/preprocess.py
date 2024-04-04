from utils import binary_file_to_binary_string, string_to_binary


def convert_input_to_binary_string(msg):
    
    if isinstance(msg, str):
        binary_string = string_to_binary(msg)
    elif isinstance(msg, bytes):
        binary_string = binary_file_to_binary_string(msg)
    elif not isinstance(msg, bytearray):
        raise TypeError 
    
    return binary_string