# Spesso, occorre eseguire una porzione di codice diverse volte in parti diverse del programma.
# Possiamo definire delle funzioni con la parola chiave "def".
# Una funzione è una parte di codice separata dal flusso di esecuzione che può essere eseguita a piacere.
# Ad esempio, abbiamo già visto alcuni esempi di funzioni come "print" e "input".

# def nome_funzione():
#   corpo della funzione

# Ora creiamo una nostra funzione che saluta.
def greet():
    print("Ciao")

# Ora possiamo salutare quante volte vogliamo:
greet()
greet()
greet()

# Possiamo dare ad una funzione dei dati in ingresso che può usare
def greet(nome):
    print("Ciao " + nome)

# Ora possiamo salutare persone diverse:
greet("Nicola")
greet("Stefano")
greet("Giulia")

# Abbiamo definito due funzioni con lo stesso nome, cosa è successo alla vecchia funzione "greet()"? Non è banale!
# greet()

# Possiamo far coesistere le due funzioni usando un valore di default:
def greet(nome = None):
    if (nome is None):
        print("Ciao")
    else:
        print("Ciao " + nome)

greet() # possiamo omettere il parametro "nome"
greet("Simone")

# NOTA: Prima di chiamare una funzione, questa DEVE essere prima definita.

# Una funziona può terminare restituendo un valore (come la funzione "input")
def somma(a, b):
    return a + b # restituisci

# Ora possiamo sommare agilmente:
risultato = somma(10, 43)
print(risultato)

# Una funzione definisce uno "scope", quindi tutte le variabili create in una funzione non sono accessibili dall'esterno!
# Invece una variabile dichiarata fuori dal corpo della funzione può essere acceduta.

variabile_esterna = 666
def funzione():
    print(variabile_esterna)
funzione()

# Ovviamente, una funzione può essere richiamata all'interno di un altra
def doppio(x):
    return somma(x, x)

print(doppio(20))

# Una funzione può richiamare se stessa, questo processo si chiama ricorsione
# In generale, una funzione ricorsiva è divisa in 3 parti:
# - Base (controllo condizione di terminazione)
# - Corpo (dove avviene la computazione)
# - Passo (viene richiamata la funzione)

def conto_alla_rovescia(n):
    if (n < 0): # Base
        return

    print(n) # Corpo
    conto_alla_rovescia(n-1) # Passo

conto_alla_rovescia(10)