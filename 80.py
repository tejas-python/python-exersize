# advance password checkker
#Create a program that asks the user to enter a new password and check that the submitted password should contain at least one number, one uppercase letter, and at least 5 characters. If the conditions are met, print out the reason why pointing to the specific condition/s that has not been satisfied.

while True:
    notes =[]
    Password = input("enter the password :")
    if not any([s.isupper() for s in Password]):
        notes.append("password dosenot have a upper case letter")
        
    if  not any([s.isdigit() for s in Password]):
        notes.append("password dosenot contain a number")

    if  not  len(Password) >=5:
        notes.append("password is not greater than 5 characters")

    if len(notes) ==0:
        print("the password is strong")
        break
    else:
        print("pleas check the following")
        for i in notes:
            print(i)
