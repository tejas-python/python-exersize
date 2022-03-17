# Question: Create a script that generates a text file with all letters of the English alphabet inside it, one letter per line.
import string
with open("alpha.txt",'w') as file:
    for i in string.ascii_lowercase:
        file.write(i+'\n')
