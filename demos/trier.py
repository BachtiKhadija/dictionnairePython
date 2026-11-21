from random import * 
l=[randint(1,50) for i in range(20)]
print(l)
#algorithme de tri => ascending order 
"""l[0] l[1]
l[1] l[2]



l[18] l[19]
"""
while True:
    exist=False
    for i in range(len(l)-1):
        if(l[i]<l[i+1]):
            exist=True
            temp=l[i]
            l[i]=l[i+1]
            l[i+1]=temp 
    if exist==False:
        break
print(l)
"""
l=[2,5,9,10,12] 
i de 0 3
i=0 =>exist=True  
i=1 =>exist=True 
i=2 =>exist=True 
i=3  =>
exist=False 
i de 0 3
i=0 => exist=True
i=1 =>
i=2 =>
i=3  =>
exist=False 
i de 0 3
i=0 => 
i=1 =>
i=2 =>
i=3  =>"""