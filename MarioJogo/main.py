import pygame as py            
import sys
from config import * 
from level import Level

py.init()

tela = py.display.set_mode((tela_largura,tela_altura))
#Definição das Larguras e Alturas Locaclizadas Na Config 


py.display.set_caption('Counter Run by OSCRIAS')
level = Level()
tempo = py.time.Clock()
rodando= True
while rodando:
    for event in py.event.get():
        if event.type == py.QUIT:
            rodando=0
            py.quit()
            sys.exit()
        
    tela.fill((back_cor))
    level.run()
    py.display.update()
    tempo.tick(75)
    
    """Colocando os  metodos em loop para funcionamento do Codigo """