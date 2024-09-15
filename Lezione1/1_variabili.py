# Le righe precedute dal cancelletto '#' sono commenti.

# Le variabili sono usate per immaganizzare dati.
# L'operatore '=' è l'operatore di assegnazione.
nome_variabile = "contenuto"

# Una variabile può contenere vari tipi di dati.
# Il contenuto di una variabile è conservato in memoria centrale come sequenza di byte.
variabile_intera = 20
variabile_decimale = 20.20 # float
variabile_stringa = "stringa" # Rappresenta una sequenza di caratteri
variabile_booleana = True # Usate per la valutazione di condizioni (True/False)
variabile_lista = [1, 2, 3, 4, 5] # Mutabili
variabile_tupla = (1, 2, 3, 4, 5) # Non mutabili
variabile_None = None # Valore speciale di Python

# Puoi assegnare ad una variabile un altra variabile.
variabile = variabile_intera

# Puoi effettuare operazioni.
sum = 20 + 20
diff = 20 - 20
mult = 20 * 20
div = 20 / 20
mod = 20 % 20
resto = 5 % 3
print("Resto: " + str(resto))

# Puoi effettuare operazioni con variabili.
addendo1 = 20
addendo2 = 20
somma = addendo1 + addendo2

# Puoi stampare il contenuto di una variabile.
print(somma)

# Puoi chiedere all'utente di inserire dei dati.
numero = input("Inserisci numero: ")

# Puoi controllare l'uguaglianza
numero == 20 # True/False

# Puoi verificate che una variabile sia o meno None
print(numero is None) # True/False
print(numero is not None)


print(type(numero)) # Restituisce il tipo