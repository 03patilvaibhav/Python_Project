import pygame
from settings import screen_width, screen_height
from game_data import Module

class Module:
	def __init__(self,current_module,surface,create_overworld2):

		# Module setup
		self.display_surface = surface
		self.current_module = current_module
		module_data = Module[current_module]
		module_content = module_data['content']
		self.new_max_module = module_data['unlock']
		self.create_overworld2 = create_overworld2

		# level display
		self.font = pygame.font.Font(None,40)
		self.text_surf = self.font.render(module_content,True,'White')
		self.text_rect = self.text_surf.get_rect(center = (screen_width / 2, screen_height / 2))

	def input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_RETURN]:
			self.create_overworld2(self.current_module,self.new_max_module)
		if keys[pygame.K_ESCAPE]:
			self.create_overworld2(self.current_module,0)

	def run(self):
		self.input()
		self.display_surface.blit(self.text_surf,self.text_rect)
