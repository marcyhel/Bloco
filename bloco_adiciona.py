import pygame

import random
from bloco import *
from tabuleiro import *
class BlocoAdiciona(Bloco):
	def __init__(self,tab,x,y,alt,larg,dir=0):
		super().__init__(tab,x,y,alt,larg,tipo=9,dir=dir)
		self.mouse=False
		self.listaItems=[3,4,5,6,7,8]
		self.scaleItem=18
		self.listaRectItems=[]
		self.itemSelect=0
		self.bordaSelect=3
		self.att_rect()
		
		self.spriteItens= [
		pygame.transform.scale(pygame.image.load('imagens/0.png'), (int(self.scaleItem), int(self.scaleItem))),
		pygame.transform.scale(pygame.image.load('imagens/1.png'), (int(self.scaleItem), int(self.scaleItem))),
		pygame.transform.scale(pygame.image.load('imagens/2.png'), (int(self.scaleItem), int(self.scaleItem))),
		pygame.transform.scale(pygame.image.load('imagens/3.png'), (int(self.scaleItem), int(self.scaleItem))),
		pygame.transform.scale(pygame.image.load('imagens/4.png'), (int(self.scaleItem), int(self.scaleItem))),
		pygame.transform.scale(pygame.image.load('imagens/5.png'), (int(self.scaleItem), int(self.scaleItem))),
		pygame.transform.scale(pygame.image.load('imagens/6.png'), (int(self.scaleItem), int(self.scaleItem))),
		pygame.transform.scale(pygame.image.load('imagens/7.png'), (int(self.scaleItem), int(self.scaleItem))),
		pygame.transform.scale(pygame.image.load('imagens/8.png'), (int(self.scaleItem), int(self.scaleItem))),
		]
		
	
	def att_rect(self):
		self.listaRectItems=[]
		for i in range(len(self.listaItems)):
			self.listaRectItems.append(pygame.Rect((self.x-50)+i*22,self.y-43,self.scaleItem,self.scaleItem))
	def mouse_cima(self):
		self.mouse=True
		print("mouse cimaaa")
	def mouse_nao_cima(self):
		self.mouse=False
	def render_balao_menu(self,screen):
		if(self.mouse):
			self.att_rect()
			pygame.draw.rect(screen,(100,100,120), pygame.Rect(self.x-60,self.y-60,self.larg+120,self.alt+25))
			pygame.draw.rect(screen,(200,50,50), pygame.Rect(self.listaRectItems[self.itemSelect].x-self.bordaSelect,self.listaRectItems[self.itemSelect].y-self.bordaSelect,self.scaleItem+self.bordaSelect*2,self.scaleItem+self.bordaSelect*2))
			for c,i in enumerate(self.listaItems):
				if(i==3):
			
					#pygame.draw.rect(screen,(50,50,150), self.rect)
					screen.blit( self.spriteItens[0], self.listaRectItems[c])
				elif(i==4):
					#pygame.draw.rect(screen,(190,190,50), self.rect)
					screen.blit( self.spriteItens[1], self.listaRectItems[c])
				elif(i==5):
					#pygame.draw.rect(screen,(190,190,50), self.rect)
					screen.blit( self.spriteItens[2], self.listaRectItems[c])
				elif(i==6):
					#pygame.draw.rect(screen,(190,190,50), self.rect)
					screen.blit( self.spriteItens[3], self.listaRectItems[c])
				elif(i==7):
					#pygame.draw.rect(screen,(190,190,50), self.rect)
					screen.blit( self.spriteItens[5], self.listaRectItems[c])
				elif(i==8):
					
					screen.blit( self.spriteItens[4], self.listaRectItems[c])
				


	def update(self):	
		self.att=True

		
			
		
		#self.x+=1
		#self.rect = pygame.Rect(self.x,self.y,self.larg,self.alt)
