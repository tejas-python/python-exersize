sentence = input('enter the sentence to convert : ').strip().lower().split()
new_sentence =[]
for i in sentence:
    if i[0] in 'aeiou':
        new_sentence.append(i+"yay")
    else:
        vol_pos = 0
        for letter in i:
            if letter not in 'aeiou':
                vol_pos +=1
            else:
                break
        cons = i[:vol_pos]
        rest = i[vol_pos:]
        new_sentence.append(rest+cons+'ay')
print(" ".join(new_sentence))

