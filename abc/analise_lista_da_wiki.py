import json

ifile = open('lista_com_artigo.txt')
lines=ifile.readlines()
ifile.close()

nomes=[]
artigos=[]
for line in lines:
	line=line.strip()
	if len(line)>0:
		elementos = (line.split(','))
		artigo = elementos[0][3:-2]
		nome = elementos[1][3:-2]
		nomes.append(nome)
		artigos.append(artigo)



ifile = open('tabela_com_sugestoes.json')
table=json.loads(ifile.read())
ifile.close()
meses = {'jan':1, 'fev':2, 'mar':3, 'abr':4, 'mai':5, 'jun':6, 'jul':7, 'ago':8, 'set':9, 'out':10, 'nov':11, 'dez':12}

#number, gender, name, link, birth, field, obs, ArticleName:
k=0
for p in table:
	k=k+1
	print(k)
	#if k>10:
	#	break 
	nome = p[2]
	if nome in nomes:
		index = nomes.index(nome)
		p[7] = artigos[index]
	else:
		p[7]=''

	#print (p[2],'[['+p[7]+']]')
#	print (p[4])  #birth
	membrodesde = (p[6][13:].replace('º','').split())  #obs
	if len(membrodesde)>4:
		data= [int(membrodesde[0]), meses.get(membrodesde[2].lower()), int(membrodesde[4])]
	else:
		data = [0,0,0]
	p[6] = data



ofile=open('tabela_com_links.json','w')
json.dump(table, ofile)
ofile.close()
