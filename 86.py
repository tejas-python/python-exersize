# Question: Please take a look at the following list:
#
# checklist = ["Portugal", "Germany", "Munster", "Spain"]
#
# One of the items is not a country. Please use Python and the file containing the list of countries (attached) as the data source to filter out the checklist  of non-country items. Once you have filtered out checklist , then print it out.

checklist = ["Portugal", "Germany", "Munster", "Spain"]
with open('clean _countrie.txt','r') as file:
    content = file.readlines()

content = [i.rstrip('\n') for i in content]
for i in checklist.copy():
    if i in content:
        pass
    else:
        checklist.remove(i)
print(checklist)
# or checked = [i for i in content if i in checklist]

# print(checked)
