import pygame

import random
from bloco import *
from tabuleiro import *
class BlocoEstatico(Bloco):
	def __init__(self,tab,x,y,alt,larg,dir=0):

		super().__init__(tab,x,y,alt,larg,tipo=6,dir=dir)
	def update(self):
		pass	
		#self.att=True

		
		
		#self.mover(self.dir)
			
		#self.duplica_bloco_de_tras(self.dir)
		#self.x+=1
		#self.rect = pygame.Rect(self.x,self.y,self.larg,self.alt)
