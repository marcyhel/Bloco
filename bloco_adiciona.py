import pygame

import random
from bloco import *
from tabuleiro import *
class BlocoAdiciona(Bloco):
	def __init__(self,tab,x,y,alt,larg,dir=0,config=[]):
		super().__init__(tab,x,y,alt,larg,tipo=9,dir=dir,config=config)
		self.mouse=False
		self.listaItems=[3,4,5,6,7,8]
		self.scaleItem=18
		self.listaRectItems=[]
		self.itemSelect=0
		self.verifica_config()
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
	def verifica_config(self):
		if(len(self.config)!=0):
			self.itemSelect=self.config[0]
	def att_config(self):
		self.config=[self.itemSelect]
	def att_rect(self):
		self.listaRectItems=[]
		for i in range(len(self.listaItems)):
			self.listaRectItems.append(pygame.Rect((self.x-50)+i*22,self.y-43,self.scaleItem,self.scaleItem))
	def mouse_cima(self):
		self.mouse=True
	
	def mouse_nao_cima(self):
		self.mouse=False

	def rola_cima(self):
		if(self.mouse):
			
			self.itemSelect+=1
			if(self.itemSelect>=len(self.listaItems)):
				self.itemSelect=0

			self.att_config()
	def rola_baixo(self):
		if(self.mouse):
			
			self.itemSelect-=1
			if(self.itemSelect<0):
				self.itemSelect=len(self.listaItems)-1
			self.att_config()
	def render_balao_menu(self,screen):
		if(self.mouse and not self.select):
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
				

	def add_item(self,x,y):
		self.tab.add_peca(x,y,self.listaItems[self.itemSelect],dir=self.dir)
		self.tab.tab_pecas[y][x].att=True
	def update(self):	
		#print(self.config)
		self.att=True
		if(self.dir==0):
			if(not self.verifica_tab(self.xx-1,self.yy)  and (self.xx-1 >=0 and self.xx-1 <len(self.tab.tab_pecas[0])) and (self.yy >=0 and self.yy <len(self.tab.tab_pecas))):
				self.empurra(self.dir,self.xx+1,self.yy)
				if(self.verifica_move(self.xx+1,self.yy)):
					self.add_item(self.xx+1,self.yy)
		elif(self.dir==1):
			if(not self.verifica_move(self.xx,self.yy-1) and (self.xx >=0 and self.xx <len(self.tab.tab_pecas[0])) and (self.yy-1 >=0 and self.yy-1 <len(self.tab.tab_pecas))):
				self.empurra(self.dir,self.xx,self.yy+1)
				if(self.verifica_move(self.xx,self.yy+1)):
					self.add_item(self.xx,self.yy+1)
		elif(self.dir==2):
			if(not self.verifica_move(self.xx+1,self.yy)  and (self.xx+1 >=0 and self.xx+1 <len(self.tab.tab_pecas[0])) and (self.yy >=0 and self.yy <len(self.tab.tab_pecas))):
				self.empurra(self.dir,self.xx-1,self.yy)
				if(self.verifica_move(self.xx-1,self.yy)):
					self.add_item(self.xx-1,self.yy)
		elif(self.dir==3):
			if(not self.verifica_move(self.xx,self.yy+1)  and (self.xx >=0 and self.xx <len(self.tab.tab_pecas[0])) and (self.yy+1 >=0 and self.yy+1 <len(self.tab.tab_pecas))):
				self.empurra(self.dir,self.xx,self.yy-1)
				if(self.verifica_move(self.xx,self.yy-1)):
					self.add_item(self.xx,self.yy-1)
		
			
		
		#self.x+=1
		#self.rect = pygame.Rect(self.x,self.y,self.larg,self.alt)
