def main():
    print("-------------\n1. Encode\n2. Decode\n2. Decode\n")
    user_choice = int(input("Please enter an option: "))

    if user_choice == 1:
        user_pass = input("Please enter your password to encode: ")
        print("Your password has been encoded and stored!")
    elif user_choice == 2:
        print("")
    elif user_choice == 3:
        exit()
