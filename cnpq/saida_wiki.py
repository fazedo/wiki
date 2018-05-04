import json
from difflib import SequenceMatcher

ifile=open('tabela_com_artigo.txt')
table = json.loads(ifile.read())
ifile.close()

table = sorted (table, key = lambda table:SequenceMatcher(None,table[0],table[6]).ratio())

names=[]
#for pesquisador, nivel, data1, data2, instituicao, area, artigo in table:
text=''
for p in table:
	if not p[6] == 'X':
		text=text+'#[['+p[6]+']], '+ p[0] + ', [[' + p[4] + ']], [[' + p[5] + ']]\n'


print(text)

open('saida.txt','w').write(text)
#print(len(names), 'pesquisadores ')

