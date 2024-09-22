# NOTA: Per convertire una stringa in un intero usare la funzione int(stringa)

# 1. [FACILE] Richiedere all'utente due numeri e stampare la somma
num1 = int(input("Inserisci un numero: "))
num2 = int(input("Inserisci un altro numero: "))
print("La somma è " + str(num1 + num2))

# 2a. [FACILE] Salvare una stringa in una variabile; richiedere all'utente di inserire una stringa.
# Se la stringa inserita è uguale alla stringa salvata, stampare "Password corretta",
# altrimenti stampare "Password sbagliata".
password = "pass123456"
user_input = input("Inserire la password: ")
if (password == user_input):
    print("Password corretta")
else:
    print("Password sbagliata")

# 2b. [INTERMEDIO] Come nell'esercizio precedente, ma continuare a chiedere all'utente
# di inserire la password finché non è corretta o viene digitato '0'.
password = "pass123456"
while True:
    user_input = input("Inserire la password: ")
    if user_input == "0":
        break
    if user_input == password:
        print("Password corretta")
        break
    else:
        print("Password sbagliata")

# 3. [INTERMEDIO] Chiedere all'utente di inserire due numeri interi (dare per scontato che lo siano).
# Verificare se il primo numero è divisibile per il secondo senza usare l'operatore
# 'modulo' (%).

# Sfruttiamo la definizione di divisione come sottrazioni ripetute
dividendo = int(input("Inserisci il dividendo: "))
divisore = int(input("Inserisci il divisore: "))
while dividendo > 0:
    if dividendo - divisore == 0:
        print("I numeri sono divisibili")
        break
    if dividendo - divisore < 0:
        print("I numeri non sono divisibili")
        break
    dividendo = dividendo - divisore

# Soluzione alternativa
quoz = dividendo / divisore
quoz_int = int(quoz) # La conversione a intero tronca la parte decimale del numero float
if (quoz - quoz_int == 0): 
    # Se la differenza tra il float originario e il suo corrispettivo intero è 0, allora il float non aveva cifre decimali (era un intero)
    print("I numeri sono divisibili")
else:
    # Al contrario, se è diversa da 0 allora la divisione dava come risultato un numero decimale, quindi c'era del resto
    print("I numeri non sono divisibili")
    

# 4. [DIFFICILE] Chiedere un numero all'utente e verificare se è un numero primo
# cercando di fornire una soluzione ottimale (ovvero il minor numero di operazioni).
numero = int(input("Inserisci un numero: "))
divisore = 2
primo = True

if numero == 1 or numero == 2:
    print("Numero primo")
else:
    while divisore < numero / 2:
        if numero % divisore == 0:
            primo = False
            print("Numero non primo")
            break
        divisore += 1 # equivale a scrivere: divisore = divisore + 1
    if primo:
        print("Numero primo")

# 5. [DIFFICILE] Data la seguente lista ordinata di numeri interi, chiedere all'utente un numero
# e verificare se il numero si trova nella lista cercando di fornire una soluzione ottimale 
# (ovvero eseguire il minor numero di letture dalla lista).
lista = [0, 3, 10, 13, 16, 22, 40, 55, 60, 121, 999]
#        ^                  ^                    ^
#        i                  m                    f

#                               ^       ^        ^
#                               i       m        f

#                               ^   ^
#                               i   f
#                               m

# Sfruttiamo il fatto che la lista è ORDINATA!
# Partiamo dal centro, se il valore inserito è minore del valore al centro della lista,
# possiamo ignorare la metà a destra. Viceversa possiamo ignorare la metà a sinistra.
# Questo processo si chiama RICERCA BINARIA
user_input = int(input("Inserisci un numero: "))
inizio = 0 # indice di inizio
fine = len(lista) - 1 # indice di fine
medio = 0 # indice nel mezzo

while inizio <= fine:
    medio = (inizio + fine) // 2 # semi-somma

    if lista[medio] < user_input:
        inizio = medio + 1
    elif lista[medio] > user_input:
        fine = medio - 1
    else:
        # Abbiamo trovato il valore!
        break

if lista[medio] == user_input:
    print("Valore presente nella lista")
else:
    print("Valore non presente nella lista")
