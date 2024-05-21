from random import random, randint

"""Creare una funzione che ritorni una lista dei numeri pari fino al numero massimo passato come argomento"""


"""creare una funzione che ritorni una lista con una tabellina. Passare come arg il numero di cui si vuole
costruire la tabellina e il numero di fattori da calcolare.
Bonus: come effetto collaterale stampare a teminale la stringa con l'operazione eseguita, esempio "2 x 4 = 8" """


"""
Funzione che aggiorna una lista. La lista numeri segue un preciso schema di inserimento, nella prima parte si trovano solo numeri 
pari mentre nella seconda parte solo numeri dispari. Scrivere la funzione per aggiornare la lista.
"""

numeri = [2, 6, 42, 128, 3, 7, 11, 57]

def aggiorna_numeri(n: int) -> None:
    pass

numero_nuovo = randint(0, 100)

aggiorna_numeri(numero_nuovo)
print("Lista aggiornata ", numeri)



"""
La lista nomi riporta in ordine di classifica generale i corridori del giro 2023.
La lista nazioni riporta seguendo lo stesso ordine, le loro nazionalità.
Produrre una lista chiamata classifica che riporti numero di posizione, nome del corridore, nazionalità
"""

nomi = [
    "Primož Roglič", 
    "Geraint Thomas", 
    "João Almeida", 
    "Damiano Caruso", 
    "Thibaut Pinot", 
    "Thymen Arensman", 
    "Eddie Dunbar", 
    "Andreas Leknessund",
    "Lennard Kämna",
    "Laurens De Plus"
    ]

nazioni = ["slo", "gb", "pt", "it", "fr", "nl", "ir", "no", "de", "be"]


""" dal testo di lorem ipsum, effettuare uno split e contare le parole contenute.

Lo split è un metodo delle stringhe che permette di dividere stringe nel momento in cui si incontra un certo carattere.
Lo split restituisce una lista di stringhe generata dalla stringa iniziale.
"""

lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

"""
Sempre a partire dal lorem creare una lista in cui ogni elemento è il numero di vocali contenuti nella parola del lorem.
Se lo facciamo sotto forma di funzione possiamo applicare a qualsiasi stringa.
"""
