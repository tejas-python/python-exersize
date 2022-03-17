#get letters from text file and make it as list
import glob
x = glob.glob('letters/*.txt')
letters =[]
for path in x:
    with open(path) as file:
        letters.append(file.read())

print(letters)
