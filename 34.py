# line saying that c  is not defined. Please fix the function so that there is no error and the  last line can print out the value of c  (i.e. 1 ).

# def foo():
#     c = 1
#     return c
# foo()
# print(c)

def foo():
    global c
    c = 1
    return c
foo()
print(c)
