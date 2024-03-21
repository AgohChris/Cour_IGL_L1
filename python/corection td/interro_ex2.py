maliste=[1,3,11,9889,747,65,-56,36,60]
pair=[]
impair=[]
i=0
while i<len(maliste):
    if maliste[i]%2 == 0:
        pair.append(maliste[i])
    else:
        impair.append(maliste[i])
        i=i+1
        
print("la liste pair est",pair)
print("la liste impair est",impair)