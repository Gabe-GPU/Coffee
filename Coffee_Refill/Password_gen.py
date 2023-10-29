import random
#setting character values 
char = "abcdefghijklmnopqrstuvwxyz1234567890@#$%^&*_-<>?"

# create inputs for length and character values for the user 
while 1:
    password_len = int(input("Length of desired password :"))
    password_count =int(input("Desired ammounts of passwords :"))

#for loops that parse through character list in order to fetch data 
    for x in range(0, password_count):
        password = ""
        for x in range(0, password_len):
            password_char = random.choice(char)
            password      = password + password_char

#print satement that will print values for generated passwords
        print("Password Result :", password)

# will break out of the lopp so the script can run 
    break
