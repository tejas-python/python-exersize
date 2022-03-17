# count no of .py file in files folder

import glob
x = glob.glob('files/*.py')
print(len(x))
 #or


file_list=glob.glob1("files","*.py")
print(len(file_list))
