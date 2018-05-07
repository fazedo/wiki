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

site = pywikibot.Site('pt', 'wikipedia')


page = pywikibot.Page(pywikibot.getSite(), 'Casa')

historia=page.getVersionHistory(reverse=True)
print(len(historia))
print (historia[0])
