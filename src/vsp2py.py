from bs4 import BeautifulSoup

with open('src/geometria.vsp3') as f:
    data = f.read()

openVSP = BeautifulSoup(data, 'xml')
geom_list = openVSP.find_all('Geom')
print(geom_list[0].get('Name'))