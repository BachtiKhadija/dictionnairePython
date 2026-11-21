livres = [
 {
 "titre": "Python pour débutants",
 "auteur": "Ahmed",
 "disponible": True
 },
 {
 "titre": "Apprendre SQL",
 "auteur": "Sara",
 "disponible": False
 },
 {
 "titre": "Algorithmique",
 "auteur": "Ali",
 "disponible": True
 }
] 
print("***************************Question1****************************")
#Q1 
titles=[]
for l in livres:
    # print(l.get('titre'))
    titles.append(l.get('titre'))
print(titles)

print("***************************Question2****************************")
#Q2 afficher les livres avec disponible =True
for x in livres:
    if x["disponible"]==True:
        print(x)
    
print("***************************Question3****************************")
#Q3 ajouter un nouveau livres
newB={"titre": "Apprendre PowerShell",
 "auteur": "Ibrahim",
 "disponible": True} 
livres.append(newB)
print(livres)
print("***************************Question4****************************")
livres[0]["disponible"]=False
print("***************************Question5****************************")
counter=0
for x in livres:
    if x["disponible"]==True:
        counter=counter+1 
print("le nombre de livre disponibles est : ",counter)

    