with open('users.txt','r') as file:
    names = file.read().split()
print(names)
def pass_checker():
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
def username():
    while True:
        username = input("enter the user name :")
        if username in names:
            print('name already exists')
            continue
        else:
            print('welcome user {} please enter password'.format(username))
            break
username()
pass_checker()
