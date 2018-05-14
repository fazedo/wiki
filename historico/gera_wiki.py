#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

from datetime import datetime

import requests
import urllib
import ast
import json


ifile = open('lista_editores_com_primeira.json')
lista = json.loads(ifile.read())
ifile.close()

total = 0
limiar = 500

ano_atual = ''
lista = sorted(lista, key = lambda p:p[0])
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
text = ''
for primeira_vez, nome, contagem, registro in lista:
	ano=primeira_vez[:4]
	if not ano == ano_atual:
		linha = '=='+ano+'==\n'
		print(linha)
		ano_atual = ano
		text=text+linha

	linha = '#' + primeira_vez[8:10] + '/' + meses[int(primeira_vez[5:7])-1] + '/' + primeira_vez[:4]
#	linha = linha + ' {{Usuário|' + nome + '}}'
	linha = linha + ' [[usuário:' + nome + '|]]\n'
	print (linha)
	text = text + linha	

f = open('lista_editores_com_primeira.wiki', 'w')

f.write(text)
f.close()

