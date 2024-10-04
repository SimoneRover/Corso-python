# Abbiamo già visto il tipo di dato "stringa"
# Una stringa è una sequenza di caratteri che devono essere delimitati da doppi apici.

stringa = "ciao"

# Possiamo eseguire varie operazioni sulle stringhe

# Rendo la prima lettere maiuscola
capitalized = stringa.capitalize()

# Quante volte è contenuta la lettera "c" nella variabile stringa?
c_count = stringa.count("c")

# La variabile stringa finisce con la lettera "o"?
finisce_in_o = stringa.endswith("o")

# In che posizione si trova il carattere "a" nella variabile stringa?
pos_a = stringa.find("a")

pos_a = stringa.index("a") # cosa cambia rispetto a "find"?

# Tutto lower case
lower_case = stringa.lower()

# Tutto upper case
upper_case = stringa.upper()

# Rimpiazzo porzioni di stringa
nuova_stringa = stringa.replace("ia", "hiass")

# Dividi la stringa
lista_split = stringa.split("i")

# La variabile stringa inizia con il carattere "c"?
stringa.startswith("c")

# Possiamo fare un ciclo sui caratteri di una stringa
for carattere in stringa:
    print(carattere)

# Ci sono molte altre funzioni utilizzabili sulle stringhe.
# Vedere la documentazione: https://www.w3schools.com/python/python_ref_string.asp