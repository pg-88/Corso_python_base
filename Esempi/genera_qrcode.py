from PIL import Image
import qrcode as qr
import argparse

parser = argparse.ArgumentParser(
    description='Genera immagine di un qrcode',
    epilog="""\n
    Autore Pietro Grigolo;
    se trovi bug o vuoi segnalare problemi scrivi a grigolopi@gmail.com
    """,
    add_help=True # invocando lo script con il flag --help
)
# positional argument per passare una stringa che deve diventare il contenuto qrcode
parser.add_argument("--contenuto", action="store")
parser.add_argument("--nome", action="store")

a = parser.parse_args()
print(a.nome, a.contenuto, type(a))

img = qr.make(a.contenuto)
img.save(f"{a.nome}.png")

"""Come si usa:
Da terminale a riga di comando, dopo il comando per lanciare python 
(da me python3, potrebbe essere python o py) seguito dal nome di questo file
sul vostro sistema operativo (genera_qrcode.py se non lo cambiate...).
Inoltre lo script ha bisogno di 2 argomenti che non vengono chiesti in fase di
esecuzione con input come abbiamo visto a lezione ma vanno passati con dei flag.
Esempio di esecuzione:
python3 genera_qrcode.py --contenuto "https://www.python.org/" --nome "python_logo"

Possibili fonti di errore:
1. controllare la cartella da cui stiamo lanciando il comando
2. nome del file eseguibile che contiene lo script
3. passare gli argomenti nel modo corretto, prima va il flag poi il valore dell'argomento.
    Non importa l'ordine dei flag ma ci devono essere
4. installare le librerie! comando da terminale:
pip install qrcode pillow
"""

""" 
Idee per espandere l'esempio: 
1. controllo input contenuto ed eventuale gestione errori se argomento non passato
2. gestione del caso in cui non venga passato il nome, anziché bloccare esecuzione
    assegnare un nome di default.
3. Aggiungere un immagine al centro del qrcode 
    https://www.geeksforgeeks.org/how-to-generate-qr-codes-with-a-custom-logo-using-python/
"""