# Corso Python
Questa repository contiene le lezioni ed eventuali risorse del corso di Python.

## Setup
Per seguire il corso occorre avere diversi tool.
### Python
Scaricare Python dal sito ufficiale [python.org](https://www.python.org/downloads/). Al momento l'ultima versione è la 3.12.6.<br>
Se dopo l'installazione non viene trovato il comando "python", aggiungere il percorso di installazione di Python alla variabile d'ambiente PATH del proprio PC.
### Visual Studio Code
- Scaricare l'editor Visual Studio Code dal sito ufficiale [code.visualstudio.com](https://code.visualstudio.com/Download).
- (Opzionale) Creare un nuovo profilo "Python".
- Installare il pacchetto estensione "Python". Di seguito il link per conferma [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python).
### Git
- Installare Git per il versioning del progetto. Il sito ufficiale è [git-scm.com](https://git-scm.com/downloads).
- Aprire Git Bash e digitare il comando `git clone https://github.com/SimoneRover/Corso-python` per copiare il progetto in locale.

## Usare Git
Una volta aperta la cartella del progetto con Visual Studio Code, nella barra verticale a sinistra potrete gestire il versioning (ovvero la sincronizzazione dei cambiamenti nei file del progetto) con l'icona 'Source Control' o premendo `Ctrl + Shift + G`.<br>
L'ecosistema di Git si sostanzia in alcuni passi essenziali:
- **Commit**: Conferma le modifiche selezionate (*staged*) per poi essere inviate alla repository remota. Prevede un messaggio che descrive le modifiche.
- **Push**: Invia le modifiche, precedentemente aggiunte in un *commit*, alla repository remota.
- **Pull**: Prende le modifiche dalla repository remota e aggiorna i file locali. Il processo di ricezione delle modifiche dalla repository remota è chiamato *fetch*.

**NOTA:** di default solo il creatore della repository può inviare modifiche. Inviare altri eventuali file (come gli esercizi assegnati a fine lezione) su Discord.

## Eseguire un file Python
Per eseguire un file Python possiamo utilizzare la console di Visual Studio Code.<br>
Per aprire la finestra del terminale premere `Ctrl + ò`.<br>
Inizialmente, il terminale verrà aperto nella cartella del progetto, ad esempio
```
PS D:\Corso-python>
```
Dato che i file Python sono collocati all'interno delle cartelle delle lezioni, dobbiamo spostare il terminale in modo che legga all'interno della cartella desiderata utilizzando il comando *change directory* `cd`, ad esempio
```
PS D:\Corso-python> cd Lezione1
PS D:\Corso-python\Lezione1>
```
Adesso possiamo eseguire i file all'interno della cartella "Lezione1"
```
PS D:\Corso-python\Lezione1> python 3_compito.py
```
Per risalire la gerarchia di cartella usiamo il comando `cd ..`, ad esempio
```
PS D:\Corso-python\Lezione1> cd ..
PS D:\Corso-python>
```

## Lezioni
### Lezione 1
11 settembre 2024

Argomenti trattati:
- Variabili e operazioni con variabili
- Le funzioni standard `print`, `len`, `type` e `input`
- Controllo del flusso di esecuzione
- Il costrutto IF, ELSE, ELIF
- Il costrutto WHILE, FOR
- Differenze tra WHILE e FOR
- Cenni all'algebra booleana (valori di verità e condizioni)
- Prima visione degli esercizi compito

Prossima lezione concordata per venerdì 20 settembre.

### Lezione 2
22 settembre 2024

Argomenti trattati:
- Correzione esercizi Lezione 1
- Algebra booleana:
    - Operatori booleani semplici
    - Operatori booleani composti
    - Proprietà degli operatori booleani
    - Teoremi dell'algebra booleana
- Funzioni:
    - Definizione di nuove funzioni
    - Parametri in ingresso
    - Parametri opzionali
    - Parola chiave `return`
    - Scope della funzione
    - Funzioni ricorsive

Prossima lezione concordata per sabato 28

### Lezione 3
TODO