def salaire_mensuel(salaire_annuel):
	return salaire_annuel / 12

def salaire_hebdomadaire(salaire_mensuel):
	return salaire_mensuel / 4

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
	return salaire_hebdomadaire / heures_travaillees

print("Quel est votre salaire annuel ?")
salaire_annuel = input()

print("Combien d'heures travaillées-vous par semaine ?")
heure_semaine = input()

resultat = salaire_horaire(salaire_hebdomadaire(salaire_mensuel(int(salaire_annuel))), int(heure_semaine))

print("Votre salaire horaire est de ", resultat, "euros")