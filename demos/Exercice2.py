produits=["yaourt","sablé","lait","sucre"]
prix=["3","2","3.5","10"]

store={}
for i in range(0,len(produits)):
    p=produits[i]
    price=prix[i]
    store[p]=price
print(store)