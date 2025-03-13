#Zamienić wszystkie litery o na 0, e na 3, i na 1, a na 4 w podanej przez użytkownika sentencji.

sentence = input("podaj sentencję: ")
sentence = sentence.replace('o','0')
sentence = sentence.replace('e','3')
sentence = sentence.replace('i','1')
sentence = sentence.replace('a','4')
print(sentence)