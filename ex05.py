nombre_a_gauche = 21.21
nombre_a_droite = 21.21
symbole = '+'
res = 0

if (isinstance(nombre_a_droite, (int, float)) == False or isinstance(nombre_a_gauche, (int, float)) == False):
	print("Les nombres doivent être des entiers")
	exit(1)
match symbole:
	case '+':
		res = nombre_a_gauche + nombre_a_droite
	case '-':
		res = nombre_a_gauche - nombre_a_droite
	case '*':
		res = nombre_a_gauche * nombre_a_droite
	case '/':
		if (nombre_a_droite == 0):
			print("Erreur: impossible de diviser par zéro.")
			exit (1)
		else:
			res = nombre_a_gauche / nombre_a_droite
	case _:
		print("Le symbole n'est pas '+, -, * ou /'.")
		exit (1)
print(res)