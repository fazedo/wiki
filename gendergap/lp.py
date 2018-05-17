#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

import requests
import urllib
import ast
import json



def pega_lista():
	lista = []
	aufrom = ''
	limit = '500'
	number = 0
	limiar = 0
	gender = ''
	while True:
		url = 'https://'+lingua+'.wikipedia.org/w/api.php?action=query&list=allusers&auwitheditsonly&aulimit=' + limit + '&format=json&auprop=editcount|registration&auexcludegroup=bot&auactiveusers&aufrom=' + aufrom


		resposta = requests.get(url, headers={"User-Agent": 'Fabio'} )

		dados = ''
		for r in resposta:
			dados = dados +r

		dados = json.loads(dados)
	

		allusers = dados.get('query').get('allusers')

		for p in allusers:
			if p.get('editcount')>=limiar:
				number = number + 1
				lista.append ([p.get('userid'), p.get('name'), p.get('editcount'), p.get('registration'), gender])
		print number

		aufrom = dados.get('continue')
		if aufrom == None:
			break
		else:
			aufrom = aufrom.get('aufrom')

#		break

	print "Foram encontrados " + str(number) + " editores."


	return lista

def pega_genero(fatia_lista):
	tamanho_lote = 50
	inicio = 0
	if len(fatia_lista) > tamanho_lote:
		raise 'Tamanho de lote excedido.'


	male = 0
	female = 0
	total = 0


	nomes = ''
	for p in fatia_lista:
		nomes = nomes + '|'+ urllib.quote(p[1].encode('utf-8'))			

	nomes = nomes[1:] #tira '|' inicial

	url = 'https://'+lingua+'.wikipedia.org/w/api.php?action=query&list=users&ususers=' + nomes + '&usprop=editcount|registration|gender&format=json'

	resposta = requests.get(url, headers={"User-Agent": 'Fabio Tools: fazedo@gmail.com'} )

	dados = ''
	for r in resposta:
		dados = dados + r

	dados = json.loads(dados).get('query').get('users')


	for index, usuario in enumerate(dados):
		gender = usuario.get ('gender')
		if gender == 'male':
			male = male + 1
		if gender == 'female':
			female = female + 1
		total = total + 1
#		print usuario.get ('name'), usuario.get ('gender'), usuario.get('editcount')
#		print usuario.get ('name'), fatia_lista[index][1]
		fatia_lista[index][4] = gender 

#		print male, female, total
#	break

n=0

gera_lista = True
lingua ='sv'
if gera_lista:
	lista = pega_lista()
	f = open('lista_editores_ativos_'+lingua+'.json', 'w')
	json.dump(lista, f)
	f.close()
else:
	f = open('lista_editores_ativos_'+lingua+'.json', 'r')
	lista = json.loads(f.read())
	f.close()


total = len(lista)
while True:
	lista = sorted (lista, key = lambda p:p[4])
	if lista[0][4] == '':
		try:
			pega_genero(lista[0:50])
		except:
			raise "não deu"

		f = open('lista_editores_ativos_'+lingua+'.json', 'w')
		json.dump(lista, f)
		f.close()
		n=n+50
		print 'Salvo. '+str(n),' de '+str(total)
	
	else:
		break
	

print lista[0:3]
quit()





