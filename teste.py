# -*- coding: utf-8 -*-
import wikipedia
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')
wikipedia.set_lang("pt")


def isfemale(pg):
	for cat in pg.categories:
		if cat[10:18]=='Mulheres':
			return True
		
	n_mulher_morta=sumario.find(" foi uma ")
	n_mulher_viva=sumario.find(" é uma ")
	n_homem_morto=sumario.find(" foi um ")
	n_homem_vivo=sumario.find(" é um ")
	if n_mulher_morta>0 or n_mulher_viva>0:
		return True
	if n_homem_morto>0 or n_homem_vivo>0:
		return True


lista=['Marie Curie', 'Márcia Barbosa', 'Jônathas de Barros Nunes', 'Albert Einstein']

for verbete in lista:
	pg = wikipedia.page(verbete)
	sumario=pg.summary
	print(verbete,isfemale(pg))



#	print(n_mulher_morta,	n_mulher_viva,	n_homem_morto,	n_homem_vivo)






