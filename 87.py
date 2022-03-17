## add missing list to the coutry missing file

checklist = ["Portugal", "Germany", "Munster"]
with open("countries_missing.txt",'r+') as file:
    file.seek(0,2)
    for i in checklist:
        file.write(i+'\n')
