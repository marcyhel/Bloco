import pygame

import random
from bloco import *
from bloco_move import *
from bloco_duplica import *
from bloco_estatico import *
from bloco_direcional import *
from bloco_gira import *


class BotaoPlay:
	def __init__(self,tab,x,y,size):
		self.tab=tab
		self.x=x
		self.y=y
		self.size=size
		self.rect = pygame.Rect(self.x,self.y,self.size,self.size)
		self.press=False
		self.cont_press=0
		#self.tipo=tipo
		self.sprite= [pygame.transform.scale(pygame.image.load('imagens/b1.png'), (int(self.size), int(self.size))),
		pygame.transform.scale(pygame.image.load('imagens/b2.png'), (int(self.size), int(self.size))),]
	
	def clica(self,pos):

		if(self.rect.collidepoint(pos)):
			self.tab.tab.play= ~ self.tab.tab.play
			
			print("clicado")
	def update(self):
		self.cont_press-=1
		if(self.cont_press<0):
			self.press=False


		
	def render(self,screen):
		
			pygame.draw.rect(screen,(250,250,50), self.rect)