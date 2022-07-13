
import pygame as py
from pygame.locals import *
from sys import exit
import os
from random import *
diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal , 'imagens')
#print(diretorio_principal)


largura = 1200
altura = 720
cor = '#0f5618'


tela = py.display.set_mode((largura , altura))
py.display.set_caption('counter run')

sprite_sheet = py.image.load(os.path.join(diretorio_imagens, 'teste.png')).convert_alpha()
#fundo_img = py.image.load(os.path.join(diretorio_imagens, 'download.jpg')).convert_alpha()
#fundo_img = py.transform.scale(fundo_img,(120*10 , 65*10))

class Rian(py.sprite.Sprite):
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.imagens_perso= []
        for i in range(3):
            img = sprite_sheet.subsurface((i * 32,0),(32,32))
            img = py.transform.scale(img, (32*5, 32*5))
            self.imagens_perso.append(img)
        
        self.index_lista = 0
        self.image =self.imagens_perso[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (100,altura - 120)
    
    def update(self):
        if self.index_lista > 2:
            self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.imagens_perso[int(self.index_lista)]

class Nuvens(py.sprite.Sprite):
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((3*32 , 0), (32,32))
        self.image = py.transform.scale(self.image,(32*5 ,32*5))
        self.rect = self.image.get_rect()
        self.rect.y = randrange(50 ,400 ,50)
        self.rect.x = largura - randrange(30,500 , 30 )

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x= largura
            self.rect.y = randrange(50 ,400 ,50)
        self.rect.x += -10


sprites = py.sprite.Group()


for i in range(4):        
    nuvem = Nuvens()
    sprites.add(nuvem)    

personagem = Rian()
sprites.add(personagem)
tempo = py.time.Clock()

while True:
    tempo.tick(30)
    tela.fill(cor)
    #tela.blit(fundo_img, (0,0))
    
    for event in py.event.get():
        if event.type == QUIT:
            py.quit()
            exit()
        
      

    sprites.draw(tela)
    sprites.update()

    py.display.flip()