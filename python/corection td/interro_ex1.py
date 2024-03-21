l=[2,9,98,100,59,0]

def Max_Min(l):
    max=l[0]
    min=l[0]
    
    for i in l:
        if i>max:
            max=i
        else:
            max=max
            
    for i in l:
        if i<min:
            min=i
        else:
            min=min  
            
    return max,min
print(Max_Min([2,9,98,100,59,0]))


