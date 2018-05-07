#python 3
#Entra no site do cnpq e lista pioneiras

import urllib.request
import unicodedata
import json

lista = []
number = 0
for edicao in ['','2', '3', '4', '5', '6']: 


	pagina = 'http://cnpq.br/pioneiras-da-ciencia-do-brasil'+edicao
#	print(pagina)
	page = urllib.request.urlopen(pagina)
	Text = str(page.read().decode("utf-8"))


	num=0
	while True:
		pos = Text.find('class="dados-perfil span12')
		Text =  Text[pos:]

		if pos<0:
			break
		pos = Text.find('h3')
		Text =  Text[pos+3:]
		pos = Text.find('<label>')

		num = num +1
		nome=Text[:pos].strip().split('(')
		if len(nome)>1:
			datas = nome[1][:-1]
			datas = datas.replace(' ','').replace('-',' - ')
		else:
			datas=''
		nome = nome[0].title().replace(' De ',' de ' ).replace(' E ', ' e ').replace(' Da ',' da ').replace(' Do ',' do ')
		Text =  Text[pos+7:]
		pos = Text.find('</label>')
		area= Text[:pos]
		print (edicao+':',nome, datas,area )
		lista.append ([edicao, nome, datas, area])

f = open('pioneiras.json', 'w')
json.dump(lista, f)
f.close()


#print (lista)


