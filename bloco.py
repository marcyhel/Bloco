import pygame
import copy
class Bloco:
	def __init__(self,tab,x,y,alt,larg,dir=0,tipo=1):
		self.tab=tab
		self.x = x
		self.y = y
		self.alt = alt
		self.larg = larg
		self.rect = pygame.Rect(self.x,self.y,self.larg,self.alt)
		self.dir=dir
		self.tipo=tipo
		self.select=False
		self.lembrarPosisao=0
	def verifica_tab(self,x,y):
		
		try:
			
			if(self.tab.tab[y][x].tipo==2 and self.tab.tab_pecas[y][x].tipo==0):
			
				return True
			else:
				
				return False
		except:
			
			return False
	def fixa_nova_posi(self,x,y):
		
		self.tab.tab_pecas[y][x]=self
		xx=int((self.x-self.tab.deslocaMundo[1])/self.tab.grade)
		yy=int((self.y-self.tab.deslocaMundo[0])/self.tab.grade)
		self.tab.add_peca(xx,yy,0)
		self.x=x*self.tab.grade+self.tab.deslocaMundo[0]
		self.y=y*self.tab.grade+self.tab.deslocaMundo[0]
	def seleciona(self):

		xx=int((self.x-self.tab.deslocaMundo[1])/self.tab.grade)
		yy=int((self.y-self.tab.deslocaMundo[0])/self.tab.grade)
		if(self.tab.tab[yy][xx].tipo==2):
			self.select=True
			self.lembrarPosisao=self.rect
	def solta(self,pos):
		self.select=False
		x=int((pos[0]-self.tab.deslocaMundo[0])/self.tab.grade)
		y=int((pos[1]-self.tab.deslocaMundo[1])/self.tab.grade)

		
		if(self.verifica_tab(x,y)):
			
			self.rect = pygame.Rect(x*self.tab.grade+self.tab.deslocaMundo[0],y*self.tab.grade+self.tab.deslocaMundo[1],self.larg,self.alt)
			self.fixa_nova_posi(x,y)
		else:
			self.rect=self.lembrarPosisao
	def rasta(self,pos):
		#print(pos)
		self.rect = pygame.Rect(pos[0]-self.alt/2,pos[1]-self.larg/2,self.larg,self.alt)
	def update(self):
		pass
	def render(self,screen):
		if(self.tipo==1):
			pygame.draw.rect(screen,(50,50,50), self.rect)
			
		elif(self.tipo==2):
			pygame.draw.rect(screen,(150,150,150), self.rect)
		elif(self.tipo==3):
			pygame.draw.rect(screen,(50,50,150), self.rect)
		elif(self.tipo==4):
			pygame.draw.rect(screen,(190,190,50), self.rect)