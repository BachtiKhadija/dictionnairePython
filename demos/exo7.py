produits=[{"nom":"Pomme","prix":3,"quantité":50},{"nom":"Lait","prix":8,"quantité":20},{"nom":"Pain","prix":5,"quantité":30}]
#Q1
print(type(produits))
for a in produits:
    print(a["nom"])
#Q1
print(type(produits))
for a in produits:
    prixT=a["prix"]*a["quantité"]
    a["prixTotal"]=prixT
print(produits)
#Q2 
#somQte=sigm(a["quantité"]) pour a in produits
somQte=0
for a in produits:
    somQte=somQte+a["quantité"]
print("la somme des qe est : ",somQte)
#Q3 

#step 1 : sort by prix 
while True:
    exist=False
    for i in range(len(produits)-1):
        if produits[i]["prix"]<produits[i+1]["prix"]:
            produits[i],produits[i+1]=produits[i+1],produits[i]
            exist=True 
    if exist==False:
        break
print(produits)
#step 2 : get product at position 0 
print("le produit avec le prix le plus elevé est : ",produits[0])

#Q4 
print("liste des produits dans la quantité inférieure à 30")
for p in produits:
    if p["quantité"]<=30:
        print(p)