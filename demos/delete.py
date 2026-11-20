ordinateur={"processeur":"code i7","hardDisque":"SSD","ram":32,"marque":"Dell"}
print(ordinateur)
del ordinateur["hardDisque"]
ordinateur.pop("ram")
print(ordinateur)