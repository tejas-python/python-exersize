import requests
response = requests.get("http://www.pythonhow.com/data/universe.txt").text
text = response
count_a = text.count("a")
print(count_a)
