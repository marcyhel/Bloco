import pygame
from enum import Enum
import random
from bloco import *
from tabuleiro import *



class Estados(Enum):
	jogando=0
	menu=1
class Main:
	def __init__(self):

		self.resolucao=(1000,600)
		pygame.init()
		self.screen = pygame.display.set_mode(self.resolucao)
		self.clock = pygame.time.Clock()
		self.done=False
		self.estado=Estados.jogando
		self.cont_Update=0
		self.tab=Tabuleiro(self,20,17,deslocaMundo=[100,100],resolucao=self.resolucao)

	def render(self,screen):
		self.tab.render(screen)
	def update(self):
		self.cont_Update+=1
		if(self.cont_Update>=20):
			self.tab.update()
			self.cont_Update=0
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
				if (event.type == pygame.MOUSEBUTTONDOWN):

					if event.button == 4:
						print('rola Cima')
						#play.RolarItem('cima')
					elif event.button == 5:
						print('rola Baixo')

						#play.RolarItem('baixo')
				
					

					pos = pygame.mouse.get_pos()
					
					if(self.estado ==Estados.jogando):
						if ( pygame.mouse.get_pressed()[0]):
							print("direito")
							self.tab.clica(pos)
							#play.attacar()
						if ( pygame.mouse.get_pressed()[2]):
							#print(pygame.mouse.get_pressed())
							print('esquerda')
							#play.attacar()

			if(self.estado ==Estados.jogando):
				pos = pygame.mouse.get_pos()
				self.tab.rasta(pos)
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