import urllib.request
from xml.etree import ElementTree as ET
import re
import unicodedata


ifile = open ('urles.txt', 'r')
paginas=ifile.readlines()
ifile.close()
k=0

text=''
total=0
for pagina in paginas:
#	k=k+1
	if k>10:
		break
	pagina=pagina.strip()
	if len(pagina)>0:
		pos = pagina.find('&')
		pagina = pagina[pos:]
		pos = pagina.find('>') 
		pagina = 'http://plsql1.cnpq.br/divulg/RESULTADO_PQ_102003.prc_comp_cmt_links?V_COD_DEMANDA=200310&V_TPO_RESULT=CURSO'+pagina[:pos]

		print(pagina)	
		bolsistas=0
		page = urllib.request.urlopen(pagina)
		s=page.readlines()
		for line in s:
#			line=line.decode("latin-1")
			LineText=str(line.decode("latin-1"))

		#	print(str(line),"\n")
			pos = LineText.find('<td WIDTH="203" VALIGN="TOP"><font size="2" face="Arial">')
			if pos>0:
				Name = LineText[pos+57:]
				pos = Name.find('<') 
				Name = Name[:pos]
				bolsistas = bolsistas + 1
				text=text+Name.strip()+"\n"
		total=total+bolsistas
		print (bolsistas,total)

ofile = open ('bolsistas.txt', 'w')
ofile.write(text)
ofile.close()


#table = ET.XML(s)
#rows = iter(table)
#headers = [col.text for col in next(rows)]
#for row in rows:
#    values = [col.text for col in row]
#    print (dict(zip(headers, values)))
