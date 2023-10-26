def validUTF8(data):
    num_bytes_to_follow = 0

    for byte in data:
        if num_bytes_to_follow == 0:
            if byte >> 5 == 0b110:
                num_bytes_to_follow = 1
            elif byte >> 4 == 0b1110:
                num_bytes_to_follow = 2
            elif byte >> 3 == 0b11110:
                num_bytes_to_follow = 3
            elif byte >> 7 == 0:
                num_bytes_to_follow = 0
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            num_bytes_to_follow -= 1
    
    return num_bytes_to_follow == 0
