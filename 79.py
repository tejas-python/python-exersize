# Exercise for reference:
#
# # Create a program that asks the user to enter a new password and check that the submitted password should contain at least one number, one uppercase letter, and at least 5 characters. If the conditions are generated, print out "Password is fine"; otherwise, keep prompting the user for a password.

while True:
    Password = input("enter the password :")
    if any([s.isupper() for s in Password]) and any([s.isdigit() for s in Password]) and len(Password) >=5:
        print("the password is strong")
        break
    else:
        print("pleas enter proper password")
