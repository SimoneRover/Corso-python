# 1. [FACILE] Creare una funzione "max" che prende in ingresso due numeri e restituisce il maggiore dei due.
def max(a, b):
    if a > b:
        return a
    else:
        return b

# 2. [INTERMEDIO] Creare una funzione "fattoriale" che prende in ingresso un numero intero e restituisce il suo fattoriale
def fattoriale(n):
    risultato = 1 # in questa variabile sarà contenuto il fattoriale
    indice = 2 # non serve partire da 1
    while indice <= n: # dobbiamo moltiplicare i numeri da 2 a N
        risultato = risultato * indice # salvo il risultato parziale
        indice = indice + 1
    return risultato

# 3. [DIFFICILE] Come l'esercizio precedente, ma rendere la funzione ricorsiva
def fattoriale(n):
    if n < 2:
        return 1
    
    return n * fattoriale(n-1)

# 4. [DIFFICILE] Un termine della serie di Fibonacci è ottenuto dalla somma dei due termini precedenti.
# Scrivere una funzione "fibonacci" che dato un numero "n" calcoli e stampi i primi "n" termini della serie di Fibonacci.
# La serie parte dai due termini 1, 1

# 1, 1, 2, 3, 5, 8, 13...


def fibonacci(n):
    if (n < 1):
        print("Errore: inserire un numero intero positivo!")
        return
    
    termine_1 = 1
    termine_2 = 1
    if n == 1:
        print(termine_1)
    else:
        print(termine_1)
        print(termine_2)
    
    indice = 3
    while indice <= n:
        nuovo_termine = termine_1 + termine_2 # calcolo nuovo termine della serie
        print(nuovo_termine)
        termine_1 = termine_2 # scalo i due termini precedenti
        termine_2 = nuovo_termine # salvo il nuovo termine
        indice = indice + 1

# 1, 1, 2, 3, 5
#    ^  ^

fibonacci(50)