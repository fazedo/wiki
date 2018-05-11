#python 3

import json

ifile = open('lista_abc_ambos.json')
tabela = json.loads(ifile.read())
ifile.close()

for name, link, birth, field, desde, nacionalidade, verbete in tabela:
	print(name,verbete)


