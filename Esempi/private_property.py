"""Esistono delle variabili che noi non controlliamo ma sono gestite da python
stesso durante il lancio e l'esecuzione.

Queste proprietà sono sempre precedute dal 'dunder' ovvero il doppio
underscore (Double UNDERscore)"""

print("nome dato dal sistema al file in esecuzione", __name__)
print("nome del file nel sistema operativo ", __file__)
print("docstring, documentazione a inizio del codice ", __doc__)
print(__cached__)