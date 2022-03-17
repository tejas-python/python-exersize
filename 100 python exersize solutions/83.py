# Question: Write a script that detects and prints out your monitor resolution.

from screeninfo import get_monitors
print("width : {}, height : {}".format(get_monitors()[0].width,get_monitors()[0].height))
