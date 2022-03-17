from xml.dom import UserDataHandler


names = ['ironman','hulk','hawkeye','ultron','captainameria','black panther','thanos']
print("Welcome to travis system")
while True:
    print("welcome user")
    user= input('ENter your name: ').strip()
    if user.lower() in names:
        print("welcome user {}".format(user))
        remove = input("do u want me to remove u: (y/n) ")
        if remove.lower() =='y':
            names.remove(user)
            print("sucessfuly removed")

        else:
            print("thanks for ur response")
    else:
        print("i haven't met you yet {}".format(user))
        add_user = input("Do u want to get added: y/n ")
        if add_user.lower() == 'y':
            names.append(user)
            print('welcome {} u have been added succesfully'.format(user))
        else:
            print("thanks for contacting will be waiting to add you when u are ready")
            

