#Używając pętli dodawaj do wcześniej zadeklarowanej tabeli
#  liczby z przedziału od 1 do 100, które są podzielne przez 3 lub podzielne przez 5.

tabela = []
for x in range(100):
    if (x+1)%3==0 or (x+1)%5==0:
            tabela.append(x+1)
print(tabela)