lst=[]
def comptecar(ca,ch):
    for pos,char in ch:
       if char == ca:
           lst.append(pos)
    return lst

print(comptecar('e','esli'))
print(lst)
            