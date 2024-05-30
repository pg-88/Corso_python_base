import this

def richiesta_operazione():
    op = input("Che operazione vuoi fare?")
    print(op)

def divisione(numeratore: float, denominatore: float=2) -> float:
    """stampa a video numeratore e denominatore e il risultato della divisione"""
    print(f"{numeratore} / {denominatore}  =  {numeratore / denominatore}")
    return numeratore / denominatore

def main():
    richiesta_operazione()
    divisione(9,3)
    pow(exp=3, base=9)

if __name__ == '__main__':
    main()