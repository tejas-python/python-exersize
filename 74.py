# Question: Please concatenate this file with this one to a single text file. The content of the output file should look like below.

import pandas as pd
data1=  pd.read_csv('https://pythonhow.com/media/data/sampledata.txt')
data2 = pd.read_csv('https://pythonhow.com/media/data/sampledata_x_2.txt')
frames = [data1,data2]

result = pd.concat(frames)
print(result)
result.to_csv('sampele2.csv',index=None)
