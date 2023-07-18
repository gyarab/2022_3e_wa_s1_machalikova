import httpx
from pprint import pprint

url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"
res = httpx.get(url)
rows = res.text.split("\n")

rows = rows[2:-1]
data = {}

for r in rows:
    cols = r.split("|")
    am = int(cols[-3])
    curr = cols[-2]
    rate = cols[-1]
    rate = rate.replace(",", ".")
    rate = float(rate)
    if am > 1:
        rate = rate/am
    data[curr] = rate
pprint(data)

user_curr_from = input("Zadejte pocatecni menu: ")
user_amount = input("Zadejte castku: ")
user_amount = float(user_amount)
user_curr = input("Zadejte cilovou menu: ")

if user_curr_from == "CZK":
    result = user_amount / data[user_curr]
    result = round(result, 2)
elif user_curr == "CZK":
    result = user_amount * data[user_curr_from]
    result = round(result, 2)
else:
    result = user_amount * data[user_curr_from]
    result = round(result, 2)
    result = result / data[user_curr]

print(f"Vysledna castka je {result} {user_curr}")