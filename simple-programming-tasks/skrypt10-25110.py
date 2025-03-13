#Napisz program, który korzystająć z metody chr()
# wygeneruje łańcuch znakowy z alfabetem,
#  czyli 'abc....xyz'. Do pliku alfabet1-numeralbumu.txt
#  zapisz wygenerowany łańcuch znakowy, a do pliku alfabet2-numeralbumu.txt
#  zapisz litery z ww. łańcucha znakowego, tylko że każda litera ma się znaleźć w osobnej linii w pliku.
#Hint: oprócz funkcji write() skorzystaj również z menadżera kontekstu with, żeby nie zapomnieć o zamknięciu pliku.

litery_int = [x+97 for x in range(26)]
litery = [str(chr(x)) for x in litery_int]

with open("alfabet1-25110.txt", 'w') as plik:
    [plik.write(x) for x in litery]


with open("alfabet2-25110.txt", 'w') as plik:
    litery_nl = [x+"\n" for x in litery]
    [plik.write(x) for x in litery_nl]