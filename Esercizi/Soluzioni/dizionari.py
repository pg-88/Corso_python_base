""" Usando nomi e nazioni della classifica del giro 2023, creare un dizionario che abbia per chiave il nome dell'atleta e come valore la nazionalità"""


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



""" Dictionary Comprehension, creare dictionary con chiave il nome dell'atleta e come valore la nazionalità"""


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

{ k:v for k,v in zip(nomi, nazioni)}


"""Creare un dizionario che abbia come chiave il nome dell'atleta e come valore un dizionario che contenga:
Posizione: numero in classifica,
nazionalità: sigla nazione"""

ciclisti = {}

for i in range(len(nomi)):
    ciclisti[nomi[i]] = {
        "Giro_2023": i + 1,
        "Nazione": nazioni[i]
    }

print(ciclisti.items())

"""Da questo testo esempio, contare quante parole ci sono e con quanta frequenza si ripetono all'interno del testo.
Utilizzare un dizionario le cui chiavi saranno le parole e i valori saranno le frequenze."""

testo_esempio = """Mi chiamo Sofia. Ho 35 anni. Mio marito si chiama Alessandro e ha 36 anni. La mia famiglia è composta in tutto da cinque persone. Io e mio marito abbiamo tre figli.

Viviamo in un piccolo paese di campagna, in una bella casa con un cortile. I nostri tre figli si chiamano Andrea, Martina e Giacomo. Andrea frequenta l'asilo, Martina e Giacomo frequentano le scuole elementari. I miei tre figli amano giocare a tanti giochi diversi nel cortile.

I genitori di mio marito vivono lontano da qui, in città. I miei genitori invece abitano vicino a noi, nello stesso paese. Vogliono molto bene ai nostri tre figli e spesso si occupano di loro.

Vicino a noi abita mia sorella Giulia con la sua famiglia. I miei figli giocano spesso con Marta, la figlia di Giulia.

Io sono una casalinga che lavora inoltre a casa come articolista. Mio marito è invece un operaio. È una persona molto buona e gioca spesso con i suoi tre figli. Sono molto felice della mia famiglia! """

def ferquenza_parole(testo: str):
    lista_stringhe = testo.split()

    frequenze = {}

    for parola in lista_stringhe:
        parola = parola.strip().lower()
        if parola.endswith(('.', ',', ':', '!', '?')):
            parola = parola[:-1]
        frequenze[parola] = frequenze.get(parola, 0) + 1
        # print(parola)
    return frequenze

print(ferquenza_parole(testo_esempio).items())