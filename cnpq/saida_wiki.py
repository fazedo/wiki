import json

ifile=open('tabela_com_artigo.txt')
table = json.loads(ifile.read())
ifile.close()

names=[]
#for pesquisador, nivel, data1, data2, instituicao, area, artigo in table:
for p in table:
	if 'PQ-1A' in p[1]:
		print(p)



print(len(names), 'pesquisadores ')

