# Question: Please download the words1.txt file from the attachment and then create a Python function that takes a text file as input and returns the number of words contained in the text file.

with open('words1.txt') as file:
    txt = file.read()
    print(len(txt.split(" ")))
# print(len(handle.readline().split()))
# print(len(handle.split()))
