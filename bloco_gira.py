import pygame

import random
from bloco import *
from tabuleiro import *
class BlocoGira(Bloco):
	def __init__(self,tab,x,y,alt,larg,dir=0):

		super().__init__(tab,x,y,alt,larg,tipo=8,dir=dir)
	def update(self):
		

		try:
			self.tab.tab_pecas[self.yy][self.xx+1].dir=self.girar(self.dir,self.tab.tab_pecas[self.yy][self.xx+1].dir)
		except:
			pass
		try:
			self.tab.tab_pecas[self.yy][self.xx-1].dir=self.girar(self.dir,self.tab.tab_pecas[self.yy][self.xx-1].dir)
		except:
			pass
		try:
			self.tab.tab_pecas[self.yy+1][self.xx].dir=self.girar(self.dir,self.tab.tab_pecas[self.yy+1][self.xx].dir)
		except:
			pass
		try:
			self.tab.tab_pecas[self.yy-1][self.xx].dir=self.girar(self.dir,self.tab.tab_pecas[self.yy-1][self.xx].dir)
		except:
			pass
		self.att=True

		
		
		#self.mover(self.dir)
			
		#self.duplica_bloco_de_tras(self.dir)
		#self.x+=1
		#self.rect = pygame.Rect(self.x,self.y,self.larg,self.alt)
