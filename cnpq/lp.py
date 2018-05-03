import urllib.request
from xml.etree import ElementTree as ET
import re
import unicodedata
import json

ifile = open ('urles.txt', 'r')
paginas=ifile.readlines()
ifile.close()
k=0

text=''
total=0
tabela=[]
for pagina in paginas:
#	k=k+1
	if k>4:
		break
	pagina=pagina.strip()
	if len(pagina)>0:

		pos = pagina.find('ASSESSOR')+12
		area = pagina[pos:]
		pos = area.find('<')
		if pos>0:
			area=area[:pos]
		print(area) 

		pos = pagina.find('&')
		pagina = pagina[pos:]
		pos = pagina.find('>') 
		pagina = 'http://plsql1.cnpq.br/divulg/RESULTADO_PQ_102003.prc_comp_cmt_links?V_COD_DEMANDA=200310&V_TPO_RESULT=CURSO'+pagina[:pos]

		print(pagina)	
		bolsistas=0
		page = urllib.request.urlopen(pagina)
		s=page.readlines()
		for line in s:

			LineText=str(line.decode("latin-1"))

		#	print(str(line),"\n")
			pos = LineText.find('<td WIDTH="203" VALIGN="TOP"><font size="2" face="Arial">')
			if pos>0:
				Nome = LineText[pos+57:]
				pos = Nome.find('<') 
				Nome = Nome[:pos].strip()
				bolsistas = bolsistas + 1
				text=text + Nome+"\n"

			pos = LineText.find('<td WIDTH="25" VALIGN="TOP"><font size="2" face="Arial">')
			if pos>0:
				Nivel = LineText[pos+56:]
				pos = Nivel.find('<') 
				Nivel = Nivel[:pos].strip()

			pos = LineText.find('<td WIDTH="41" VALIGN="TOP"><font size="2" face="Arial">')
			if pos>0:
				data1 = LineText[pos+56:]
				pos = data1.find('<') 
				data1 = data1[:pos].strip()
				
			pos = LineText.find('<td WIDTH="53" VALIGN="TOP"><font size="2" face="Arial">')
			if pos>0:
				data2 = LineText[pos+56:]
				pos = data2.find('<') 
				data2 = data2[:pos].strip()

			pos = LineText.find('<td WIDTH="75" VALIGN="TOP"><font size="2" face="Arial">')
			if pos>0:
				instituicao = LineText[pos+56:]
				pos = instituicao.find('<') 
				instituicao = instituicao[:pos].strip()
				print(Nome, Nivel, data1, data2, instituicao, area)
				tabela.append ([Nome, Nivel, data1, data2, instituicao, area])



		total=total+bolsistas
		print (bolsistas,total)



f = open('tabela_bolsistas.txt', 'w')
json.dump(tabela, f)
f.close()

#print(tabela)
#ofile = open ('bolsistas_tabela.txt', 'w')
#ofile.write(tabela)
#ofile.close()


#table = ET.XML(s)
#rows = iter(table)
#headers = [col.text for col in next(rows)]
#for row in rows:
#    values = [col.text for col in row]
#    print (dict(zip(headers, values)))
