# Question: Create a function that takes a text file as input and returns the number of words contained in the text file. Please take into consideration that a comma can separate some words with no space. For example, "Hi, it's me." would need to be counted as three words. For your convenience, you can use the text file in the attachment.
import re 
def counted(file_name):
    with open(file_name) as file:
        txt = file.read()
        txt = txt.replace(",", " ")
        # string_list = re.split(",| ", txt)


    print(len(txt.split(" ")))
counted('words2.txt')
