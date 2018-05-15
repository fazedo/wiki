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
number = 0
limiar = 0
while True:
	url = 'https://pt.wikipedia.org/w/api.php?action=query&list=allusers&auwitheditsonly&aulimit=' + limit + '&format=json&auprop=editcount|registration&auexcludegroup=bot&auactiveusers&aufrom=' + aufrom


	resposta = requests.get(url, headers={"User-Agent": 'Fabio'} )

	dados = ''
	for r in resposta:
		dados = dados +r

	dados = json.loads(dados)
	

	allusers = dados.get('query').get('allusers')

	for p in allusers:
		if p.get('editcount')>=limiar:
			number = number + 1
			lista.append ([p.get('name'), p.get('editcount'), p.get('registration')])
	print number

	aufrom = dados.get('continue')
	if aufrom == None:
		break
	else:
		aufrom = aufrom.get('aufrom')


print "Foram encontrados " + str(number) + " editores."


###Pega gênero
tamanho_lote = 50
inicio = 0

novalista=[]
male = 0
female = 0
total = 0

while True:
	fim = min (inicio + tamanho_lote, number)
	nomes = ''
	for p in lista[inicio:fim]:
		nomes = nomes + '|'+ urllib.quote(p[0].encode('utf-8'))			

	nomes =nomes[1:]	
#	url = 'https://pt.wikipedia.org/w/api.php?action=query&list=users&ususers='+nomes+'&usprop=gender&format=json'
	url = 'https://pt.wikipedia.org/w/api.php?action=query&list=users&ususers=' + nomes + '&usprop=editcount|registration|gender&format=json'
#	print url
	resposta = requests.get(url, headers={"User-Agent": 'Fabio'} )

	dados = ''
	for r in resposta:
		dados = dados + r

	dados = json.loads(dados).get('query').get('users')

#	print dados
#	print len(dados)

	for usuario in dados:
		gender = usuario.get ('gender')
		if gender == 'male':
			male = male + 1
		if gender == 'female':
			female = female + 1
		total = total + 1
#		print usuario.get ('name'), usuario.get ('gender'), usuario.get('editcount')
		novalista.append([usuario.get ('name'), usuario.get ('gender'), usuario.get ('editcount')])

		print male, female, total
#	break

	inicio = fim
	if fim  == number:
		break




f = open('lista_editores_ativos.json', 'w')
json.dump(novalista, f)
f.close()

