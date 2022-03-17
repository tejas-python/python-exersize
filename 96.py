# write the user input to a file
file =  open("userchat.txt","a+")



def update():
    while True:
        data= input("Write a value: ")
        if data=='CLOSE':
             file.close()
             break
        file.write(data+"\n")

update()
