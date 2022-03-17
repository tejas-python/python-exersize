# Question: Create an English to Portuguese translation program.
#
# The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source. Also, return the message, "We couldn't find that word!" when the user enters a word that is not in the dictionary. Also, make the program non-case-sensitive, meaning that, for example, both earth and Earth should return the translation correctly for that word.

d = dict(weather = "clima", earth = "terra", rain = "chuva")
def vocabolary(word):
    if word in d:
        return d[word]
    else:
        return 'word not in dictionary .'
print(vocabolary(input("enter the word: ").strip().lower()))
