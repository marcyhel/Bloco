import pygame
from bloco import *
from bloco_move import *
class Tabuleiro:
	def __init__(self,root,larg,alt,deslocaMundo=[0,0],resolucao=(600,600)):
		self.root=root 
		self.tab = []
		self.tab_pecas = []
		self.alt = alt
		self.larg = larg
		self.grade=resolucao[0]/40
		self.resolucao = resolucao
		self.deslocaMundo=deslocaMundo
		self.inicializa()
		
		self.area_move(inix=0,fimx=3,iniy=0,fimy=5)
		self.area_move(inix=5,fimx=9,iniy=6,fimy=9)
		self.add_peca(2,3,3)
		self.add_peca(9,1,3)
		self.add_peca(2,1,4)
	def inicializa(self):
		for i in range(self.alt):
			aux=[]
			aux2=[]
			for j in range(self.larg):
				aux.append(Bloco(self,j*self.grade+self.deslocaMundo[0],i*self.grade+self.deslocaMundo[1],self.grade-1,self.grade-1))
				aux2.append(Bloco(self,j*self.grade+self.deslocaMundo[0],i*self.grade+self.deslocaMundo[1],self.grade-1,self.grade-1,tipo=0))
			self.tab_pecas.append(aux2)
			self.tab.append(aux)
	def add_peca(self,x,y,tipo):
		if(tipo==3):
			self.tab_pecas[y][x]=BlocoMove(self,self.tab_pecas[y][x].x,self.tab_pecas[y][x].y,self.tab_pecas[y][x].alt,self.tab_pecas[y][x].larg)
		if(tipo==0):
			self.tab_pecas[y][x]=Bloco(self,self.tab_pecas[y][x].x,self.tab_pecas[y][x].y,self.tab_pecas[y][x].alt,self.tab_pecas[y][x].larg,tipo=0)
		if(tipo==4):
			self.tab_pecas[y][x]=Bloco(self,self.tab_pecas[y][x].x,self.tab_pecas[y][x].y,self.tab_pecas[y][x].alt,self.tab_pecas[y][x].larg,tipo=4)
	def area_move(self,inix=0,iniy=0,fimx=0,fimy=0):
		for i in range(iniy,fimy):
			
			for j in range(inix,fimx):
				self.tab[i][j].tipo=2
	def rasta(self,pos):
		for i in self.tab_pecas:
			for j in i:
				if(j.tipo>=3):
					if(j.select):
						j.rasta(pos)
	def solta(self,pos):	
		for i in self.tab_pecas:
			for j in i:
				if(j.select):
					j.solta(pos)
				

	def clica(self,pos):
		for i in self.tab_pecas:
			for j in i:
				if(j.tipo>=3):
					if(j.rect.collidepoint(pos)):
						j.seleciona()
	
	def update(self):
		for i in self.tab_pecas:
			for j in i:
				
				j.update()
					
	def render(self,screen):
		for i in self.tab:
			for j in i:
				j.render(screen)
		#aux pra renderizar o item arrastado em primeiro plano
		aux=0
		for i in self.tab_pecas:
			for j in i:
				if(j.select):
					aux=j
				j.render(screen)
		if(aux!=0):
			aux.render(screen)