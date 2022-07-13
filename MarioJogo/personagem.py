import pygame as py

from config import *

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal , 'imagens')

class Personagem(py.sprite.Sprite):
	def __init__(self,pos,grupos,colisao_sprites):
		super().__init__(grupos)

		sprite_sheet = py.image.load(os.path.join(diretorio_imagens, 'dino.png')).convert_alpha()
		self.imagens_perso= []
		for i in range(4):
			img = sprite_sheet.subsurface((i * 32,0),(32,32))
			img = py.transform.scale(img, (32*3, 32*3))
			self.imagens_perso.append(img)
		self.index_lista = 0

		self.image =self.imagens_perso[self.index_lista]
		self.rect = self.image.get_rect(topleft = pos)
		self.rect.center = (100,tela_altura - 120)
									#deixar em 32 px 
		

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