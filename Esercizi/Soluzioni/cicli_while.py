"""Problema con il ciclo, provare a eseguire e correggere"""
n = 20_000

while n >= 0:
    n -= 1.5

print(n)


"""Utilizzando un ciclo while calcoliamo la somma dei numeri interi fino all'intero MAX_INT"""

MAX_INT = 50
sum = MAX_INT * (MAX_INT + 1) * 0.5 # Somma dei numeri naturali

loop_sum = 0
i = 0

while i <= MAX_INT:
    loop_sum += i
    i += 1


print(f"Somma {loop_sum}", f"formula {sum}")

"""Scrivere un ciclo che calcola la sequenza di fibonacci per n iterazioni
https://it.wikipedia.org/wiki/Successione_di_Fibonacci
"""

n_max = 5  # fino a quale numero della serie vogliamo arrivare

n_0 = 0 
n_1 = 1

iterazione = 1 # n.b. i primi 2 valori della successione sono fissati per definizione
# quindi la prima iterazione è già fatta

risultato = 0

while iterazione < n_max:

    risultato = n_0 + n_1 
    n_0 = n_1 
    n_1 = risultato
    iterazione += 1

print(f"Il numero alla posizione {n_max} della successione di fibonacci è {risultato}")

n = 0 
my_str = "Hello "

## stringhe con il while
while n < len(my_str):
    print(my_str[n])
    n += 1
    