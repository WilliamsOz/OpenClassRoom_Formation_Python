print("Entrez une liste de nombre séparée par des virgule")
input = input()
list = input.split(',')
print(f"Votre liste est {list}.")

res = 0
for x in list:
	res = res + int(x)
print(f"La somme de votre liste est {res}.")

moyenne = res / len(list)
print(f"La moyenne de la somme de la liste est {moyenne}")

nb_sup_moyenne = []
for x in list:
	if (int(x) > int(moyenne)):
		nb_sup_moyenne.append(int(x))

print(f"Les nombres supérieur à la moyenne de la liste sont : {nb_sup_moyenne}.")

even_number = []
for x in list:
	if (int(x) % 2 == 0):
		even_number.append(int(x))
print(f"Les nombres paires de votre liste sont : {even_number}.")