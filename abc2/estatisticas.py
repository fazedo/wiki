#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from datetime import datetime

import requests
import urllib
import ast
import json
from datetime import datetime



ifile = open('lista_com_dados_do_artigo.json')
tabela = json.loads(ifile.read())
ifile.close()

MulherBrasil = 0
HomemBrasil = 1
MulherEst = 2
HomemEst = 3

total = [0, 0, 0, 0]
art = [0, 0, 0, 0]
view = [0, 0, 0, 0]
dias = [0, 0, 0, 0]

idade = [0, 0, 0, 0]
com_idade = [0, 0, 0, 0]

mdesde = [0, 0, 0, 0]
com_desde = [0, 0, 0, 0]

idade_com_art = [0, 0, 0, 0]
com_idade_com_art = [0, 0, 0, 0]

mdesde_com_art = [0, 0, 0, 0]
com_desde_com_art = [0, 0, 0, 0]

tabela_total = {'Mulher_brasileira':0, 'Mulher_estrangeira':0, 'Homem_brasileiro':0, 'Homem_estrangeiro':0   }
tabela_com_artigo = {'Mulher_brasileira':0, 'Mulher_estrangeira':0, 'Homem_brasileiro':0, 'Homem_estrangeiro':0   }


n = 0
for name, link, birth, field, desde, nacionalidade, verbete, genero, views, numero_de_revisoes, dias_desde_criacao in tabela:
	n = n+1
	if verbete == '':
		v = 0
	else:
		v = 1

	brasil = 'brasil' in nacionalidade.lower()

	if genero == 'M' and brasil:
		indice = HomemBrasil 
	
	if genero == 'F' and brasil:
		indice = MulherBrasil

	if genero == 'M' and not brasil:
		indice = HomemEst

	if genero == 'F' and not brasil:
		indice = MulherEst
		
	total[indice] = total[indice] + 1
	art[indice] = art[indice] + v
	view[indice] = view[indice] + views
	dias[indice] = dias[indice] + dias_desde_criacao

	if not birth[2] == 0:
		data = str(birth[0])+'-'+str(birth[1])+'-'+str(birth[2])
		data = datetime.strptime(data, '%d-%m-%Y')

		hoje = datetime.strptime('2018-05-01 00:00:00', '%Y-%m-%d %H:%M:%S')
		tempo =  (hoje - data).total_seconds()  
		tempo = int(tempo / (3600*24*365.25)) 
		idade[indice] = idade[indice] + tempo
		com_idade[indice] = com_idade[indice] + 1

		idade_com_art[indice] = idade_com_art[indice] + tempo * v
		com_idade_com_art[indice] = com_idade_com_art[indice] + v
		


	if not desde == []:

		data = str(desde[0])+'-'+str(desde[1])+'-'+str(desde[2])
		data = datetime.strptime(data, '%d-%m-%Y')
		hoje = datetime.strptime('2018-05-01 00:00:00', '%Y-%m-%d %H:%M:%S')
		tempo =  (hoje - data).total_seconds()  
		tempo = int(tempo / (3600*24*365.25)) 
		mdesde[indice] = mdesde[indice] + tempo
		com_desde[indice] = com_desde[indice] + 1

		mdesde_com_art[indice] = mdesde_com_art[indice] + tempo * v
		com_desde_com_art[indice] = com_desde_com_art[indice] + v
			
	
print(n, total[0] + total[1] + total[2] + total[3])
		

#print(total,art)

nome = ['Pesquisadoras brasileiras', 'Pesquisadores brasileiros', 'Pesquisadoras estrangeiras', 'Pesquisadores estrangeiros']

for i, p in enumerate(nome):	
	texto = p +': '+str(art[i]) + ' de ' + str(total[i])+ ' (' + "{:.2f}".format(100*art[i]/total[i]) + '%). Views:' + "{:.0f}".format(view[i]/art[i]) 
	texto = texto + '. idade_media: ' + "{:.0f}".format(idade[i]/com_idade[i])
	texto = texto + '. tempo_medio: ' + "{:.0f}".format(mdesde[i]/com_desde[i])
	texto = texto + '. idade_media_com_art: ' + "{:.0f}".format(idade_com_art[i]/com_idade_com_art[i])
	texto = texto + '. tempo_medio_com_art: ' + "{:.0f}".format(mdesde_com_art[i]/com_desde_com_art[i])
	texto = texto + '. dias: ' + "{:.0f}".format(dias[i]/art[i])

	print texto 



#f = open('lista_com_dados_do_artigo.json', 'w')
#json.dump(tabela, f)
#f.close()
