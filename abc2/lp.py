import urllib.request
from xml.etree import ElementTree as ET
import re
import unicodedata
import json

meses = {'jan':1, 'fev':2, 'mar':3, 'abr':4, 'mai':5, 'jun':6, 'jul':7, 'ago':8, 'set':9, 'out':10, 'nov':11, 'dez':12}
table = []
number = 0

#genero = 'Feminino'
genero = 'Masculino'

for k in range(0,{'Masculino':851, 'Feminino':141}.get(genero),10):

	pagina = 'http://www.abc.org.br/?page=buscaAcademico&id_rubrique=95&titre=&genero=' + genero + '&especializacao=&categoria=&debut_Resultado='+str(k)+'#pagination_Resultado'


	page = urllib.request.urlopen(pagina)
	Text = str(page.read().decode("utf-8"))
	num=0
	while True:
		pos = Text.find('<li dir="ltr" class="hentry clearfix text-left">')
		if pos<0:
			break
		num = num +1
		Text =  Text[pos:]

		pos = Text.find('clear="all"')
		Text2 = Text
		Text = Text[pos:]

		pos =  Text2.find('href="./?')
		Text2 =  Text2[pos+9:]
		pos = Text2.find('">')
		link = Text2[:pos]

		pos = Text2.find('/>')
		Text2 = Text2[pos+3:]
		pos = Text2.find('</a>')
		name = Text2[:pos]

		pos = Text2.find('<small>')
		Text2 = Text2[pos+7:]
		pos = Text2.find('</small>')
		birth = Text2[:pos]

		pos = Text2.find('<b>')
		Text2 = Text2[pos+3:]
		pos = Text2.find('</b>')
		field = Text2[:pos]

		pos = Text2.find('</b>')
		Text2 = Text2[pos+6:]
		pos = Text2.find('</small>')
		obs = Text2[:pos].strip('membro')
		obs=obs.replace('desde','').replace('membro','').replace('º','').strip().split()

		number = number + 1

		birth = birth.replace("n.","").replace("(","").replace(")","").replace("-","").replace('º','').strip().split()

#		print(birth)
#		print(num, name, link, birth, field, obs)

		length = len(birth)

		if length <3:
			birth = [0,0,0]
			nacionalidade = ''
		elif birth[length-2] == 'Nacionalidade:':
			nacionalidade = birth[-1]

		if length >  4:
			birth = [int(birth[0]), meses.get(birth[2].lower()), int(birth[4])]
			
		else:
			birth = [0,0,0]

		
		length = len(obs)
		desde=[]

		if len(obs) == 3:
			desde = [int(obs[0]), meses.get(obs[2].lower()), 2018]

		
		if len(obs) == 5:
			desde = [int(obs[0]), meses.get(obs[2].lower()), int(obs[4])]

#		if desde == []:
#			print(obs)
		table.append([name, link, birth, field, desde])
#		print (name, link, birth, field, obs)
		print(birth,desde,obs)
#	break

	if num<10:
		print (k)
		break


print (number)
ofile = open('lista_abc_'+genero.lower()+'s.json', 'w')
json.dump(table, ofile)
ofile.close()



