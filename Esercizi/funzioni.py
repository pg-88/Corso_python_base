""" Definire funzioni """


"""
scrivere una funzione che stampa a video i primi 5 numeri della successione di Fibonacci. 
La funzione non deve prendere argomenti, non deve avere ritorno, deve essere dotata 
di docstring e deve avere l'annotazione dei tipi
"""
def fibonacci_1():
    n_0 = 0
    n_1 = 1

    risultato = 0

    num_iterazioni = 5 
    for i in range(num_iterazioni - 1):
        n_0 = n_1
        n_1 = risultato
        risultato = n_0 + n_1
    print(f"Il valore della successione di fibonacci dopo {num_iterazioni} iterazioni è: {risultato}")

fibonacci_1()


"""
copiare il codice dell'esercizio sopra e creare un'altra funzione che prende come arg 
un numero intero che è il numero di valori della succesione da calcolare 
Modificare a dovere dichiarazione della funzione, docstring e blocco di codice
"""
def fibonacci_2(num_iterazioni: int):
    n_0 = 0
    n_1 = 1

    risultato = 0

    for i in range(num_iterazioni - 1):
        n_0 = n_1
        n_1 = risultato
        risultato = n_0 + n_1
    print(f"Il valore della successione di fibonacci dopo {num_iterazioni} iterazioni è: {risultato}")
    return risultato

fibonacci_2(6)

"""
in uno scatolone ci stanno 42 contenitori, devo stipare n contenitori, 
quanti scatoloni mi servono?

Scrivere una funzione che prende in input il numero di contenitori e ritorna il numero 
di scatoloni necessari
Per renderla più generale possibile possiamo definire un parametro di default
per il numero di contenitori in uno scatolone (parametro di default)
"""


"""
libreria di funzioni per un app della gestione dell'automobile

L'app girerà grazie a un loop nel main, per il momento definiamo 
le funzioni della libreria
- funzione ricorda la revisione, in funzione della data in cui 
    bisogna fare la revisione ci ritorna il numero di giorni che mancano
    se il giorno è già passato stampa anche una stringa di avviso
- ricorda tagliando km ultimo tagliando come parametro default, più 
    parametro km attuali ritorna True se dobbiamo fare il tagliando 
    False altrimenti
- calcola costo viaggio, prende km previsti, tipo strada (str), 
    prezzo medio carburante. 
    Ritorna float che rappresenta la cifra in euro
"""

"""

"""
