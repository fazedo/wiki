from __future__ import division

#pywikibot
import pywikibot
from pywikibot import pagegenerators
from pywikibot.pagegenerators import GeneratorFactory, parameterHelp

#distance between strings
from difflib import SequenceMatcher

#strings:
import string

#combibations of sets
import itertools

#json
import json


import unicodedata
import datetime




###
#stackoverflow:begin
import re
import unicodedata

def StripAccents(text):
    """
    Strip accents from input String.
    :param text: The input string.
    :type text: String.
    :returns: The processed String.
    :rtype: String.
    """
    try:
        text = unicode(text, 'utf-8')
    except NameError: # unicode is a default on python 3 
        pass
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)
#Stackoverflow:end


def CompareFullNames(FullName, Name):
	NameList1 = StripAccents(FullName).split()
	NameList2 = StripAccents(Name).split()

	if '(' in NameList1[-1]:
		NameList1.pop()

	if '(' in NameList2[-1]:
		NameList2.pop()

	if len(NameList2) > len (NameList1): 
		return 0

	lenght = min(len(NameList1), len(NameList2))

	MaxScore = 0
	for l in [lenght]:
		for Combination1 in itertools.combinations(NameList1, l): 
			for  Combination2 in itertools.combinations(NameList2, l): 
				Score = 0
				MatchedWords = 0
				for k in range(0, l):			
					WordScore = SequenceMatcher(None,Combination1[k],Combination2[k]).ratio()
					if WordScore > .7: #A arbitrary number
						Score = Score + WordScore
						MatchedWords = MatchedWords + 1
				if MatchedWords==l:
					MaxScore = max (MaxScore, Score)
				
	

	return MaxScore


def CompareNames(Name1, Name2):
	NameList1 = StripAccents(Name1).split()
	NameList2 = StripAccents(Name2).split()

	if '(' in NameList1[-1]:
		NameList1.pop()

	if '(' in NameList2[-1]:
		NameList2.pop()

	lenght = min(len(NameList1), len(NameList2))

	MaxScore = 0
	for l in range(2, lenght+1):
		for Combination1 in itertools.combinations(NameList1, l): 
			for  Combination2 in itertools.combinations(NameList2, l): 
				Score = 0
				MatchedWords = 0
				for k in range(0, l):			
					WordScore = SequenceMatcher(None,Combination1[k],Combination2[k]).ratio()
					if WordScore > .5: #A arbitrary number
						Score = Score + WordScore
						MatchedWords = MatchedWords + 1
				Score = Score -  (lenght - MatchedWords) * 0.7  #A arbitrary penalization factor  
				MaxScore = max (MaxScore, Score)
				
	
	return MaxScore - abs (len(NameList1) - len(NameList2) ) * 0.2  #A arbitrary penalization factor



#Look for articles about someone, treat search suggestions (no ideia how to retrieve them)
def HasArticle(FullName):
	total=10 #number of pages we are retrieving from Wikipedia
	#print (FullName)
	gen = pagegenerators.SearchPageGenerator(query=FullName, site=site, namespaces=[0], total=total)
	ArticleList = []

	#Redirects = pagegenerators.RedirectFilterPageGenerator(gen, no_redirects=False)

	#Get list of titles and sring distance from FullName 	
	for Article in gen:
		ArticleTitle = Article.title()
		Score = CompareFullNames(FullName, ArticleTitle)
		ArticleList.append ((Article, ArticleTitle, Score))
		#print(ArticleTitle)

	SortedArticleList = sorted (ArticleList, key = lambda ArticleList:-ArticleList[2])
	#print(SortedArticleList)ret

	#print(ArticleList)
	if SortedArticleList == []:
		return False

	BestScore = SortedArticleList [0][2]
	#print (BestScore)

	#Magic number
	if BestScore < 1.5:
		return False
	return SortedArticleList [0][1]







###


meses = {'jan':1, 'fev':2, 'mar':3, 'abr':4, 'mai':5, 'jun':6, 'jul':7, 'ago':8, 'set':9, 'out':10, 'nov':11, 'dez':12}
def parse(gender):
	for number, name, link, birth, field, obs in Table:
#		print (birth)	
		pos = birth.find(' ')
		birth = birth[pos+1:]
		pos = birth.find(' ')
		dia = int(birth[:pos].replace('º',''))
		if dia>0:	
			pos = birth.find('de')
			mes = meses.get(birth[pos+3:pos+6].lower())
			ano = int(birth[pos+10:pos+14])
			#birth = datetime.datetime(ano, mes, dia)
			birth = [ano, mes, dia] 
		else:
			mes = 0
			ano = 0
			birth = None

		Article = name #HasArticle (name) ############## 
		if Article == False:
			print (name, "  XXXX")
			ArticleName = 'X'
		else:
			print (name, "s",Article.title())
#			NumberOfExistingArticles = NumberOfExistingArticles + 1
			ArticleName = Article



		NewTable.append([number, gender, name, link, birth, field, obs, ArticleName])
	


site = pywikibot.Site('pt', 'wikipedia')



NewTable=[]
ifile = open('lista_abc_masculino.json', 'r')
Table = json.loads(ifile.read())
ifile.close()

parse('M')

ifile = open('lista_abc_feminino.json', 'r')
Table = json.loads(ifile.read())
ifile.close()
parse('F')


print (len(NewTable))

#print(NewTable)
quit()
ofile=open('tabela_com_sugestoes.json','w')
json.dump(NewTable, ofile)
ofile.close()
