import pygame

import random
from bloco import *
from tabuleiro import *
class BlocoDuplica(Bloco):
	def __init__(self,tab,x,y,alt,larg,dir=0):

		super().__init__(tab,x,y,alt,larg,tipo=5,dir=dir)
	def update(self):	
		self.att=True

		if(self.dir==0):
			if(not self.verifica_move(self.xx-1,self.yy)):
				self.empurra(self.dir,self.xx+1,self.yy)
		elif(self.dir==1):
			if(not self.verifica_move(self.xx,self.yy-1)):
				self.empurra(self.dir,self.xx,self.yy+1)
		elif(self.dir==2):
			if(not self.verifica_move(self.xx+1,self.yy)):
				self.empurra(self.dir,self.xx-1,self.yy)
		elif(self.dir==3):
			if(not self.verifica_move(self.xx,self.yy+1)):
				self.empurra(self.dir,self.xx,self.yy-1)
		
		#self.mover(self.dir)
			
		self.duplica_bloco_de_tras(self.dir)
		#self.x+=1
		#self.rect = pygame.Rect(self.x,self.y,self.larg,self.alt)
