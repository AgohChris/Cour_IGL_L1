""""
i=1
factoriel=1
print("entrez un nombre ")
n=int(input())
while i<=n:
    factoriel=factoriel*i
    i+=1
print('le factoriel de ',n,"est ",factoriel)
"""""

def factoriel(n):
    if n==0 or n==1:
        return 1
    facto=1
    for i in range(2,n+1):
        facto=facto*i
        return facto
    
n=int(input("entrez un nombre entier: "))
print(factoriel(n))