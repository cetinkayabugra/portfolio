#!/usr/bin/env python3

if __name__ == '__main__':
    pass

BAD_PASSWORD = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']


password_1 = input("Enter password")
password_2 = input("Enter password")





if 8 <= len(password_1) <= 16:
    


    if password_1 == password_2:
        if password_1 in BAD_PASSWORD:
            print("Bad password choose another")
        else:
            print("password set")
        

    else:
        print("password do not match, TRY AGAIN")





else:
    print("Password length should be between 8 and 16 chars")
        

