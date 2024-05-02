from pathlib import Path
import os



class PercorsoScaricati:
    """individua il percorso della cartella scaricati"""

    def __init__(self) -> None:
        home = Path().home()
        self.__cartella = home.joinpath("Download")

        try:
            open(self.__cartella)
        except FileNotFoundError as err:
            print("cartella non trovata ", err)
        try:
            self.__cartella = home.joinpath("Scaricati")
        except FileNotFoundError as err:
            print("Cartella non trovata, indicare il nome:\n")
            nome_cartella = input("La cartella deve trovarsi nella home utente\n")
            self.__cartella = home.joinpath(nome_cartella)
        finally:
            print("Cartella Scaricati", self.__cartella)

    @property
    def iteratore_files(self):
        return os.scandir(self.__cartella)
    
    @property
    def percorso_scaricati(self):
        return self.__cartella.resolve()


class Struttura:
    """Analizza i file nella cartella individuata 
    e crea una cartella per ogni estensione"""

    def __init__(self, scricati: PercorsoScaricati) -> None:
        with scricati.iteratore_files as files:
            self.__path_scaricati = scricati.percorso_scaricati
            self.__estensioni = set()
            for item in files:
                if item.is_file():
                    filename, ext = os.path.splitext(item)

                    if ext and ext[0] == '.': # se il primo carattere è un punto
                        ext = ext[1:] # escludo il primo carattere

                    # print("Nome", filename, "estensione", ext)
                    self.__estensioni.add(ext)  # aggiorno estensioni        

    @property
    def estensioni(self):
        return self.__estensioni
    
    def crea_sottocartelle(self, *arg):
        """crea sottocartelle per ogni estensione o solo per quelle passate"""

        if arg:
            self.__estensioni = arg # ridefinisco estensioni

        for ext in self.__estensioni:

            if ext == '':
                ext = "Nessuna_estensione"

            try:
                os.mkdir(Path.joinpath(self.__path_scaricati, ext).resolve())
            except FileExistsError:
                print(f"Cartella {ext} già presente, nulla da fare")


class Organizzatore:
    """sposta i file nelle cartelle appropriate"""
    def __init__(self, strutt: Struttura, percorso: PercorsoScaricati) -> None:
        self.__s = strutt
        self.__p = percorso
        self.organizza_file()

    def organizza_file(self):
        with self.__p.iteratore_files as files:
            for f in files:
                _, ext = os.path.splitext(f)
                if ext and ext[0] == '.':
                    if ext[1:] in self.__s.estensioni:
                        try:
                            os.rename(
                                Path(f.path).absolute(), 
                                Path().joinpath(self.__p.percorso_scaricati, ext[1:], f.name)
                            )
                        except FileExistsError:
                            print("File già presente")



def organizza_in_cartelle(*estensioni):
    p = PercorsoScaricati()  # inizializzo l'oggetto che gestisce i percorsi
    s = Struttura(p)  # inizializzo l'oggetto che crea la struttura delle cartelle
    s.crea_sottocartelle(*estensioni) # definisco quali cartelle creare
    o = Organizzatore(s, p)  # inizializzo l'organizzatore 


def main():
    """funzione principale invoca le altre"""

    organizza_in_cartelle("pdf", "deb")


if __name__ == '__main__':
    main()
    