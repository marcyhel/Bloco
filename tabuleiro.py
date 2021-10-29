import pygame
from bloco import *
from bloco_move import *
from bloco_duplica import *
from bloco_estatico import *
from bloco_direcional import *
from bloco_gira import *

import random
class Tabuleiro:
	def __init__(self,root,larg,alt,deslocaMundo=[0,0],resolucao=(600,600)):
		self.root=root 
		self.tab = []
		self.tab_pecas = []
		self.alt = alt
		self.larg = larg
		self.grade=int(resolucao[0]/35)
		self.resolucao = resolucao
		self.deslocaMundo=deslocaMundo
		self.peca_flutua_botao=0
		self.play=False
		self.inicializa()
		
		self.area_move(inix=0,fimx=25,iniy=0,fimy=18)
		self.area_move(inix=5,fimx=9,iniy=6,fimy=9)
		self.add_peca(0,3,3,dir=0)
		self.add_peca(5,0,3,dir=1)
		#for i in range(5):
		#	self.add_peca(random.randint(0,8),random.randint(0,8),3,dir=random.randint(0,3))
		self.add_peca(2,2,4)
		self.add_peca(4,3,4)
		self.add_peca(8,3,4)

		self.add_peca(9,8,4)
		self.add_peca(11,8,4)

		self.add_peca(10,8,5,dir=1)
		#self.add_peca(15,8,5,dir=0)
		#self.add_peca(15,15,6,dir=0)
		#self.add_peca(15,19,7,dir=0)
		#self.add_peca(18,19,7,dir=1)
		#self.add_peca(10,19,8,dir=0)
		#self.add_peca(0,19,8,dir=1)
	def inicializa(self):
		for i in range(self.alt):
			aux=[]
			aux2=[]
			for j in range(self.larg):
				aux.append(Bloco(self,j*self.grade+self.deslocaMundo[0],i*self.grade+self.deslocaMundo[1],self.grade-1,self.grade-1))
				aux2.append(Bloco(self,j*self.grade+self.deslocaMundo[0],i*self.grade+self.deslocaMundo[1],self.grade-1,self.grade-1,tipo=0))
			self.tab_pecas.append(aux2)
			self.tab.append(aux)
	def add_peca(self,x,y,tipo,dir=0):
		if(tipo==3):
			self.tab_pecas[y][x]=BlocoMove(self,self.tab_pecas[y][x].x,self.tab_pecas[y][x].y,self.tab_pecas[y][x].alt,self.tab_pecas[y][x].larg,dir=dir)
		if(tipo==5):
			self.tab_pecas[y][x]=BlocoDuplica(self,self.tab_pecas[y][x].x,self.tab_pecas[y][x].y,self.tab_pecas[y][x].alt,self.tab_pecas[y][x].larg,dir=dir)
		if(tipo==6):
			self.tab_pecas[y][x]=BlocoEstatico(self,self.tab_pecas[y][x].x,self.tab_pecas[y][x].y,self.tab_pecas[y][x].alt,self.tab_pecas[y][x].larg,dir=dir)
		if(tipo==7):
			self.tab_pecas[y][x]=BlocoDirecional(self,self.tab_pecas[y][x].x,self.tab_pecas[y][x].y,self.tab_pecas[y][x].alt,self.tab_pecas[y][x].larg,dir=dir)
		if(tipo==8):
			self.tab_pecas[y][x]=BlocoGira(self,self.tab_pecas[y][x].x,self.tab_pecas[y][x].y,self.tab_pecas[y][x].alt,self.tab_pecas[y][x].larg,dir=dir)
		if(tipo==0):
			self.tab_pecas[y][x]=Bloco(self,self.tab_pecas[y][x].x,self.tab_pecas[y][x].y,self.tab_pecas[y][x].alt,self.tab_pecas[y][x].larg,tipo=0,dir=dir)
		if(tipo==4):
			self.tab_pecas[y][x]=Bloco(self,self.tab_pecas[y][x].x,self.tab_pecas[y][x].y,self.tab_pecas[y][x].alt,self.tab_pecas[y][x].larg,tipo=4,dir=dir)
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
				
	def clica_direito(self,pos):
		for i in self.tab_pecas:
			for j in i:
				if(j.tipo>=3):
					if(j.rect.collidepoint(pos)):
						j.clica_direito()
	def clica(self,pos):
		for i in self.tab_pecas:
			for j in i:
				if(j.tipo>=3):
					if(j.rect.collidepoint(pos)):
						j.seleciona()
	
	def update(self):
		if(self.play):
			for i in self.tab_pecas:
				for j in i:
					if(j.tipo==8):
						if(not j.att):
							j.update()
			for i in self.tab_pecas:
				for j in i:
					if(j.tipo==5):
						if(not j.att):
							j.update()
			for i in self.tab_pecas:
				for j in i:
					if(not j.att):
						j.update()
			for i in self.tab_pecas:
				for j in i:
					
					j.reset()
					
	def render(self,screen):
		try:
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
		except:
			pass
		try:
			self.peca_flutua_botao.render(screen)
		except:
			pass