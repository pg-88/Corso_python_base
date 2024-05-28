from math import pi, tau
from random import randint


"""Funzione che calcola area e perimetro del cerchio e ritorna come tupla"""

def area_perimetro_cerchio(raggio: float) -> tuple[float, float]:
    """Ritorna tupla con (AREA, PERIMETRO) """

    return (pow(raggio, 2) * pi, raggio * tau)

# print(area_perimetro_cerchio(2))

(a , p) = area_perimetro_cerchio(2)
# print(a, p)


"""Ordinamento dictionary"""

"""Vedere esercizio su dizionari.py"""
testo_esempio = """Mi chiamo Sofia. Ho 35 anni. Mio marito si chiama Alessandro e ha 36 anni. La mia famiglia è composta in tutto da cinque persone. Io e mio marito abbiamo tre figli.

Viviamo in un piccolo paese di campagna, in una bella casa con un cortile. I nostri tre figli si chiamano Andrea, Martina e Giacomo. Andrea frequenta l'asilo, Martina e Giacomo frequentano le scuole elementari. I miei tre figli amano giocare a tanti giochi diversi nel cortile.

I genitori di mio marito vivono lontano da qui, in città. I miei genitori invece abitano vicino a noi, nello stesso paese. Vogliono molto bene ai nostri tre figli e spesso si occupano di loro.

Vicino a noi abita mia sorella Giulia con la sua famiglia. I miei figli giocano spesso con Marta, la figlia di Giulia.

Io sono una casalinga che lavora inoltre a casa come articolista. Mio marito è invece un operaio. È una persona molto buona e gioca spesso con i suoi tre figli. Sono molto felice della mia famiglia! """

def ferquenza_parole(testo: str):
    testo = testo.lower()
    for c in ".,;:_-?'!":
        testo = testo.replace(c, ' ')
    lista_stringhe = testo.split()


    frequenze = {}

    for parola in lista_stringhe:
        frequenze[parola] = frequenze.get(parola, 0) + 1
        # print(parola)
    return frequenze

freq_dict = ferquenza_parole(testo_esempio)

print(freq_dict.items())

""" freq_dict è il nostro dizionario con le frequenze, 
1) ordiniamo il dizionario in modo che le parole siano in ordine alfabetico
2) ordiniamo il dizionario in ordine decrescente secondo la frequenza
"""

# 1)
alfa_list = sorted(freq_dict.items())
# print(alfa_list) # risultato come lista
# print(dict(alfa_list)) # risultato come dict

# 2)
"""
la tupla può essere ordinata solo per il primo elemento 
quindi devo invertire l'ordine degli elementi di items
"""
tmp = [] # lista con gli elementi invertiti

for (k, v) in freq_dict.items():
    tmp.append((v, k))

# print(tmp)
"""
posso ora usare la funzione sorted
uso reverse=True per ordine decrescente
"""
tmp = sorted(tmp, reverse=True)
# print(tmp)

"""
riporto gli elementi della tupla al loro posto
"""

lista_decresc = []

for i, j in tmp:
    lista_decresc.append((j, i))

risultato = dict(lista_decresc)
# print(risultato)


"""SET"""

numeri1 = [randint(0,10) for i in range(50)]
numeri2 = [randint(7,30) for i in range(50)]
# print(numeri1, numeri2) # liste che contiene numeri ripetuti

insieme1, insieme2 = (set(numeri1), set(numeri2))
# print("inizialmente ", insieme1, insieme2)

print(insieme1 | insieme2)
# unione: tutti gli elementi presenti sia in insieme1 che in insieme2
print(insieme1 & insieme2)
# intersezione: insieme di valori presenti in entrambe gli insiemi
print(insieme1 - insieme2) 
# sottrazione: insieme1 senza gli elementi che sono anche in insieme2
print(insieme1 ^ insieme2) 
# esclusione: l'insieme dei numeri che non sono presenti in entrambi

"""
Dalla lista di birre estrapolare il tipo di birra e preparare un set in modo 
da vedere quante categorie di birra diverse ci sono nella lista
"""
birra = [
    "white Dog - Indian Pale Ale",
    "Heineken - Lager",
    "Guinness - Stout",
    "Corona Extra - Pale Lager",
    "Peroni - Pale Lager",
    "Leffe Blonde - Belgian Blonde Ale",
    "Moretti - Pale Lager",
    "Hoegaarden - Belgian Witbier",
    "Chimay Blue - Belgian Strong Dark Ale",
    "Sierra Nevada Pale Ale - American Pale Ale",
    "Budweiser - American Lager",
    "Stella Artois - Pale Lager",
    "Duvel - Belgian Strong Golden Ale",
    "Pilsner Urquell - Pilsner",
    "Paulaner Hefe-Weißbier - Hefeweizen",
    "Bass Pale Ale - English Pale Ale",
    "Newcastle Brown Ale - Brown Ale",
    "Samuel Adams Boston Lager - Vienna Lager",
    "Anchor Steam - California Common",
    "Köstritzer Schwarzbier - Schwarzbier",
    "Blue Moon Belgian White - Belgian-style Wheat Ale"
]
