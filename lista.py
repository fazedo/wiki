#prepara lista de prenomes

#ifile = open('cientistas_mulheres.txt')

#ifile = open('cientistas_mulheres.txt')
ifile = open('nao_sei.txt')

linhas=ifile.readlines()
ifile.close()

k=0
n=1
lista_prenomes=[]
prenome_velho=""

for linha in linhas:
	posi=linha.find('[[')+3
	posf=linha.find(' ',posi)
	if posf<0:
		posf=linha.find(']',posi)

#	nome = linha[pos:-3]
	prenome=linha[posi:posf]
	if prenome==prenome_velho:
		n=n+1
	else:
		par = (prenome_velho,n)
		lista_prenomes.append(par)
		n=1
		prenome_velho=prenome					

	k=k+1
	
lista_prenomes=sorted(lista_prenomes, key = lambda lista_prenomes:-lista_prenomes[1])
texto=''
for k, par in enumerate(lista_prenomes):
	par=lista_prenomes[k]
	texto=texto+ format(par[1],'03d')+'   '+par[0]+'\n'
	#texto=texto+par[0]+'\n'
	
#ofile=open('lista_aux.txt','w')
ofile=open('nao_sei_org.txt','w')
ofile.write(texto)
ofile.close()
