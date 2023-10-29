import random

char = "abcdefghijklmnopqrstuvwxyz123456789@#$%^&*_-<>?"

while 1:
    password_len = int(input("Length of desired password :"))
    password_count =int(input("Desired ammounts of passwords :"))

    for x in range(0, password_count):
        password = ""
        for x in range(0, password_len):
            password_char = random.choice(char)
            password      = password + password_char
        print("Password Result :", password)
    break
