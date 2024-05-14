from datetime import datetime


"""
Slicing [start:stop:step]
"""

print("Ma la volpe col suo balzo ha raggiunto il quieto fido"[0:26])
print("0123456789012345678901245"[0:12:2])


stringa_base = "aaa bbb ccc ddd eee"

stringa_base[0:3]
# risultato slicing: "aaa"

stringa_base[::4]
# risultato slicing: "abcd"


nome = "Pietro"

saluto = "Hello"

saldo = 3.14

'''Formattazione delle stringhe'''

stringa_finale = "Saluti\n%s %s" %(nome, saluto)
print(stringa_finale)


stringa_finale = "Saluti\n{1} {0}".format(nome, saluto)
print(stringa_finale)

stringa_finale = f"Saluti\n{nome} {saluto}"
print(stringa_finale)

print("%s %s, il suo saldo è di %f \n" %(saluto, nome, saldo))
print(f"{saluto} {nome}, il suo saldo è di {saldo:3.5f}\n")
print("{0} {1}, il suo saldo è di {2:0.1f}\n".format(saluto, nome, saldo))

## if statement nelle stringhe
n = 41
str_1 = f"in numero selezionato è {n}; {'''il senso della vita, dell'universo e tutto quanto''' if n == 42 else ''}"
print(str_1)

adesso = datetime.now()
print(adesso, type(adesso))
# help(datetime)
"""Formattazione del tipo di dato datetime"""

print(f"Oggi è {adesso:%A}\nData: {adesso:%d}/{adesso:%m}/{adesso:%Y}")
print(f"Orario: {adesso:%H}:{adesso:%M}")
