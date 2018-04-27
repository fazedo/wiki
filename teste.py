# -*- coding: utf-8 -*-
import wikipedia
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

wikipedia.set_lang("pt")


lista=['Marie Curie', 'Márcia Barbosa', 'Jônathas de Barros Nunes', 'Albert Einstein']#, 'carro', 'lista']

for verbete in lista:
	pg = wikipedia.page(verbete)
	sumario=pg.summary
	print(verbete)
	n_mulher_morta=sumario.find(" foi uma ")
	n_mulher_viva=sumario.find(" é uma ")
	n_homem_morto=sumario.find(" foi um ")
	n_homem_vivo=sumario.find(" é um ")



	print(n_mulher_morta,	n_mulher_viva,	n_homem_morto,	n_homem_vivo)






