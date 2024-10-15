import csv
import requests
from bs4 import BeautifulSoup

# fichier = open('HelloWorld.txt', 'a')
# fichier.write('Hello World !\n')
# fichier.close()

# with open('HelloWorld.txt') as fichier:
# 	for ligne in fichier:
# 		print(ligne)

# with open('couleurs_preferees.csv') as fichier_csv:
# 	reader = csv.reader(fichier_csv, delimiter=',')
# 	for ligne in reader:
# 		print(ligne)

# with open('couleurs_preferees.csv') as fichier_csv:
# 	reader = csv.DictReader(fichier_csv, delimiter=',')
# 	for ligne in reader:
# 		print(ligne['nom'] + " travaille en tant que " + ligne['metier'] + " et sa couleur preferee est " + ligne['couleur_preferee'])

url = "https://www.gov.uk/search/news-and-communications"
response = requests.get(url)
page = response.content
soup = BeautifulSoup(page, "html.parser")

titres = soup.find_all("a", class_="gem-print-link")
titres_text = []
for titre in titres:
	titres_text.append(titre.string)

descriptions = soup.find_all("p", class_="gem-c-document-list__item-description")
description_text = []
for description in descriptions:
	description_text.append(description.string)

headers = ['title', 'description']
with open('data.csv', 'w') as csv_file:
	writer = csv.writer(csv_file, delimiter=',')
	writer.writerow(headers)
	for titre, description in zip(titres_text, description_text):
		writer.writerow([titre, description])