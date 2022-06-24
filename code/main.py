import pygame, sys
from settings import *
from overworld import Overworld
from overworld2 import Overworld2

class Game:
	def __init__(self):
		self.max_level = 2
		self.overworld = Overworld(1, self.max_level, screen, self.create_level)
		self.status = 'overworld'
		self.max_module = 3
		self.overworld2 =Overworld2(1,self.max_module,screen,self.create_module)

	def create_module(self,current_module):
		self.module = Module(current_module,screen,self.create_overworld2)
		self.status = 'module'

	def create_overworld2(self,current_module,new_max_module):
		if new_max_module > self.max_module:
			self.max_module = new_max_module
		self.overworld = Overworld(current_module,self.max_module,screen,self.overworld2)
		self.status = 'overworld'

	def create_level(self,current_level):
		self.level = Level(current_level,screen,self.create_overworld)
		self.status = 'level'

	def create_overworld(self,current_level,new_max_level):
		if new_max_level > self.max_level:
			self.max_level = new_max_level
		self.overworld = Overworld(current_level,self.max_level,screen,self.create_level)
		self.status = 'overworld'

	def run(self):
		if self.status == 'overworld':
			self.overworld.run()
		else:
			self.overworld2.run()

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
game = Game()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
			
	screen.fill('black')
	game.run()

	pygame.display.update()
	clock.tick(60)
