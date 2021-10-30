import pygame
from enum import Enum
import random
from bloco import *
from tabuleiro import *
from botao import *
from botao_play import *


class Estados(Enum):
	jogando=0
	menu=1
class Main:
	def __init__(self):

		self.resolucao=[1000,700]
		pygame.init()
		self.screen = pygame.display.set_mode(self.resolucao)
		self.clock = pygame.time.Clock()
		self.done=False
		self.estado=Estados.jogando
		self.cont_Update=0
		self.tab=Tabuleiro(self,25,18,deslocaMundo=[100,50],resolucao=self.resolucao)

		self.botoes=[BotaoPlay(self,50,600,50),Botao(self,20,30,50,9),Botao(self,20,100,50,3),Botao(self,20,170,50,5),Botao(self,20,240,50,6),Botao(self,20,310,50,7),Botao(self,20,390,50,8),Botao(self,20,460,50,4)]

	def render(self,screen):
		self.tab.render(screen)
		for i in self.botoes:
			
			i.render(screen)
	def update(self):
		self.cont_Update+=1
		if(self.cont_Update>=20):
			self.tab.update()
			self.cont_Update=0

		for i in self.botoes:
			
			i.update()
	def rodar(self):
		while not self.done:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.done=True
				if event.type == pygame.KEYDOWN :

					
					if event.scancode == 79:
						pass
					if event.scancode == 80:
						pass
				if event.type == pygame.KEYUP:
					if event.scancode == 79:
						pass
					if event.scancode == 80:
						pass
				if (event.type == pygame.MOUSEBUTTONUP):
					pos = pygame.mouse.get_pos()
					if(self.estado ==Estados.jogando):
						self.tab.solta(pos)
						try:
							self.tab.peca_flutua_botao.solta(pos)
							print('soltou')
							self.tab.peca_flutua_botao=0
							
						except :
							pass
				if (event.type == pygame.MOUSEBUTTONDOWN):

					if event.button == 4:
						print('rola Cima')
						self.tab.rola_cima(pos)
						#play.RolarItem('cima')
					elif event.button == 5:
						print('rola Baixo')
						self.tab.rola_baixo(pos)
						#play.RolarItem('baixo')
				
					

					pos = pygame.mouse.get_pos()
					
					if(self.estado ==Estados.jogando):
						if ( pygame.mouse.get_pressed()[0]):
							print("direito")
							self.tab.clica(pos)
							
								
							for i in self.botoes:
								i.clica(pos)
							#play.attacar()
						if ( pygame.mouse.get_pressed()[2]):
							self.tab.clica_direito(pos)
							#print(pygame.mouse.get_pressed())
							print('esquerda')
							#play.attacar()

			if(self.estado ==Estados.jogando):
				pos = pygame.mouse.get_pos()
				self.tab.rasta(pos)
				try:
					self.tab.peca_flutua_botao.rasta(pos)
					
				except :
					pass
				try:
					self.tab.mouse_cima(pos)
					
				except :
					pass
			self.screen.fill((10,10,10))
			self.clock.tick(60)


			self.render(self.screen)
			self.update()



			font = pygame.font.Font(None, 30)
			fps = font.render("fps: "+str(int(self.clock.get_fps())), True, pygame.Color('white'))
			self.screen.blit(fps, (50, 50))
			
			
			
			pygame.display.update()
		pygame.quit()

a=Main()
a.rodar()