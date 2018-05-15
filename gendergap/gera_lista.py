#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Todo: remover bots com RonaldB, incluir lista de usuário sem gênero definido: JMGM

from __future__ import division

from datetime import datetime

import requests
import urllib
import ast
import json


ifile = open('lista_editores_ativos.json')
lista = json.loads(ifile.read())
ifile.close()

male = 0
female = 0
total = 0
malecount = 0
femalecount = 0
totalcount = 0


limiar = 10000
limiar_max = 100000

verbose = False 
verbose = True
for nome,  genero, contagem in lista:
	if contagem >= limiar and contagem <=limiar_max:
		if genero == 'male':
			male = male + 1
			malecount = malecount + contagem
		elif genero == 'female':
			female = female + 1
			femalecount = femalecount + contagem
		else: 		#neutro/nao declarou
			if verbose:
				print nome, genero, contagem
		total = total + 1
		totalcount = totalcount + contagem


print male, female, total-female-male, total
print 'Declarados:', male + female, 'seja: ', 100*(male + female)/total
print 'Feminino:', 100*female/(female+male)

print 'Declarados count:', malecount + femalecount, 'seja: ', 100*(malecount + femalecount)/totalcount
print 'Feminino count:', 100*femalecount/(femalecount+malecount)
print male, female, total-female-male, total

