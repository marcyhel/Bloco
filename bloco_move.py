import pygame

import random
from bloco import *
from tabuleiro import *
class BlocoMove(Bloco):
	def __init__(self,tab,x,y,alt,larg,dir=0):
		super().__init__(tab,x,y,alt,larg,tipo=3)
	def update(self):

		if(self.dir==0):
			pass
			#print(self.mover(self.dir))
			#self.x+=1
			#self.rect = pygame.Rect(self.x,self.y,self.larg,self.alt)
