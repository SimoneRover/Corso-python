# Una condizione semplice (senza uso di operatori booleani and/or/not) è chiamata predicato o proposizione.
# Proposizioni possono essere combinate con gli operatori booleani

a = True
b = False
c = False

# NOT - Inverte in predicato
not_a = not a # False

# AND - True se entrambe (tutte) le proposizioni sono True
a_and_a = a and a # True
a_and_b = a and b # False
b_and_b = b and b # False

# OR - True se almeno una proposizione è True
a_or_a = a or a # True
a_or_b = a or b # True
b_or_b = b or b # False

# Priorità degli operatori booleani
# 1. NOT
# 2. AND (moltiplicazione)
# 3. OR (somma)
# Le parentesi possono cambiare l'ordine di priorità degli operatori (proprio come in algebra!)
# In caso di parentesi, si calcola prima la condizione più interna.

# Operatori composti

# NAND - Negazione di AND (NOT AND)
not_a_and_a = not a_and_a # False - not (a and a)
not_a_and_b = not a_and_b # True
not_b_and_b = not b_and_b # True

# NOR - Negazione di OR
not_a_or_a = not a_or_a # False
not_a_or_b = not a_or_b # False
not_b_or_b = not b_or_b # True

# XOR - OR esclusivo, True solo se una E UNA SOLA proposizione è True
a_xor_a = (a and not a) or (not a and a) # False
a_xor_b = (a and not b) or (not a and b) # True
b_xor_b = (b and not b) or (not b and b) # False

# XNOR - Negazione di XOR, True se entrambe (tutte) le proposizioni hanno lo stesso valore di verità
a_xnor_a = (a and a) or (not a and not a) # True - not a_xor_a
a_xnor_b = (a and b) or (not a and not b) # False
b_xnor_b = (b and b) or (not b and not b) # True

a == b # se a e b sono predicati

# Le espressioni booleane godono di utili proprietà (proprio come gli operatori matematici)

# PROPRIETA' COMMUTATIVA
a and b == b and a 
a or b == b or a 

# PROPRIETA' ASSOCIATIVA
a or b or c == (a or b) or c == a or (b or c)
a and b and c == (a and b) and c == a and (b and c)

# PROPRIETA' DISTRIBUTIVA
a and c or b and c == (a or b) and c
(a or c) and (b or c) == a and b or c

# Teoremi

# TEOREMA DELL'ANNULLAMENTO
a and False == False
a or True == True

# TEOREMA DELL'IDENTITA'
a and True == a
a or False == a

# TEOREMA DEI COMPLEMENTI
a and not a == False
a or not a == True # Un predicato sempre vero è detto TAUTOLOGIA
not (a and not a) == True # Tautologia, è il contrario del primo predicato

# TEOREMA DELL'IDEMPOTENZA
a and a = a
a or a = a

# TEOREMA DELL'ASSORBIMENTO
a and (a or b) == a
a or (a and b) == a

# TEOREMA DI DE MORGAN
# Il teorema più utilizzato
# Il not viene distribuito e si cambia l'operatore booleano (and diventa or e viceversa)
not (a and b) == (not a or not b)
not (a or b) == (not a and not b)