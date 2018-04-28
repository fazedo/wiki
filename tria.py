# -*- coding: utf-8 -*-
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

#prepara lista de prenomes

ifile = open('nomes_femininos.txt')
nomes_femininos_lista=ifile.readlines()
ifile.close()

ifile = open('nomes_masculinos.txt')
nomes_masculinos_lista=ifile.readlines()
ifile.close()

ifile = open('cientistas.txt')
cientistas=ifile.readlines()
ifile.close()


nomes_femininos=[]
for linha in nomes_femininos_lista:
	nomes_femininos.append(linha.strip())

nomes_masculinos=[]
for linha in nomes_masculinos_lista:
	nomes_masculinos.append(linha.strip())

mulheres=0
homens=0
nao_sei=0
total=0
texto=''

for nome in cientistas:
	posi=nome.find('[[')+3
	posf=nome.find(' ',posi)
	if posf<0:
		posf=nome.find(']',posi)

	prenome=nome[posi:posf]
	if prenome in nomes_femininos:
		mulheres=mulheres+1

	else:
		if prenome in nomes_masculinos:
			homens=homens+1
		else:
			nao_sei=nao_sei+1
			texto = texto +  nome.strip() + '\n'
			if prenome[-1]=='a':
				print prenome
	total=total+1			
	
	

print total
print homens,mulheres,nao_sei
print homens+mulheres+nao_sei

ofile=open('nao_sei.txt','w')
ofile.write(texto)
ofile.close()
