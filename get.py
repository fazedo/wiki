# -*- coding: utf-8 -*-

#pywikibot
import pywikibot
from pywikibot import pagegenerators
from pywikibot.pagegenerators import GeneratorFactory, parameterHelp

#distance between strings
from difflib import SequenceMatcher

#strings:
import string


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


def DecomposeName(Name):
	pos = Name.find(" ")
	if pos<0:
		FirstName = Name
		return [FirstName, "", ""]

	FirstName = Name[:pos]
	Name = Name[pos+1:]

	pos=Name.find("(")
	if pos<0:
		FamilyName = Name
		return [FirstName, FamilyName, ""]

	FamilyName = Name[:pos-1]
	Complement = Name[pos+1:-1]

	return [FirstName, FamilyName, Complement]

#Compare names giving greater weight to first name and disconsidering accents.
def CompareNames(Name_1, Name_2):
	NameParts_1=DecomposeName(StripAccents(Name_1))
	NameParts_2=DecomposeName(StripAccents(Name_2))
	return (SequenceMatcher(None,NameParts_1[0],NameParts_2[0]).ratio()+SequenceMatcher(None,NameParts_1[1],NameParts_2[1]).ratio())/2.0


#Look for articles about someone, treat search suggestions (no ideia how to retrieve them)
def HasArticle(FullName, KeyWords):
	total=100 #number of pages we are looking for in Wikipedia
	#print (FullName)
	gen = pagegenerators.SearchPageGenerator(query=FullName, site=site, namespaces=[0], total=total)
	ArticleList=[]

	#Get list of titles and sring distance from FullName 	
	for Article in gen:
		ArticleTitle = Article.title()
		Score = CompareNames(ArticleTitle,FullName)
		ArticleList.append ((Article, ArticleTitle, Score))

	SortedArticleList = sorted (ArticleList, key = lambda ArticleList:-ArticleList[2])

	#print(ArticleList)
	if SortedArticleList == []:
		return False
	#Set threshold to analyse ArticleText
	BestScore = SortedArticleList [0][2]

	#Magic number
	Threshold = BestScore * 0.8

	#print (BestScore)

	for i in range(0,len(ArticleList)):
		Score = SortedArticleList[i][2]
		if Score<Threshold:
			break
		#print(Score)
		ArticleText=SortedArticleList[i][0].text.lower()

	#Must contain at least one keyword
		for key in KeyWords:
			if key.lower() in ArticleText:
				return True


	return False



site = pywikibot.Site('pt', 'wikipedia')

keywords=["universidade", "pesquisa", "cientista", "física", "química", "matemática", "biolog", "geolog", "botanica"]

nome = "Márcia Barbosa"
nome = "Adriana Neumann"


print(HasArticle(nome, keywords))

i = 0 # esse i é só para não ser eterno aqui
achou=False


#print (i)]
#print (DecomposeName("Fábio Souto de Azevedo (ff)"))
