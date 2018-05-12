#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import urllib
import ast
import json
from datetime import datetime


#pywikibot
import pywikibot
from pywikibot import pagegenerators
from pywikibot.pagegenerators import GeneratorFactory, parameterHelp


def get_views(verbete):
	url = 'https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/pt.wikipedia/all-access/all-agents/'+verbete+'/monthly/2017050100/2018043000'
	resposta = requests.get(url, headers={"User-Agent": 'Fabio'} )

	dados=''
	for r in resposta:
		dados = dados +r

	dados = ast.literal_eval(dados).get('items')

	views = 0
	for j in dados:
		views = views + j.get('views')


	return views


def get_history(verbete):
	site = pywikibot.Site('pt', 'wikipedia')
	page = pywikibot.Page(pywikibot.getSite(), verbete)

	historia=page.getVersionHistory(reverse=True)
	#print(len(historia)) #número de edições



	hoje = datetime.strptime('2018-05-01 00:00:00', '%Y-%m-%d %H:%M:%S')
	tempo =  (hoje - historia[0][1]).total_seconds()  #data da primeira edição
	tempo = int(tempo / (3600*24)) #tempo em dias da criação até 1 de maio de 2018
	return [len(historia), tempo]




#[nr, tempo] = get_history('casa')
#print(tempo)
#quit()


ifile = open('lista_abc_ambos.json')
tabela = json.loads(ifile.read())
ifile.close()

nova_tabela=[]

for name, link, birth, field, desde, nacionalidade, genero, verbete in tabela:
#	print (name, link, birth, field, desde, nacionalidade, verbete, genero)
	if verbete == '':
		views = 0
		numero_de_revisoes = 0
		dias_desde_criacao = 0
	else:
		views = get_views(verbete)
		[numero_de_revisoes, dias_desde_criacao] = get_history(verbete)
		print(name, verbete, views, dias_desde_criacao)

	nova_tabela.append([name, link, birth, field, desde, nacionalidade, verbete, genero, views, numero_de_revisoes, dias_desde_criacao])


f = open('lista_com_dados_do_artigo.json', 'w')
json.dump(nova_tabela, f)
f.close()
