import pygame

import random
from bloco import *
from bloco_move import *
from bloco_duplica import *
from bloco_estatico import *
from bloco_direcional import *
from bloco_gira import *
from bloco_adiciona import *


class Botao:
	def __init__(self,tab,x,y,size,tipo):
		self.tab=tab
		self.x=x
		self.y=y
		self.size=size
		self.rect = pygame.Rect(self.x,self.y,self.size,self.size)
		self.press=False
		self.cont_press=0
		self.tipo=tipo
		self.sprite= [pygame.transform.scale(pygame.image.load('imagens/b1.png'), (int(self.size), int(self.size))),
		pygame.transform.scale(pygame.image.load('imagens/b2.png'), (int(self.size), int(self.size))),]
	
	def clica(self,pos):

		if(self.rect.collidepoint(pos)):
			if(self.tipo==3):
				self.tab.tab.peca_flutua_botao=BlocoMove(self.tab.tab,self.x,self.y,self.tab.tab.tab_pecas[0][0].alt,self.tab.tab.tab_pecas[0][0].larg,dir=0)
			if(self.tipo==5):
				self.tab.tab.peca_flutua_botao=BlocoDuplica(self.tab.tab,self.x,self.y,self.tab.tab.tab_pecas[0][0].alt,self.tab.tab.tab_pecas[0][0].larg,dir=0)
			if(self.tipo==6):
				self.tab.tab.peca_flutua_botao=BlocoEstatico(self.tab.tab,self.x,self.y,self.tab.tab.tab_pecas[0][0].alt,self.tab.tab.tab_pecas[0][0].larg,dir=0)
			if(self.tipo==7):
				self.tab.tab.peca_flutua_botao=BlocoDirecional(self.tab.tab,self.x,self.y,self.tab.tab.tab_pecas[0][0].alt,self.tab.tab.tab_pecas[0][0].larg,dir=0)
			if(self.tipo==8):
				self.tab.tab.peca_flutua_botao=BlocoGira(self.tab.tab,self.x,self.y,self.tab.tab.tab_pecas[0][0].alt,self.tab.tab.tab_pecas[0][0].larg,dir=0)
			if(self.tipo==9):
				self.tab.tab.peca_flutua_botao=BlocoAdiciona(self.tab.tab,self.x,self.y,self.tab.tab.tab_pecas[0][0].alt,self.tab.tab.tab_pecas[0][0].larg,dir=0)
			if(self.tipo==4):
				self.tab.tab.peca_flutua_botao=Bloco(self.tab.tab,self.x,self.y,self.tab.tab.tab_pecas[0][0].alt,self.tab.tab.tab_pecas[0][0].larg,tipo=4,dir=0)

			self.tab.tab.peca_flutua_botao.select=True
			
			print("clicado")
	def update(self):
		self.cont_press-=1
		if(self.cont_press<0):
			self.press=False


		
	def render(self,screen):
		if(self.tipo==3):
			pygame.draw.rect(screen,(50,50,150), self.rect)
		if(self.tipo==5):
			pygame.draw.rect(screen,(50,150,50), self.rect)
		if(self.tipo==6):
			pygame.draw.rect(screen,(70,70,70), self.rect)
		if(self.tipo==7):
			pygame.draw.rect(screen,(190,190,50), self.rect)
		if(self.tipo==8):
			pygame.draw.rect(screen,(250,100,50), self.rect)
		if(self.tipo==9):
			pygame.draw.rect(screen,(160,50,150), self.rect)
		if(self.tipo==4):
			pygame.draw.rect(screen,(250,250,50), self.rect)