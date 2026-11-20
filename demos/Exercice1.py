s="laval"
#d={"b":1,"o":2,"n":1,"j":1,"u":1,"r":1}

#déclarer un dictionnaire vide 
d={} 
#d=dict()
for c in s:
    if c in d.keys():
        d[c]=d[c]+1 
    else:
         d[c]=1  
d={"l":2,"a":2,"v":1}