import requests

def fetchAndSaveToFile(url, path):
    r = requests.get(url)
    with open(path, "w") as f:
        f.write(r.text)

url = "https://www.ilboursa.com/marches/news_valeur?p=3&s=BH"
r = requests.get(url)
print(r.text)

fetchAndSaveToFile(url, "data/times.html")