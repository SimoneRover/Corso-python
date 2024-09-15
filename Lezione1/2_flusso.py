# Il programma viene eseguito dalla prima riga a scorrere.
# E' però possibile alterare il flusso di esecuzione.

# La parola chiave "if" valuta una condizione.
if True:
  # Se la condizione è vera, il blocco di codice viene eseguito.
  print("Condizione vera")

if False:
  print("Condizione vera")
else:
  # La parola chiave "else" specifica un blocco di codice da eseguire
  # se la condizione è falsa.
  print("Condizione falsa")

# Possiamo formulare condizioni con degli operatori.
altezza = 1.83
if altezza >= 1.80:
  print("Sono alto 1.80 o più")
else:
  print("Sono più basso di 1.80")

# Se una condizione ha più di due esiti possibili
# possiamo usare la parola chave "elif" (else-if)
score_1 = 2
score_2 = 1
if score_1 > score_2:
  print("Ha vinto la squadra 1")
elif score_2 > score_1: # else-if
  print("Ha vinto la squadra 2")
else:
  print("Pareggio")

# Se vogliamo eseguire un blocco di codice finché
# una condizione è verificata (vera), usiamo i cicli
conto_alla_rovescia_start = 10
# Il ciclo "while" viene eseguito finché la condizione è vera
while conto_alla_rovescia_start > 0:
  print(conto_alla_rovescia_start)
  conto_alla_rovescia_start = conto_alla_rovescia_start - 1
print("Buon anno!")

lista_nomi = ["Simone", "Nicola", "Alessandro", "Giulio"]
# print( lista_nomi[len(lista_nomi)-1] )

# Il ciclo "for" scorre gli elementi di una lista
for nome in lista_nomi:  # List comprehension
  print("Ciao " + nome)
print("Ho salutato tutti")

# Un ciclo "for" può essere espresso come ciclo "while"
i = 0 # le posizioni in una lista partono da 0!
while i < len(lista_nomi): # len() restituisce la lunghezza di una lista
  print("Ciao " + lista_nomi[i]) # lista[indice] accede all'elemento in posizione "i"
  i = i + 1
print("Ho salutato tutti")

# Un ciclo può essere interrotto con la parola chiave "break"
criminale = "Alessandro"
for sospettato in lista_nomi:
    print("Interrogo " + sospettato)
    if (sospettato == criminale):
      print("Criminale trovato!")
      break

# Condizioni con operatori booleani
criminale == "Alessandro" and altezza >= 1.80
criminale == "Alessandro" or altezza >= 1.80
not criminale == "Alessandro" and altezza >= 1.80
