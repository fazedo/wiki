#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

import requests
import urllib
import ast
import json


lista = []
aufrom = ''
limit = '500'
while True:
	url = 'https://pt.wikipedia.org/w/api.php?action=query&list=allusers&auwitheditsonly&aulimit=' + limit + '&format=json&auprop=editcount|registration&auexcludegroup=bot&aufrom=' + aufrom


	resposta = requests.get(url, headers={"User-Agent": 'Fabio'} )

	dados = ''
	for r in resposta:
		dados = dados +r

	dados = json.loads(dados)
	
	aufrom = dados.get('continue')
	if aufrom == None:
		aufrom = None
	else:
		aufrom = aufrom.get('aufrom')
	allusers = dados.get('query').get('allusers')

	for p in allusers:
		if p.get('editcount')>=50:
			print p.get('name'), p.get('editcount'), p.get('registration')
			lista.append ([p.get('name'), p.get('editcount'), p.get('registration')])
	if aufrom == None:
		break

f = open('lista_editores2.json', 'w')
json.dump(lista, f)
f.close()

