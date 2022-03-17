# Question: Create a script that generates a file where all letters of the English alphabet are listed two in each line. The inside of the text file would look like:
#
# ab
# cd
# ef
#
# and so on.
import string
with open("togetheralpga.txt",'w') as file:
    letter = list(string.ascii_lowercase)
    for i in range(0,len(letter),2):
        file.write(''.join(letter[i-2:i])+'\n')
print("done")
