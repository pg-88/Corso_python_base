"""La funzione print non ha ritorno ma ha effetto sul sistema.

L'effetto è che quando invocata prende gli argomenti e li 'butta' nel 
terminale.
In questo modo, l'utente che sta guardando il terminale, può vedere cosa
succede nell'esecuzione del codice.
Print è spesso utilizzata per seguire l'evoluzione delle varibili 
durante l'esecuzione del codice"""

x = 2 
risultato = 0
print("inizialmente il valore di x è: ", x, "\nIl risultato è : ", risultato)


risultato = 3 * x + x - 2 

print("valore di x è: ", x, "\nIl risultato è : ", risultato)


x = 4

risultato = 3 * x + x - 2 

print("valore di x è: ", x, "\nIl risultato è : ", risultato)

# il carattere \n è un carattere speciale, serve per creare una nuova riga
# esiste anche \t che è la tabulazione (tab sulla tastiera) 

print("Prima riga\nSeconda Riga\nTerza Riga")
print("Prima Colonna\tSeconda Colonna\tTerza Colonna","\nPrimo valore\tSecondo valore\tTerzo valore")
# si può andare a capo anche dividendo in più print
# esempio: aggiungo una riga alla tabella sopra
print("altro valore\taltro valore\taltro valore")
