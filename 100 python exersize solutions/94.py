# Question: Please download the attached urls.txt file. The file contains some broken URLs. Here's what the file contains:
#
# https:/www.google.com
# https:/www.yahoo.com
# https:/www.stackoverflow.com
# https:/www.pythonhow.com

with open("urls.txt",'r') as file:
    content = file.readlines()
content = [i.replace("s","") for i in content]
with open('urls_corrected.txt','w') as file:
    for url in content:
        fin_url = url[:6] +"/"+url[6:]
        file.write(fin_url)
print('done')
