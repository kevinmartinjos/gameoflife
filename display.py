import pygame
from pygame.locals import *
import sys
from game import Game
from compute import Generate
class Display:
	def __init__(self,width,height,nrows,ncols,continous_mode):
		self.game_instance=Game(nrows,ncols)	#Initialise the background stuff the game needs
		self.nrows=nrows			#No of rows and columns
		self.ncols=ncols 
		self.continous_mode=continous_mode	#Whether the next generation is rendered automatically or upon user input

		self.cmode_mouse=False			#In continous mode, the program should wait for the user to input the initial 								configuration. After the initial configuration is set, a right click will trigger 								continous updation of the cells 	

		self.width=width			#Width and height of the screen		
		self.height=height
		self.length_x=self.width/self.ncols     #Width of each cell
		self.length_y=self.height/self.nrows	#Height of each cell
		self.circle_list=[]			#To hold the list of cells to be updated (when the user clicks on it)
		pygame.init()
		self.screen=pygame.display.set_mode((self.width,self.height),0,16)
		self.screen.fill((255,255,255))	
		self.render()				#render() puts everything on the screen		
	
	def render(self):
		while True:
			if self.continous_mode==False:
				for event in pygame.event.get():
					if event.type==QUIT:
						pygame.display.quit()
						return
					if event.type==pygame.MOUSEBUTTONDOWN:
						if pygame.mouse.get_pressed()[0]:
							mouse_pos=pygame.mouse.get_pos()
							#Every cell on which the user click is recorded and added to a list of cells
							#Circles (green dots) are drawn inside the cells in the list later
							self.circle_list.append(self.mouse_interact(mouse_pos))
					
						elif pygame.mouse.get_pressed()[2]:
							#Upon right click, the current turn ends. The no of neighbours are calculated and cells updated
											
							self.circle_list=self.game_instance.input_update(self.circle_list)
							self.screen.fill((255,255,255))
				self.draw_lines()
				self.draw_circle()
				pygame.display.update()

			elif self.continous_mode==True:
				pygame.time.Clock().tick(40)
				self.screen.fill((255,255,255))
				for event in pygame.event.get():
					if event.type==QUIT:
						pygame.display.quit()
						return

					if event.type==pygame.MOUSEBUTTONDOWN:
						
						if pygame.mouse.get_pressed()[0]:
							if self.cmode_mouse==False:
								mouse_pos=pygame.mouse.get_pos()
								self.circle_list.append(self.mouse_interact(mouse_pos))
						if pygame.mouse.get_pressed()[2]:
							self.cmode_mouse=True
				self.draw_lines()
				if self.cmode_mouse==True:
				  pygame.time.Clock().tick(5)
				self.draw_circle()
				if self.cmode_mouse:
					self.circle_list=self.game_instance.input_update(self.circle_list)
					
				pygame.display.update()
				



	def draw_lines(self):

		#Divides the screen into a certain no of cells by drawing a number of vertical and horizontal lines
		i=0
		while i<self.ncols:
			pygame.draw.line(self.screen,(0,0,0),(0,self.length_y*i),(self.height,self.length_y*i))
			i=i+1
		i=0
		while i<self.nrows:
			pygame.draw.line(self.screen,(0,0,0),(self.length_x*i,0),(self.length_x*i,self.height))
			i=i+1


	def mouse_interact(self,mouse_pos):
		#mouse_pos[1] is the y coordinate. y cordinate divided by height of each cell will give you the row in which the mouse pointer 			belongs to. Similarly, mouse_pos[0] is the x cordinate. X cordinate divided by width of each cell gives the column in which the 			mouse pointer resides.

		#The return function returns (row number, column number) tuple
		return [mouse_pos[1]/self.length_y,mouse_pos[0]/self.length_x]

	def draw_circle(self):
		
		for x in self.circle_list:
			#circle_list contains tuple in the form (row number, column number)
			#column number * width of each cell gives the x coordinate of the cell .Row no * height of each cell gives the y 				coordinate.
			#x[1] = column number of the xth element in circle_list.
			#x[1]*length_x = x co-ordinate of the cell represented by xth element in circles_list
			#(self.length_x/2) is added to the x co-ordinate to put the circle in the centre of a cell.
			#pygame.draw.circle(self.screen,(0,255,0),(x[1]*self.length_x+(self.length_x/2),x[0]*self.length_y+(self.length_y/2)),5)
			pygame.draw.rect(self.screen,(0,0,0),(x[1]*self.length_x,x[0]*self.length_y,self.length_x,self.length_y))


		
