# Question: Create a script that generates a file where all letters of the English alphabet are listed three in each line. The inside of the text file would look like:
#
# abc
# def
# ghi
#
# and so on.
import string
with open("abc.txt",'w') as file:
    letter = list(string.ascii_lowercase)
    for i in range(0,len(letter),3):
        file.write("".join(letter[i-3:i])+'\n')
