def encode(password):
    temp_pass = ""
    for x in range(len(password)):
        temp_pass += str(int(password[x]) + 3)
    print("Your password has been encoded and stored!")
    return temp_pass


def decode(password):
    return -1


def main():
    print("-------------\n1. Encode\n2. Decode\n2. Decode\n")
    user_choice = int(input("Please enter an option: "))
    encoded_pass = ""
    user_pass = ""
    if user_choice == 1:
        user_pass = input("Please enter your password to encode: ")
        encoded_pass = encode(user_pass)
    elif user_choice == 2:
        decoded_pass = decode(encoded_pass)
        print("")
    elif user_choice == 3:
        exit()
