import requests

url = "https://files.rcsb.org/download/1BGA.pdb"

r = requests.get(url)

print(r.text)
