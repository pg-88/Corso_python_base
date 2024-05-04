"""utilizzando solo operatori aritmetici, estrapolare il numero di 
giorni, ore, minuti, secondi dall'output della funzione time"""

from time import time

tempo = time() # variabile tempo contiene l'output della time()

giorni = 0 # variabile in cui si deve inserire il valore (int) deì giorni

ora = 0 # variabile in cui si deve inserire il valore (int) dell'ora

# hint: un'ora sono 3600 secondi, un girono sono 3600 * 24 secondi

giorni = tempo / (3600 * 24)

print(int(giorni))

print(
    "più o meno ", 
    giorni // 365, 
    " dall'inizio dell'epoca da cui parte a contare la fz time()"
    )
