from datetime import date
import sys

def giorni_alla_revisione(data_revisione: date) -> int:
    """prende la data in cui va fatta la revisione 
    ritorna i giorni come int, che mancano alla 
    revisione.
    Se la revisione è scaduta ritorna int negativo 
    che rappresenta i giorni passati dalla scadenza 
    """
    pass

def necessita_tagliando(
        km_attuali: int, 
        km_ultimo_tagliando: int, 
        km_freq_tagliando: int = 10_000
        ) -> bool:
    """
    km_attuali : chilometri percorsi dalla macchina 
    km_ultimo_tagliando: chilometri percorsi all'ultimo tagliando
    km_freq_tagliando: int = 10_000 ogni quanto va fatto il tagliando
 
    ritorna True se è ora di tagliando, false altrimenti
    """
def costo_viaggio(
        km_viaggio: int, 
        strade: str, 
        prezzo_carburante: float = 1.7812, 
        km_per_litro: float = 19.1
        ) -> float:
    """
    km_viaggio: int km previsti 
    strade: str tipo di strada (autostrada, urbano, extraurbano)
    prezzo_carburante: float = 1.7812 
    km_per_litro: float = 19.1 consumi medi dell'auto 

    in funzione del tipo di strada aumenta con un coefficiente il 
    consumo al km
    ritorna il costo in euro del viaggio 
    """
    pass

def main():
    pass

if __name__ == '__main__':
    print(sys.argv[0], sys.argv[1])
    
