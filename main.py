def main():
    print("-------------\n1. Encode\n2. Decode\n2. Decode\n")
    user_choice = int(input("Please enter an option: "))
    encoded_pass = ""
    user_pass = ""
    if user_choice == 1:
        user_pass = input("Please enter your password to encode: ")
        for x in range(len(user_pass)):
            encoded_pass += str(int(user_pass[x]) + 3)
        print("Your password has been encoded and stored!")
    elif user_choice == 2:
        print("The encoded password is " + encoded_pass + ", and the original password is " + user_pass)
    elif user_choice == 3:
        exit()
