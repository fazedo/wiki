#python 3

import json

ifile = open('tabela_com_links.json')
tabela_links=json.loads(ifile.read())
ifile.close()


ifile = open('lista_abc_masculinos.json')
tabela=json.loads(ifile.read())
ifile.close()

ifile = open('lista_abc_femininos.json')
tabela = tabela + json.loads(ifile.read())
ifile.close()


tabela_links = sorted (tabela_links, key = lambda p:p[2])
tabela = sorted (tabela, key = lambda p:p[0])

num = 0

for k in range(0,len(tabela)):
	if not tabela[k][0] == tabela_links[k][2]:
		print(tabela[k][0], tabela_links[k][2])
	tabela[k].append(tabela_links[k][7])
	if not tabela_links[k][7] == '':
#		print(tabela[k])			
		num = num + 1

print (num)

ofile = open('lista_abc_ambos.json', 'w')
json.dump(tabela, ofile)
ofile.close
