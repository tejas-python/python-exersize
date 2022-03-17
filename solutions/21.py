# Question: Filter the dictionary by removing all items with a value of greater than 1.

d = {"a": 1, "b": 2, "c": 3}
d = {i:j for i,j in d.items() if j<=1}
print(d)
