# Question: Please download the attached countries-raw.txt file. The file contains the list of country names, but it also contains some unnecessary text among the countries.
#
# Please clean the list with Python by generating a new text file that contains a flawless list of country names without any other text or brake lines in it. The new file content should look like in the expected output.
with open("countries_raw.txt",'r') as file:
    content = file.readlines()
content =     [i for i in [i for i in [i for i in [i.strip("\n") for i in content if "\n" in i]  if i !=""] if 1 !="Top of Page"] if len(i) != 1]
with open("clean _countrie.txt",'w') as file:
    for i in content:
        file.write(i+'\n')
