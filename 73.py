import pandas
# Create a script that reads this file, multiplies its values by two, and saves the output in a new text file.
data = pandas.read_csv("https://pythonhow.com/media/data/sampledata.txt")
data_2 = data * 2
data_2.to_csv("sampledata_x_2.txt", index=None)
