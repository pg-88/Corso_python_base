# Corso_python_base
DigiGreen Manufacturing base (48 h) – GP5

- tenuto da Grigolo Pietro <a href="mailto:grigolopi@gmail.com">e-mail grigolopi@gmail.com</a>

## Programma del corso:
- [Corso\_python\_base](#corso_python_base)
  - [Programma del corso:](#programma-del-corso)
    - [Introduzione e Storia](#introduzione-e-storia)
    - [L'interprete Python e l'IDLE](#linterprete-python-e-lidle)
    - [Sintassi](#sintassi)
      - [Funzione print](#funzione-print)
      - [Funzioni con ritorno](#funzioni-con-ritorno)
      - [Esercizio](#esercizio)
    - [Tipi di dato semplici](#tipi-di-dato-semplici)
    - [Cicli Interattivi e Iterativi](#cicli-interattivi-e-iterativi)
      - [Fuori tema](#fuori-tema)
    - [Funzioni, moduli e oggetti](#funzioni-moduli-e-oggetti)
    - [Strutture dati: list, tuple, set, dictionary](#strutture-dati-list-tuple-set-dictionary)
    - [Gestione delle stringhe, dei file e dell'input da terminale](#gestione-delle-stringhe-dei-file-e-dellinput-da-terminale)
    - [Installazione e uso del package manager PIP](#installazione-e-uso-del-package-manager-pip)
    - [Python come moderno linguaggio di Scripting](#python-come-moderno-linguaggio-di-scripting)
  - [Progetto Automobile](#progetto-automobile)

### Introduzione e Storia

[slide](https://docs.google.com/presentation/d/122N21k2_MtJehqsGaAKmmj1EDI5lWALfzuM-X1WGAVU/edit?usp=sharing)

**Vecchio logo**

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Python_logo_1990s.svg/1920px-Python_logo_1990s.svg.png" width="33%"/> 

Cosa si può fare con python:
- [esempio script per organizzare file](./Esempi/organizza_download.py)
- [esempio script per generare qrcode](./Esempi/genera_qrcode.py)

- Filosofia di python:

  <code>
    The Zen of Python, by Tim Peters<br>
    <br>
    Beautiful is better than ugly.<br>
    Explicit is better than implicit.<br>
    Simple is better than complex.<br>
    Complex is better than complicated.<br>
    Flat is better than nested.<br>
    Sparse is better than dense.<br>
    Readability counts.<br>
    Special cases aren't special enough to break the rules.<br>
    Although practicality beats purity.<br>
    Errors should never pass silently.<br>
    Unless explicitly silenced.<br>
    In the face of ambiguity, refuse the temptation to guess.<br>
    There should be one-- and preferably only one --obvious way to do it.<br>
    Although that way may not be obvious at first unless you're Dutch.<br>
    Now is better than never.<br>
    Although never is often better than *right* now.<br>
    If the implementation is hard to explain, it's a bad idea.<br>
    If the implementation is easy to explain, it may be a good idea.<br>
    Namespaces are one honking great idea -- let's do more of those!<br>

  </code>

- Nascita di python: 

### L'interprete Python e l'IDLE

[slide](https://docs.google.com/presentation/d/16P8V_V3i6wOxzOaCVx47xnZej2yCXYtZ_WrOZnWsdMs/edit?usp=sharing)

- Linguaggi interpretati VS linguaggi compilati [esempio C++](./Esempi/helloC.cpp)
- Interprete python [articolo in inglese](https://learnpython.com/blog/blopython-interpreter/)
- Guida intergalattica al terminale aka la riga di comando [linuxcommand.org](https://linuxcommand.org/index.php)

### Sintassi

[slide](https://docs.google.com/presentation/d/1mihm0iy8C5F_lzG7AZeR49mvJW6jRxfCqGXxSUL-z9Y/edit?usp=sharing)
Le parole e i simboli che fanno il linguaggio.

[documentazione](https://docs.python.org/3/reference/lexical_analysis.html)

#### Funzione print
[codice con esempi](./Esempi/esempi_print.py) da lanciare, modificare e rilanciare!

#### Funzioni con ritorno
[codice con esempi](./Esempi/funzioni_ritorno.py)

#### Esercizio
[Esercizio Proposto](./Esercizi/tempo.py) prevede di gestire il ritorno della funzione `tempo()` assegnandolo a una variabile per poi poterci svolgere operazioni algebriche.

### Tipi di dato semplici
[slide](https://docs.google.com/presentation/d/13muy_9qsUs6OWGAY529W9X7fO0X0gV5bND8K4yYncto/edit#slide=id.g1ec709cba46_2_23)

[esempi stringhe](./Esempi/stringhe/esempi_stringhe.py)

[cambiare tipo di dato](./Esercizi/input.py)

### Cicli Interattivi e Iterativi

[slide cicli](https://docs.google.com/presentation/d/1Qnd5xqA0lQdYrUosftfUFUwdm8gplTTI9CQLw9aFTx0/edit?usp=sharing)

[Esempi con i cicli](./Esempi/cicli/ciclo_intro.py)

[Cicli While](./Esercizi/cicli_while.py)

[Cicli For](./Esercizi/cicli_for.py)

#### Fuori tema 
Esempio di un notebook jupyter [Notebook jupyter](./Notebook/random.ipynb).

- Per installare la libreria: `pip install jupyter`

### Funzioni, moduli e oggetti

[slide](https://docs.google.com/presentation/d/1iy03POHIZsC4vqxhKJXtCbs1qZEtm7NCVd-Ewf3QBq0/edit?usp=sharing)

[esercizi](./Esercizi/funzioni.py)

[extra](./Notebook/decoratori.ipynb)

### Strutture dati: list, tuple, set, dictionary

[slide](https://docs.google.com/presentation/d/1MPA17cY1oOrEMthsCOMtBJhoCDTgpSLoaEYhoJQq47M/edit?usp=sharing)

[esercizi liste](./Esercizi/liste.py)
[esercizi dictionary](./Esercizi/dizionari.py)


[Gestire gli errori](./Notebook/gestione_errori.ipynb)

### Gestione delle stringhe, dei file e dell'input da terminale

[Leggere e scrivere File](./Notebook/leggere_scrivere_file.ipynb)

[Modulo sys](./Notebook/libreria_sys.ipynb)

[Modulo os](./Notebook/libreria_os.ipynb)

[Modulo json](./Notebook/libreria_json.ipynb)

Altra libreria molto ricca di funzionalità che può leggere e manipolare dati da file è [Pandas](./Notebook/pandas_notebook.ipynb)

### Installazione e uso del package manager PIP

[pip e venv](https://docs.google.com/presentation/d/1wheheSXbIYSIPIQdIuD75Qu3ANomMn_PWpo8Btgr0aE/edit?usp=sharing)

### Python come moderno linguaggio di Scripting

[Classi e oggetti, Object Oriented](./Notebook/classi_oop.ipynb)

[Database sqlite](./Notebook/db_sqlite3.ipynb)

[Introduzione a Pandas](./Notebook/intro_pandas.ipynb)

[Utilizzare le API](./Notebook/usare_API.ipynb)

[Creare API](./Notebook/creare_API.ipynb)

[esempio FastAPI](./Esempi/fastapi_main.py) simile a quello fatto a lezione. Da finire e integrare

[interfaccie grafiche](./Notebook/gui.ipynb)



## Progetto Automobile

Il file main con il la signature e docstring delle funzioni finora pensate è [main_automobili](./Esercizi/main_automobili.py)