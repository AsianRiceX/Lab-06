def enc(password):
    temp_pass = ""
    for x in range(len(password)):
        temp_pass += str(int(password[x]) + 3)
    print("Your password has been encoded and stored!")
    return temp_pass
