"""Vediamo alcuni esempi con float e int
float e int non sono propriamente funzioni ma in realtà servono per 
generare oggetti qunidi sono il costruttore di una classe
Per quello che ci riguarda in questa fase le usiamo come funzioni.
Infatti si comportano esattamente come funzioni che hanno un ritorno

Inoltre vediamo un altro esempio da una libreria molto utilizzata: time
per poter usare la funzione time dobbiamo importarla. Non preoccupiamoci 
troppo per la sintassi di importazione, la vedremo più avanti in dettaglio
"""

from time import time  # importazione della fz time dalla libreria time

float("3.14") # "3.14" è una stringa, float prova a convertire in numero con virgola

# eseguendo il codice sopra cosa mi aspetto di vedere a terminale?

# prendo il riotorno della funzione e lo caccio dentro una variabile

il_mio_float = float("3.14")

print("il mio float: ", il_mio_float)
# adesso lo vedo!

string_int = "1992"

il_mio_int = int(string_int)

print("il_mio_int", il_mio_int)

print("Che ore sono?", time())
# per capire come si comporta la funzione ho bisogno di aiuto 
help(time)



