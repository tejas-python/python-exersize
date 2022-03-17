# Question: Create a script that asks the user to enter their age, and the script calculates the user's year of birth and prints it out in a string like in the expected output. Please make sure you generate the current year dynamically.

import datetime
year = datetime.datetime.now().year
age = int(input("Enter your age : "))
print("We think you were born back in {} ".format(int(year)-age))
