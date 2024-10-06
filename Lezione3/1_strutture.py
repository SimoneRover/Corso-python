# Nella prima lezione abbiamo già visto qualche esempio di strutture dati.
# Una struttura dati è una variabile complessa che consente di immagazzinare diverse informazioni (anche di tipi diversi)

# 1. Lista
# Una lista contiene più dati
lista = [1, 2, 3, 10, 5, 120]
# Possiamo accedere ad un elemento o ad una sottolista
elemento = lista[2] # accedo all'elemento in posizione 2 (il dato 3)
sottolista = lista[0:3] # prendo la sottilista compresa tra gli indici 0 (compreso) e 3 (non compreso)
# Possiamo effettuare diverse operazioni sulla lista
lista.append(666) # aggiunge un elemento alla fine della lista
lista.extend([9, 8, 7, 1]) # aggiunge un'altra lista alla fine della lista
lista.insert(0, 12) # aggiunge un elemento in una specifica posizione (in questo caso aggiunge 12 in prima posizione)
lista.remove(120) # rimuove un dato dalla lista
elemento_eliminato = lista.pop(3) # rimuove il dato all'indice specificato e lo restituisce
indice = lista.index(120) # restituisce l'indice in cui è contenuto il valore specificato. Dà errore se l'elemento non è presente!
conteggio = lista.count(3) # restituisce il numero di volte in cui l'elemento specificato appare nella lista
lista.sort() # ordina la lista
lista_copia = lista.copy() # restituisce la copia della lista
lista.clear() # svuota la lista

# 2. Set
# Un set è una collezione non ordinata con nessun elemento duplicato.
insieme = {"mela", "pera", "mela", "arancia", "pera", "mela"}
print(insieme) # i duplicati vengono rimossi
# Possiamo creare un set da una lista
lista = [1, 2, 3, 1, 2, 3, 1, 2, 3]
insieme = set(lista)
print(insieme)

# 3. Dizionario
# Memorizza associazioni tra dati ed un elemento "chiave"
dizionario = {"name": "Simone", "age": 26}
# Possiamo accedere ad un valore specificando la sua "chiave"
age = dizionario["age"]

# CICLI SU STRUTTURE DATI
for chiave, valore in dizionario.items():
    print(chiave + ": " + valore)

for indice, valore in enumerate(lista):
    print("[" + indice + "] " + valore)

domande = ["Come ti chiami?", "Come stai?"]
risposte = ["Simone", "Bene"]
for d, r in zip(domande, risposte):
    print(d)
    print(r)