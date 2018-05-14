#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

from datetime import datetime

import requests
import urllib
import ast
import json


ifile = open('lista_editores_com_primeira_cinquenta.json')
lista = json.loads(ifile.read())
ifile.close()

total = 0
limiar = 50

ano_atual = ''
lista = sorted(lista, key = lambda p:p[0])
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
text = ''
n=0
for primeira_vez, nome, contagem, registro in lista:
	ano=primeira_vez[:4]
	if not ano == ano_atual:
		print n
		ano_atual = ano
		n=0
	if contagem >= limiar:
		n = n+1

