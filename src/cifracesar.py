funct = lambda x: 2*x + 1
def cifra(word,x):
    new_word = ""
    count = 0
    for i in word:

        new_word = new_word + chr(ord(i) + funct(x+count))
        count = count + 1
    return new_word

print(cifra("abc", 1))


#a->d = 4(somou 3)
#b->g = 7(somou 5)
#c->j = 10(somou 7)
