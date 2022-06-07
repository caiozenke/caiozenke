import pygame as py
from config import *
from blocos import Blocos
from personagem import Personagem

class Level:
	def __init__(self):

		#Base
		self.exibir= py.display.get_surface()

		#sprites group
		self.ver_sprites = Camera()
        #desenhar sprites
		self.ativa_sprites =py.sprite.Group()
        #update sprites
		self.colisao_sprites =py.sprite.Group()
        #colisão sprites
		self.level_base()

	def level_base(self):
		for lin_indice,linha in enumerate(mapa):
            #print (f'{lin_indice}:{linha}-->{lin_indice * blocos_tam}')
			for col_indice,coluna in enumerate(linha):
				y= lin_indice * blocos_tam
				x= col_indice * blocos_tam
				if coluna == 'X':
					Blocos((x,y),[self.ver_sprites,self.colisao_sprites])
				if coluna == 'P':
					self.personagem = Personagem((x,y),[self.ver_sprites,self.ativa_sprites],self.colisao_sprites)

	def run(self):
		# run the entire game (level)
		self.ativa_sprites.update()
		self.ver_sprites.desenhar_dif(self.personagem)

class Camera(py.sprite.Group):
	def __init__(self):
		super().__init__()
		
		self.exibir = py.display.get_surface()
		self.deslocar = py.math.Vector2(100,300)

		# center camera setup 
		# self.half_w = self.display_surface.get_size()[0] // 2
		# self.half_h = self.display_surface.get_size()[1] // 2

		# camera
		cam_esquerda = camera_borda['esquerda']
		cam_top = camera_borda['top']
		cam_largura = self.exibir.get_size()[0] - (cam_esquerda + camera_borda['direita'])
		cam_altura = self.exibir.get_size()[1] - (cam_top + camera_borda['baixo'])

		self.camera_rect = py.Rect(cam_esquerda,cam_top,cam_largura,cam_altura)

	def desenhar_dif(self,personagem):

		

		# getting the camera position
		if personagem.rect.left < self.camera_rect.left:
			self.camera_rect.left = personagem.rect.left
		if personagem.rect.right > self.camera_rect.right:
			self.camera_rect.right = personagem.rect.right
		if personagem.rect.top < self.camera_rect.top:
			self.camera_rect.top = personagem.rect.top
		if personagem.rect.bottom > self.camera_rect.bottom:
			self.camera_rect.bottom = personagem.rect.bottom

		# camera deslocar 
		self.deslocar = py.math.Vector2(
			self.camera_rect.left - camera_borda['esquerda'],
			self.camera_rect.top - camera_borda['top'])

		for sprite in self.sprites():
			deslocar_pos = sprite.rect.topleft - self.deslocar
			self.exibir.blit(sprite.image,deslocar_pos)
