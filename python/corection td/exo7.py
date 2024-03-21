t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin','Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']

i=0
a = len(t1)
b = len(t2)
t3 = []
for c in range(a):
    for d in range(b):
        while i <=a :
            t3.append(t1[c])
            t3.append(t2[d])
    i=i+1

print("Yann")
            
# for cle in t1 :
#     for mois in t2:
#         while i<=len(t1) and i <=len(t2):
#             t3=[]
#             t3.append(t2[mois])
#             t3.append(t1[cle])
#         i=i+1
        
# print(t3)