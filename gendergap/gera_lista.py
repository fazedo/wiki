#!/usr/bin/env python
# -*- coding: utf-8 -*-

#To do: remover bots com RonaldB, incluir lista de usuário sem gênero definido: JMGM

from __future__ import division

from datetime import datetime

import requests
import urllib
import ast
import json

lingua = 'sv'
limiar = 1
limiar_max = 100000000
lista_feminino=False
verbose = False
#verbose = True



ifile = open('lista_editores_ativos_' + lingua + '.json')
lista = json.loads(ifile.read())
ifile.close()

lista = sorted(lista, key = lambda f:-f[2])

lista_bots = ['RonaldB']
lista_male = []   #'Umberto Bottura']
lista_female = [] #'JMGM']

male = 0
female = 0
total = 0
malecount = 0
femalecount = 0
totalcount = 0

lista_sem_genero=''

for userid, nome, contagem, registro, genero in lista:
	if contagem >= limiar and contagem <=limiar_max and not nome in lista_bots:
		if genero == 'male' or nome in lista_male:
			male = male + 1
			malecount = malecount + contagem
		elif genero == 'female' or nome in lista_female:
			female = female + 1
			femalecount = femalecount + contagem
			if lista_feminino:
				print nome
		else: 		#neutro/nao declarou
			if verbose:
				print nome, genero, contagem
				lista_sem_genero = lista_sem_genero + nome + '\n'
		total = total + 1
		totalcount = totalcount + contagem


print male, female, total-female-male, total
print 'Declarados:', male + female, 'seja: ', 100*(male + female)/total
print 'Feminino:', 100*female/(female+male)

#print 'Declarados count:', malecount + femalecount, 'seja: ', 100*(malecount + femalecount)/totalcount
#print 'Feminino count:', 100*femalecount/(femalecount+malecount)
#print male, female, total-female-male, total

#open('lista_sem_genero.txt','w').write(lista_sem_genero)
