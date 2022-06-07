import pygame as py
from config import *

class Personagem(py.sprite.Sprite):
	def __init__(self,pos,grupos,colisao_sprites):
		super().__init__(grupos)
		self.image = py.Surface((blocos_tam // 2,blocos_tam))
  		#self.image = py.image.load('pulo2.png')
									#deixar em 32 px 
		self.image.fill(personagem_cor)
		self.rect = self.image.get_rect(topleft = pos)

		# movimentacao
		self.direcao = py.math.Vector2()#[x:0
                                        # y:0]
		self.velocidade = 6
		self.gravidade = 0.6
		self.pulo_velocidade = 14
	
		self.colisao_sprites = colisao_sprites
		self.dentro_chao = False
  

	def entrada_dados(self):
     
		tecla = py.key.get_pressed()

		if tecla[py.K_RIGHT]:    #[x:1
			self.direcao.x = 1   # y:0]
   
   
		elif tecla[py.K_LEFT]:   # [x:1
			self.direcao.x = -1  #  y:0]
   
		else:
			self.direcao.x = 0   # [x: 1
	   		                     #  y: 0]


		if tecla[py.K_SPACE] and self.dentro_chao:
			self.direcao.y = -self.pulo_velocidade

	def colisao_horizontal(self):
     
		for sprite in self.colisao_sprites.sprites():
			if sprite.rect.colliderect(self.rect):
				if self.direcao.x < 0: 
					self.rect.left = sprite.rect.right
				if self.direcao.x > 0: 
					self.rect.right = sprite.rect.left

	def colisao_vertical(self):
     
		for sprite in self.colisao_sprites.sprites():
      
			if sprite.rect.colliderect(self.rect):
				if self.direcao.y > 0:
					self.rect.bottom = sprite.rect.top

					#Respawn
					self.direcao.y = 0
					self.dentro_chao = True
     
				if self.direcao.y < 0:
					self.rect.top = sprite.rect.bottom
					
					#Respawn
					self.direcao.y = 0

		if self.dentro_chao and self.direcao.y != 0:
			self.dentro_chao = False

	def usar_gravidade(self):
		self.direcao.y += self.gravidade
		self.rect.y += self.direcao.y

	def update(self):
		self.entrada_dados()
		self.rect.x += self.direcao.x * self.velocidade
		self.colisao_horizontal()
		self.usar_gravidade()
		self.colisao_vertical()