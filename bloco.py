import pygame
import copy
#0  ->
#1  \/
#2  <-
#3  ^
class Bloco:
	def __init__(self,tab,x,y,alt,larg,dir=0,tipo=1,config=[]):
		self.tab=tab
		self.x = x
		self.y = y
		self.alt = alt
		self.larg = larg
		self.rect = pygame.Rect(self.x,self.y,self.larg,self.alt)
		self.config=config
		self.xx=int((self.x-self.tab.deslocaMundo[0])/self.tab.grade)
		self.yy=int((self.y-self.tab.deslocaMundo[1])/self.tab.grade)
		self.dir=dir
		self.sprite= [pygame.transform.scale(pygame.image.load('imagens/0.png'), (int(self.alt), int(self.alt))),
		pygame.transform.scale(pygame.image.load('imagens/1.png'), (int(self.alt), int(self.alt))),
		pygame.transform.scale(pygame.image.load('imagens/2.png'), (int(self.alt), int(self.alt))),
		pygame.transform.scale(pygame.image.load('imagens/3.png'), (int(self.alt), int(self.alt))),
		pygame.transform.scale(pygame.image.load('imagens/4.png'), (int(self.alt), int(self.alt))),
		pygame.transform.scale(pygame.image.load('imagens/5.png'), (int(self.alt), int(self.alt))),
		pygame.transform.scale(pygame.image.load('imagens/6.png'), (int(self.alt), int(self.alt))),
		pygame.transform.scale(pygame.image.load('imagens/7.png'), (int(self.alt), int(self.alt))),
		pygame.transform.scale(pygame.image.load('imagens/8.png'), (int(self.alt), int(self.alt))),
		]
		self.tipo=tipo
		self.select=False
		self.lembrarPosisao=0
		self.historicoMove=[]
		self.att=False
	def reset(self):
		self.historicoMove=[]
		self.att=False
	def verifica_tab(self,x,y):
		try:
			if(self.tab.tab[y][x].tipo==2 and self.tab.tab_pecas[y][x].tipo==0  and x>=0 and y>=0):
				return True
			else:
				return False
		except:
			return False
	def verifica_move_dir(self,x,y,dir):
		try:
			if(self.tab.tab_pecas[y][x].tipo!=6 ):
				if(self.tab.tab_pecas[y][x].tipo==7):
					if((dir == 0 or dir == 2) and (self.tab.tab_pecas[y][x].dir==1 or self.tab.tab_pecas[y][x].dir ==3)):
						return True
					elif((dir == 1 or dir == 3) and (self.tab.tab_pecas[y][x].dir==0 or self.tab.tab_pecas[y][x].dir ==2)):
						return True
					else:
						return False
					
				else:
					return True
			else:
				return False
		except:
			return False

	def verifica_move(self,x,y):
		
		try:
			if(self.tab.tab_pecas[y][x].tipo==0 and x>=0 and y>=0  ):
				return True
			else:
				return False
		except:
			return False
	def fixa_nova_posi(self,x,y):
		
		self.tab.tab_pecas[y][x]=self
		self.rect = pygame.Rect(x*self.tab.grade+self.tab.deslocaMundo[0],y*self.tab.grade+self.tab.deslocaMundo[1],self.larg,self.alt)
		self.tab.add_peca(self.xx,self.yy,0)
		self.x=x*self.tab.grade+self.tab.deslocaMundo[0]
		
		self.y=y*self.tab.grade+self.tab.deslocaMundo[1]
		self.xx=int((self.x-self.tab.deslocaMundo[0])/self.tab.grade)
		self.yy=int((self.y-self.tab.deslocaMundo[1])/self.tab.grade)

		
	def empurra(self,dir,x,y):
		try:
			if(self.tab.tab_pecas[y][x].tipo!=0):
				#print("d")
				if(dir==0):
					if(self.tab.tab_pecas[y][x].verifica_move(x,y)and self.verifica_move_dir(x,y,dir)):	
						if(self.verifica_move_dir(x,y,dir)):
							self.tab.tab_pecas[y][x].mover(dir)
					else:
						
						
						if(self.verifica_move_dir(x,y,dir)):
							self.tab.tab_pecas[y][x].empurra(dir,x+1,y)
							self.tab.tab_pecas[y][x].mover(dir)
						
				if(dir==1):
					if(self.tab.tab_pecas[y][x].verifica_move(x,y) ):	
							self.tab.tab_pecas[y][x].mover(dir)
					else:
						
						
						if(self.verifica_move_dir(x,y,dir)):
							self.tab.tab_pecas[y][x].empurra(dir,x,y+1)
							self.tab.tab_pecas[y][x].mover(dir)
				if(dir==2):
					if(self.tab.tab_pecas[y][x].verifica_move(x,y) and self.verifica_move_dir(x,y,dir)):	
						if(self.verifica_move_dir(x,y,dir)):
							self.tab.tab_pecas[y][x].mover(dir)
					else:
						
						
						if(self.verifica_move_dir(x,y,dir)):
							self.tab.tab_pecas[y][x].empurra(dir,x-1,y)
							self.tab.tab_pecas[y][x].mover(dir)
				if(dir==3):
					if(self.tab.tab_pecas[y][x].verifica_move(x,y) and self.verifica_move_dir(x,y,dir)):	
						self.tab.tab_pecas[y][x].mover(dir)	
					else:
						
						
						if(self.verifica_move_dir(x,y,dir)):
							self.tab.tab_pecas[y][x].empurra(dir,x,y-1)
							self.tab.tab_pecas[y][x].mover(dir)
			else:
				pass
		except:
			return False

	def duplica_bloco_de_tras(self,dir):
		try:
			if(dir==0):
				if(self.tab.tab_pecas[self.yy][self.xx-1].tipo!=0 and self.verifica_move(self.xx+1,self.yy) and self.xx-1>=0 and self.yy>=0):
				
					self.tab.add_peca(self.xx+1,self.yy,self.tab.tab_pecas[self.yy][self.xx-1].tipo,dir=self.tab.tab_pecas[self.yy][self.xx-1].dir,config=self.tab.tab_pecas[self.yy][self.xx-1].config)
					self.tab.tab_pecas[self.yy][self.xx+1].att=True
				
			if(dir==1):
				if(self.tab.tab_pecas[self.yy-1][self.xx].tipo!=0 and self.verifica_move(self.xx,self.yy+1) and self.xx>=0 and self.yy-1>=0):
					self.tab.add_peca(self.xx,self.yy+1,self.tab.tab_pecas[self.yy-1][self.xx].tipo,dir=self.tab.tab_pecas[self.yy-1][self.xx].dir,config=self.tab.tab_pecas[self.yy-1][self.xx].config)
					self.tab.tab_pecas[self.yy+1][self.xx].att=True
			if(dir==2):
				if(self.tab.tab_pecas[self.yy][self.xx+1].tipo!=0 and self.verifica_move(self.xx-1,self.yy) and self.xx+1>=0 and self.yy>=0):
					self.tab.add_peca(self.xx-1,self.yy,self.tab.tab_pecas[self.yy][self.xx+1].tipo,dir=self.tab.tab_pecas[self.yy][self.xx+1].dir,config=self.tab.tab_pecas[self.yy][self.xx+1].config)
					self.tab.tab_pecas[self.yy][self.xx-1].att=True
			if(dir==3):
				if(self.tab.tab_pecas[self.yy+1][self.xx].tipo!=0 and self.verifica_move(self.xx,self.yy-1) and self.xx>=0 and self.yy+1>=0):
					self.tab.add_peca(self.xx,self.yy-1,self.tab.tab_pecas[self.yy+1][self.xx].tipo,dir=self.tab.tab_pecas[self.yy+1][self.xx].dir,config=self.tab.tab_pecas[self.yy+1][self.xx].config)
					self.tab.tab_pecas[self.yy-1][self.xx].att=True
		except:
			pass
		
		
	def mover(self,dir):
		#print(self.dir)
		try:
			if(dir==0):
				#print(dir)
				if(self.verifica_move(self.xx+1,self.yy) and dir not in self.historicoMove ):
					
					self.fixa_nova_posi(self.tab.tab_pecas[self.yy][self.xx+1].xx,self.tab.tab_pecas[self.yy][self.xx+1].yy)
					self.historicoMove.append(dir)
					return True
				else:
					pass
					#print("não pode mover {}".format(self.tipo))
			elif(dir==1):
				#print(dir)
				if(self.verifica_move(self.xx,self.yy+1) and dir not in self.historicoMove ):
					
					self.fixa_nova_posi(self.tab.tab_pecas[self.yy+1][self.xx].xx,self.tab.tab_pecas[self.yy+1][self.xx].yy)
					self.historicoMove.append(dir)
					return True
				else:
					pass#print("não pode mover {}".format(self.tipo))
			elif(dir==2):
				#print(dir)
				if(self.verifica_move(self.xx-1,self.yy) and dir not in self.historicoMove ):
					
					self.fixa_nova_posi(self.tab.tab_pecas[self.yy][self.xx-1].xx,self.tab.tab_pecas[self.yy][self.xx-1].yy)
					self.historicoMove.append(dir)
					return True
				else:
					pass#print("não pode mover {}".format(self.tipo))
			elif(dir==3):
				#print(dir)
				if(self.verifica_move(self.xx,self.yy-1) and dir not in self.historicoMove ):
					
					self.fixa_nova_posi(self.tab.tab_pecas[self.yy-1][self.xx].xx,self.tab.tab_pecas[self.yy-1][self.xx].yy)
					self.historicoMove.append(dir)
					return True
				else:
					pass#print("não pode mover {}".format(self.tipo))
		except:
			return False
	def girar(self,dir,new):
		if(dir ==0 or dir==2):
			if(new +1>3):
				return 0
			return new +1
		if(dir ==1 or dir==3):
			if(new -1<0):
				return 3
			return new -1

	def seleciona(self):

		#xx=int((self.x-self.tab.deslocaMundo[1])/self.tab.grade)
		#yy=int((self.y-self.tab.deslocaMundo[0])/self.tab.grade)
		if(self.tab.tab[self.yy][self.xx].tipo==2):
			self.select=True
			self.lembrarPosisao=self.rect

	def clica_direito(self):
		self.dir=self.girar(0,self.dir)
	def solta(self,pos):
		self.select=False
		x=int((pos[0]-self.tab.deslocaMundo[0])/self.tab.grade)
		y=int((pos[1]-self.tab.deslocaMundo[1])/self.tab.grade)

		
		if(self.verifica_tab(x,y)):
			
			
			self.fixa_nova_posi(x,y)
		else:
			self.rect=self.lembrarPosisao
	def rotacao_sprite(self):
		if(self.dir==0):
			return 0
		elif(self.dir==1):
			return -90
		elif(self.dir==2):
			return -180
		elif(self.dir==3):
			return -270
	def rasta(self,pos):
		#print(pos)
		self.rect = pygame.Rect(pos[0]-self.alt/2,pos[1]-self.larg/2,self.larg,self.alt)
	def render_balao_menu(self,screen):
		pass
	def mouse_cima(self):
		pass
		
	def mouse_nao_cima(self):
		pass
	def rola_cima(self):
		pass
	def rola_baixo(self):
		pass
	def update(self):
		pass
	def render(self,screen):
		if(self.tipo==1):
			#pygame.draw.rect(screen,(50,50,50), self.rect)
			screen.blit( pygame.transform.rotate(self.sprite[6], self.rotacao_sprite()), self.rect)
			
		elif(self.tipo==2):
			#pygame.draw.rect(screen,(150,150,150), self.rect)
			screen.blit( pygame.transform.rotate(self.sprite[7], self.rotacao_sprite()), self.rect)
		elif(self.tipo==3):
			
			#pygame.draw.rect(screen,(50,50,150), self.rect)
			screen.blit( pygame.transform.rotate(self.sprite[0], self.rotacao_sprite()), self.rect)
		elif(self.tipo==4):
			#pygame.draw.rect(screen,(190,190,50), self.rect)
			screen.blit( pygame.transform.rotate(self.sprite[1], self.rotacao_sprite()), self.rect)
		elif(self.tipo==5):
			#pygame.draw.rect(screen,(190,190,50), self.rect)
			screen.blit( pygame.transform.rotate(self.sprite[2], self.rotacao_sprite()), self.rect)
		elif(self.tipo==6):
			#pygame.draw.rect(screen,(190,190,50), self.rect)
			screen.blit( pygame.transform.rotate(self.sprite[3], self.rotacao_sprite()), self.rect)
		elif(self.tipo==7):
			#pygame.draw.rect(screen,(190,190,50), self.rect)
			screen.blit( pygame.transform.rotate(self.sprite[5], self.rotacao_sprite()), self.rect)
		elif(self.tipo==8):
			#pygame.draw.rect(screen,(190,190,50), self.rect)
			if(self.dir ==0 or self.dir == 2):
				screen.blit( self.sprite[4], self.rect)
			else:
				screen.blit(pygame.transform.flip(self.sprite[4], True, False), self.rect)
		elif(self.tipo==9):
			#pygame.draw.rect(screen,(190,190,50), self.rect)
			self.render_balao_menu(screen)
			screen.blit( pygame.transform.rotate(self.sprite[8], self.rotacao_sprite()), self.rect)

		
		
