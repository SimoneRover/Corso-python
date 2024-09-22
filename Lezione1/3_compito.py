# NOTA: Per convertire una stringa in un intero usare la funzione int(stringa)

# 1. [FACILE] Richiedere all'utente due numeri e stampare la somma

# 2a. [FACILE] Salvare una stringa in una variabile; richiedere all'utente di inserire una stringa.
# Se la stringa inserita è uguale alla stringa salvata, stampare "Password corretta",
# altrimenti stampare "Password sbagliata".

# 2b. [INTERMEDIO] Come nell'esercizio precedente, ma continuare a chiedere all'utente
# di inserire la password finché non è corretta o viene digitato '0'.

# 3. [INTERMEDIO] Chiedere all'utente di inserire due numeri interi (dare per scontato che lo siano).
# Verificare se il primo numero è divisibile per il secondo senza usare l'operatore
# 'modulo' (%).

a = 10
b = 2

# 4. [DIFFICILE] Chiedere un numero all'utente e verificare se è un numero primo
# cercando di fornire una soluzione ottimale (ovvero il minor numero di operazioni).

numero = 113
primo = True

if numero == 1 or numero == 2:
    print("Primo")
else:
    divisore = 2
    while divisore < numero // 2:
        if numero % divisore == 0:
            primo = False
            print("Non è primo")
            break
        divisore = divisore + 1
    if primo:
        print("Primo")


# 5. [DIFFICILE] Data la seguente lista ordinata di numeri interi, chiedere all'utente un numero
# e verificare se il numero si trova nella lista cercando di fornire una soluzione ottimale 
# (ovvero eseguire il minor numero di letture dalla lista).
lista = [0, 3, 10, 13, 16, 22, 40, 55, 60, 121, 999]
