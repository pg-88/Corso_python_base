# import 


def main():
    # saluto = input("Come vuoi essere salutato?\n")

    # nome = input("Come ti chiami?\n")

    # print(saluto + nome)

    # carattere_iniziale = "La tua iniziale è: " + nome[0]
    
    # carattere_finale = "L'ultimo carattere del tuo nome è: " + nome[-1]

    # print(nome[1:])


    # stringa_base = "aaa bbb ccc ddd eee"

    # print(stringa_base[::4])
    # numerone = 45_000_000_000
    

    # print(carattere_iniziale, carattere_finale, nome[-2])


    numero_iniziale_str = input("scegli un numero\n")

    print("Tipo di dato di input", type(numero_iniziale_str))

    if type(numero_iniziale_str) is str:
        numero_iniziale_int = int(numero_iniziale_str)

    print(isinstance(numero_iniziale_int, int))


    print("Dimmi il quadrato del numero", numero_iniziale_int)
    
    risposta_str = input("Scrivi qui la tua risposta\n")
    risposta_int = int(risposta_str)

    if risposta_int == numero_iniziale_int ** 2:
        print("Grande conosci i quadrati ")
    else:
        esito_str = "Errore, il quadrato di {} non è {} ma è {}".format(numero_iniziale_int, risposta_int, numero_iniziale_int ** 2)
        print(esito_str)

if __name__ == '__main__':
    main()