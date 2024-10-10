import requests

from bs4 import BeautifulSoup

url = "https://www.gov.uk/search/news-and-communications"
reponse = requests.get(url)
page = reponse.content
soup = BeautifulSoup(page, "html.parser")
class_name = "gem-c-document-list__item-description"
descriptions = soup.find_all("p", class_=class_name)
description_textes = []

for description in descriptions:
	description_textes.append(description.string)

print(description_textes)