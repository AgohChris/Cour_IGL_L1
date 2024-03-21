etudiant={"NCIN":"","NOM":"","PRENOM":"","AGE":"","DECISION":""}
def saisir():
    with open('concours.txt','a') as c:
        for cle in etudiant.keys():
           etudiant[cle]=int(input("entrez la valeur"))
           c.write(etudiant[cle])
       
           
def admis():
    with open('admis.txt','a'):
        