emps={"radi":2000,"rami":1500,"razi":3000} 
#transfomer le dict en list 
l=list(emps.items())

print(l)

while True:
    exist=False
    for i in range(len(l)-1):
        if l[i][1]<l[i+1][1]:
            exist=True
            temp=l[i]
            l[i]=l[i+1]
            l[i+1]=temp
    if exist==False:
        break
print(l)
print("l employe qui a la plus grande salaire est : ",l[0][0])
