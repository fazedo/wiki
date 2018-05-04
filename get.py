# -*- coding: utf-8 -*-


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
def HasArticle(FullName, KeyWords):
	total=10 #number of pages we are retrieving from Wikipedia
	#print (FullName)
	gen = pagegenerators.SearchPageGenerator(query=FullName, site=site, namespaces=[0], total=total)
	ArticleList = []

	#Redirects = pagegenerators.RedirectFilterPageGenerator(gen, no_redirects=False)

	#Get list of titles and sring distance from FullName 	
	for Article in gen:
		ArticleTitle = Article.title()
		Score = CompareNames(ArticleTitle,FullName)
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
	

	#Set threshold to analyse ArticleText
	Threshold = BestScore * 0.7 #Another Magic Number
	
	for i in range(0,len(ArticleList)):
		
		Score = SortedArticleList[i][2]
		#print(i, Score)
		if Score<Threshold:
			break
		#print(Score)
		ArticleText=StripAccents(SortedArticleList[i][0].text).lower()

		#Must contain at least one keyword
		for key in KeyWords:
			if StripAccents(key).lower() in ArticleText:
				return SortedArticleList[i][0]
	
	return False


site = pywikibot.Site('pt', 'wikipedia')

ifile= open("keywords.txt","r")
lines=ifile.readlines()
ifile.close()

#get keywords
keywords=[]
for line in lines:
	key=line.strip()
	if (not key=='') and (not key[0]=='#'): 
		keywords.append(key)


#get list of researchers to look for
ifile= open("bolsistas.txt","r")
lines=ifile.readlines()
ifile.close()

names=[]
for line in lines:
	name=line.strip()
	if (not name=='') and (not name[0]=='#'): 
		names.append(name)
#print (names)

TotalNumberOfArticles=0
NumberOfExistingArticles=0

for name in names:
	TotalNumberOfArticles = TotalNumberOfArticles + 1
	Article = HasArticle (name, keywords) 
	if Article == False:
		print (name, "  XXXX")
	else:
		print (name, "s",Article.title())
		NumberOfExistingArticles = NumberOfExistingArticles + 1

	print(NumberOfExistingArticles, TotalNumberOfArticles, str(100 * NumberOfExistingArticles / TotalNumberOfArticles) + "%")

#	if TotalNumberOfArticles > 20:
#		break

print(NumberOfExistingArticles, TotalNumberOfArticles, str(100 * NumberOfExistingArticles / TotalNumberOfArticles) + "%")


