# Question: Create a program that, once executed the programs prints Hello  instantly first, then it prints it after 1 second, then after 2, 3, and then the program prints out the message "End of the Loop" and stops.

from time import sleep
i =0
while i<4:
    print("hello")
    sleep(i)
    i+=1
print("End of loop")

# or
i=0
while True:
    if i >3: break
    print("hello")
    sleep(i)
    i+=1
print("End of loop")
