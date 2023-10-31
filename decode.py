
# Sam Morsics's decode function
def decode(encoded_password):
    decoded_password = ""

    for num in encoded_password:
        decoded_password += str((int(num) - 3))

    return decoded_password