# Create a program that asks the user to input values separated by commas and stores those values in a text file, each value in a separate line

with open('user_data.txt','a+') as file:
    data = input('enter the data: ').strip().split(',')
    for i in data:
        file.write(i+'\n')
