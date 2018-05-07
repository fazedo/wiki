from __future__ import division

import json
import urllib
#import urllib.request
import unicodedata



#from urllib.request import FancyURLopener


class AppURLopener(urllib.FancyURLopener):
    version = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)     Chrome/37.0.2049.0 Safari/537.36'

	

def GetPageViews (ArticleTitle):

	nome='https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/de.wikipedia/all-access/user/Johann_Wolfgang_von_Goethe/daily/2017050100/2018105701'



	print (nome)

	
	urllib._urlopener = AppURLopener()
	response = urllib.request.urlopen(nome)
	
	return response.pageread() #pageread().decode("utf-8")

	#page  = MyOpener().open (nome)

	print(page)	

	return
	req = urllib.Request(nome)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)     Chrome/37.0.2049.0 Safari/537.36')

ifile = open('tabela_com_links.json')
table=json.loads(ifile.read())
ifile.close()
k=0
numero_f=0
numero_m=0

numero_f_com_art=0
numero_m_com_art=0

print(GetPageViews(''))

quit()
for number, gender, name, link, birth, field, obs, ArticleName in table:
	k=k+1
	print (k,number, name)
	if gender == 'M':
		numero_m = numero_m + 1
		if not ArticleName.strip() == '':
			numero_m_com_art = numero_m_com_art +1	
	if gender == 'F':
		numero_f = numero_f + 1
		if not ArticleName.strip() == '':
			numero_f_com_art = numero_f_com_art +1	
	

print(numero_f, numero_f_com_art, numero_f, "{:.2f}".format(100*numero_f_com_art/ numero_f)+'%')
print(numero_m, numero_m_com_art, "{:.2f}".format(100*numero_m_com_art/ numero_m)+'%' )

