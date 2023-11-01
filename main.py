import encode
import decode


def main():
    # placeholders
    encoded_pass = ""
    decoded_pass = ""
    while True:
        print("-------------\n1. Encode\n2. Decode\n3. Quit\n")
        user_choice = int(input("Please enter an option: "))
        # encode a password using another file
        if user_choice == 1:
            user_pass = input("Please enter your password to encode: ")
            encoded_pass = encode.enc(user_pass)
        # decode an encoded password using another file
        elif user_choice == 2:
            decoded_pass = decode.dec(encoded_pass)
            print("The encoded password is " + encoded_pass + ", and the original password is " + decoded_pass + ".")
        # exit the code
        elif user_choice == 3:
            exit()


if __name__ == '__main__':
    main()
