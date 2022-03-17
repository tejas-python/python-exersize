email = input('enter your email: ').strip()

username = email[:email.index('@')]
domain = email[email.index('@')+1:]

out = "your user name is {} and domain is {}".format(username,domain)
print(out)


