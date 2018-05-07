#python 3

import json

ifile = open('tabela_com_links.json')
table=json.loads(ifile.read())
ifile.close()

Text = ''
OldArea = ''
lista = ['F','M']

table = sorted (table, key = lambda p:(p[5],lista.index(p[1]) ))

for number, gender, name, link, birth, field, obs, ArticleName in table:
	if not OldArea == field:
		Text = Text + '=='+field+'==\n'
		OldGender=''
		OldArea=field

	if not OldGender == gender:
		Text = Text + '==='+gender+'===\n'
		OldGender = gender

	if ArticleName.strip() == '':
		ArticleName = name
	Text = Text + '#[['+ArticleName+']], [['+name+']], [http://www.abc.org.br/?'+ link+' ABC]\n' 
	
open('lista.wiki','w').write(Text)
print(Text)
