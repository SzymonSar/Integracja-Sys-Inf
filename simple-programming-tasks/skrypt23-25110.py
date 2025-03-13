#Za pomocą pętli stworzyć 1000 losowych 6 znakowych wyrazów
#  [A-Z][a-z][0-9] i zapisać je do pliku passwords.txt.
import random
import string
characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
slowa = []
for x in range(1000):
    slowa.append(''.join(random.choice(characters) for x in range(6)))
print(slowa)
with open("passwords.txt",'w') as plik:
    #tutaj kontynuacja