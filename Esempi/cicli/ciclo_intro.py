VALORE_MASSIMO = 1_000
# variabili per gestire il ciclo
n = 0

while n < VALORE_MASSIMO:  # condizione di permanenza nel ciclo
    # blocco di codice che si ripete a ogni iterazione
    print(f"n ha valore {n}")
    n = n * 2  + 1
    print(f"ora il valore di n è {n}")

# terminato il ciclo si procede con il resto del codice
print(f"il valore massimo raggiunto da n è {n}")

# ciclo for con range(start, stop)
for i in range(5, 10):
    print(i)

# solo 1 valore a range
for i in range(10):
    print(i)


# range con start stop e step
for i in range(0, 300, 10):
    print(i)
# else: print(f"{i} era l'ultimo")

for i in range(0, 20, 7):
    print(f"sette per è uguale a {i}")