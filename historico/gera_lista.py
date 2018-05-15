#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

from datetime import datetime

import requests
import urllib
import ast
import json


def primeira_edicao(usuario):
	usuario = urllib.quote(usuario.encode('utf-8'))
	url='https://pt.wikipedia.org/w/api.php?action=query&list=usercontribs&ucuser=' + usuario + '&uclimit=1&ucdir=newer&format=json'
	resposta = requests.get(url, headers={"User-Agent": 'Fabio'} )

	
	dados = ''
	for r in resposta:
		dados = dados +r
#	print dados
	try:
		dados = json.loads(dados).get('query').get('usercontribs')[0].get('timestamp')
		return dados
#		return datetime.strptime(dados, '%Y-%m-%dT%H:%M:%SZ') # json não gosta de datetime
	except:
		return ''
ifile = open('lista_editores2.json')
lista = json.loads(ifile.read())
ifile.close()

total = 0
limiar = 0
novalista=[]
for nome, contagem, registro in lista:
	if contagem >= limiar:
		total = total + 1

n=0
for nome, contagem, registro in lista:
	if contagem >= limiar:
		n = n+1
		primeira_vez = primeira_edicao(nome)
		print n, primeira_vez, nome, contagem, registro,'  ',round(100*n/total,2)
		novalista.append ([primeira_vez, nome, contagem, registro])
#		break		
#		if primeira_vez == '':
#			break
f = open('lista_editores_com_primeira_um.json', 'w')
json.dump(novalista, f)
f.close()

