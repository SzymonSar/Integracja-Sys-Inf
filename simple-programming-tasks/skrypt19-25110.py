#Sprawdź czy wyraz bądź zdanie podane przez użytkownika jest palindromem.

zdanie = input("podaj zdanie: ")
if zdanie == zdanie[::-1]:
    print("Jest palindromem")
else:
    print("Nie jest palindromem")