def inverse ():
    inv=''
    p=len(ch)
    while p>0 :
        inv=inv+ch[p-1]
        p-=1
    return inv
        
def  palindrome(ch):
    if inverse(ch)==ch:
        return "est un palindrome"
    else:
        return "est un palindrome"
    
ch=str(input("entrez une chaine de caractère: "))
print(inverse(ch),palindrome)