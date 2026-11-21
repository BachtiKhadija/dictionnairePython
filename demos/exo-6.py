# Exercice 6

mot = "programmation"
dict_mot = {}

for letter in mot:
    if letter in dict_mot.keys():
        dict_mot[letter] = (dict_mot[letter] + 1)
    else:
        dict_mot[letter] = 1

print(dict_mot)