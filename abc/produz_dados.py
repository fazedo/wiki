import json


ifile = open('tabela_com_links.json')
table=json.loads(ifile.read())
ifile.close()
k=0
numero_f=0
numero_m=0

for number, gender, name, link, birth, field, obs, ArticleName in table:
	k=k+1
	print (k,number, name)
	if gender == 'M':
		numero_m = numero_m + 1


print(numero_f, numero_m)
