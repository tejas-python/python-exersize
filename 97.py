# write the user input to a file



def update():
    file =  open("data.txt","a+")

    while True:
        data= input("Write a value: ")
        if data=='CLOSE':
             file.close()
             break
        elif data=="SAVE":
            file.close()
            file =  open("data.txt","a+")
            continue
        else:
            file.write(data+"\n")

update()
