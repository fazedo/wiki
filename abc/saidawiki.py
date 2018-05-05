import json
from difflib import SequenceMatcher

ifile=open('tabela_com_sugestoes.json')
table = json.loads(ifile.read())
ifile.close()

table = sorted (table, key = lambda table:SequenceMatcher(None,table[2],table[7]).ratio())
somam=0
somaf=0
somama=0
somafa=0

names=[]
#number, gender, name, link, birth, field, obs, ArticleName:
text=''
for p in table:
	art=0
	if not p[7] == 'X':
		text=text+'#[['+p[7]+']], [['+ p[2] + ']],  [[' + p[5] + ']], ' + p[1] + '\n'
		art=1
	if p[1]=="M":
		somam = somam + 1
		somama = somama + art
	if p[1]=="F":
		somaf = somaf + 1
		somafa = somafa + art

		

print((somama/somam), (somafa/somaf))

open('saida.txt','w').write(text)
#print(len(names), 'pesquisadores ')

