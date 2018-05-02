# -*- coding: utf-8 -*-
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

#distance between strings
from difflib import SequenceMatcher

#strings:
import string

import re
import unicodedata



#Stackoverflow:begin
def StripAccents(text):

    """
    Strip accents from input String.
    :param text: The input string.
    :type text: String.
    :returns: The processed String.
    :rtype: String.
    """
    try:
        text = unicode(text, 'utf-8')
    except NameError: # unicode is a default on python 3 
        pass
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)
#Stackoverflow:end

def NormalizeCreativeBrazilianNames(name):
	name = StripAccents(name).lower().strip()
	name = name.replace('ph','f')
	name = name.replace('th','t')
	name = name.replace('y','i')
	name = name.replace('z','s')
	name = name.replace('ka','ca')


#	if len(name)>2:
#		if name [-3:] == 'ele':
#			name[-1] = 'a'  

	return name

def IsSameName (Name1, Name2):
	Name1 = NormalizeCreativeBrazilianNames(Name1)
	Name2 = NormalizeCreativeBrazilianNames(Name2)

	if not Name1[-1] == Name2[-1]: #Let's be conservative here! (eg. Luísa vs Luís)
		return 0

#	print(Name1,Name2)
	Score = SequenceMatcher(None, Name1, Name2).ratio() 
	return Score
	

def IsFemale(nome):
	prenome = nome.strip().split()[0].lower()
	
	#if prenome in ('josé'):
	#	return False

	#if prenome in ( 'isis'):
	#	return True

	Male_Score = 0
	for nome in nomes_masculinos:
		Male_Score = max(Male_Score, IsSameName (prenome, nome))

	Female_Score = 0
	for nome in nomes_femininos:
		Female_Score = max(Female_Score, IsSameName (prenome, nome))

#	print(prenome, Male_Score, Female_Score)

	if Male_Score == 1 and not prenome[-1] == nome[-1]: 
		return False

	if Female_Score == 1 and not prenome[-1] == nome[-1]:
		return True

	if Male_Score > 0.9 and Female_Score < 0.7:
		return False
	if Male_Score < 0.7 and Female_Score > 0.9:
		return True
	#print(prenome, Male_Score, Female_Score)

	return None

 


#prepara lista de prenomes
ifile = open('nomes_femininos.txt')
nomes_femininos_lista=ifile.readlines()
ifile.close()

ifile = open('nomes_masculinos.txt')
nomes_masculinos_lista=ifile.readlines()
ifile.close()

ifile = open('bolsistas.txt')
cientistas=ifile.readlines()
ifile.close()


lista_femininos=''
lista_masculinos=''

nomes_femininos=[]
for linha in nomes_femininos_lista:
	nome = StripAccents(linha).strip()
	if not nome.strip() == '':
		nomes_femininos.append(nome.strip())

nomes_masculinos=[]
for linha in nomes_masculinos_lista:
	nome = StripAccents(linha).strip()
	if not nome.strip() == '':
		nomes_masculinos.append(nome.strip())





for name in cientistas:
	if not name.strip() == '':
		if not name.strip()[0] == '#':
			IsFe = IsFemale (name)
			if IsFe == None:
				#print(NormalizeCreativeBrazilianNames(name.strip().split()[0]))	
#				print (name.strip())

				while True:
					hm = raw_input("Entre com o gênero de "+name.strip() + ": (m/f/x)" ).lower()
					if hm == 'm' or hm == 'f' or hm == 'x':
						break
				if hm == 'm':
					IsFe = False
					prenome = name.strip().split()[0]
					sn = raw_input("Deseja adicionar " + prenome + " à lista de nomes masculinos? " ).lower()
					if sn =='s':
						ofile = open('nomes_masculinos.txt','a')
						ofile.write('\n'+prenome)					
						ofile.close()
						nomes_masculinos.append(prenome)		
				

				if hm == 'f':
					IsFe = True
					prenome = name.strip().split()[0]
					sn = raw_input("Deseja adicionar " + prenome + " à lista de nomes femininos? " ).lower()
					if sn =='s':
						ofile = open('nomes_femininos.txt','a')
						ofile.write('\n'+prenome)					
						ofile.close()
						nomes_femininos.append(prenome)		


			if not IsFe == None:

				if IsFe:
					lista_femininos = lista_femininos + name.strip()+'\n'
				else:
					lista_masculinos = lista_masculinos + name.strip()+'\n'
					
				



ofile = open('lista_masculinos.txt','w')
ofile.write(lista_masculinos)
ofile.close()

ofile = open('lista_femininos.txt','w')
ofile.write(lista_femininos)
ofile.close()

