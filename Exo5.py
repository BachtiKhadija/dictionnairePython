notes = {
 "Ali": 14,
 "Sara": 18,
 "Youssef": 12,
 "Amine": 16
}

#Q1
print(notes.get("Sara","Not Found"))
#Q2
notes["Fatima"]=17
print(notes)
#Q3 
v=list(notes.values())
taille=len(v)
som=0
for x in v:
    som=som+x  
moy=som/taille
print("la moyenne est :",moy)
#Q4
#** trier le dictionnaire par note dans l ordre descendant 
#*** transformer le dict en list 
Lnotes=list(notes.items())
print(Lnotes)
while True:
    exist=False
    for i in range(taille-1):
        if Lnotes[i][1]<Lnotes[i+1][1]:
            exist=True
            Lnotes[i],Lnotes[i+1]=Lnotes[i+1],Lnotes[i]
            
    if exist==False:
        break 
print("le stagiaire qui a la meilleure note est : ",Lnotes[0][0])
#Q5 
over15={}
for k,v in notes.items():
    if v>=15:
        over15[k]=v 
        #over15.update({k:v})
print(over15)