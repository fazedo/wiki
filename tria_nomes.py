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

#	if len(name)>2:
#		if name [-3:] == 'ele':
#			name[-1] = 'a'  

	return name

def IsSameName (Name1, Name2):
	Name1 = NormalizeCreativeBrazilianNames(Name1)
	Name2 = NormalizeCreativeBrazilianNames(Name2)

	if not Name1[-1] == Name2[-1]:
		return 0

#	print(Name1,Name2)
	Score = SequenceMatcher(None, Name1, Name2).ratio() 
	return Score
	

def IsFemale(nome):
	prenome = nome.strip().split()[0]
	
	Male_Score = 0
	for nome in nomes_masculinos:
		Male_Score = max(Male_Score, IsSameName (prenome, nome))

	Female_Score = 0
	for nome in nomes_femininos:
		Female_Score = max(Female_Score, IsSameName (prenome, nome))

#	print(prenome, Male_Score, Female_Score)

	if Male_Score > 0.8 and Female_Score < 0.6:
		return False
	if Male_Score < 0.6 and Female_Score > 0.8:
		return True
	return None

 


#prepara lista de prenomes
ifile = open('nomes_femininos.txt')
nomes_femininos_lista=ifile.readlines()
ifile.close()

ifile = open('nomes_masculinos.txt')
nomes_masculinos_lista=ifile.readlines()
ifile.close()

ifile = open('names.txt')
cientistas=ifile.readlines()
ifile.close()


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
		if IsFemale (name) == None:
			print(name.strip())	


