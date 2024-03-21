def inverse(ch):
    lettre=""
    for i in ch :
        lettre = i + lettre 
        
    return lettre
ch=str(input("entrez une chaine de caractère:"))
print(inverse(ch))