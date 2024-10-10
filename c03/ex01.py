from bs4 import BeautifulSoup

with open("index.html", 'r') as file:
	soup = BeautifulSoup(file, 'html.parser')

title = soup.title.string

print(f"Titre de la page : {title}")

balise_h1 = soup.find_all("h1")[0].string

print(f"balise h1 : {balise_h1}")

products = soup.find_all("li")
product_list = []

for product in products:
	name = product.h2.string
	price = product.find('p', string=lambda s: 'Prix' in s).string
	product_list.append((name, price))

print(product_list)

products = soup.find_all("li")
product_description = []

for product in products:
	product_description.append(product.find('p', string=lambda s: 'Description' in s).string)

print(product_description)

for i, (name, price) in enumerate(product_list):
	euro_price_str = ''.join(filter(str.isdigit, price.split()[2]))
	euro_price = int(euro_price_str)
	dollar_price = euro_price * 1.2
	product_list[i] = (name, f"{dollar_price}$")

print(product_list)