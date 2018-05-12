#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import urllib
import ast

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

verbete='João Doria'

print get_views(verbete)
