"""Con un ciclo for contare quanti sono gli spazi della stringa prova"""

spazi = 0
STRINGA_PROVA = """Sequi eveniet aspernatur aut totam. 
Et non neque ut quod. Autem repellat nostrum voluptatum 
repellendus asperiores saepe. Provident doloribus ducimus deleniti sit nisi maiores.…"""
for i in STRINGA_PROVA:
    print(i)

print(spazi)

"""Trovare il numero di vocali nella stringa prova """


"""Con i cicli for, creare una stringa di n_colonne e n_righe che contenga solo punti"""
stringa = "" 

for i in range(0,10):
    for j in range(1,10):
        stringa += "." 

    stringa += f"riga{i}" + '\n'

print(stringa)