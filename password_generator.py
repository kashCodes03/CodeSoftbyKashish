import string
import random

s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation

while True:
    length = input("Enter the password length = ").lower()
    print("for exiting the program write exit in length section")
    if length.isdigit():
        length=int(length)
        s = []
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))


        random.shuffle(s)
        print("your password is : ")
        print("".join(s[0:length]))

    elif length == "exit":
        print("exiting the program!")
        exit()
    
        
    else:
        print("invalid statement!")
        break
    





