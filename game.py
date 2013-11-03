#This is the main game file
from init import Board
from compute import ComputeNeighbours,Generate

class Game:
	def __init__(self,row,col):
		self.nrows=row			#Number of rows and columns in the game screen 
		self.ncols=col

		#Board is a class. The next line initialises Board by supplying it with the no of rows and columns and returns the matrix
		#The matrix, here, refers to the mathematical matrix which can be compared to the graphical screen divided into rows and columns
		self.matrix=Board(row,col).create_matrix()
		
			
	def compute_next(self):
		
		
		self.matrix=ComputeNeighbours(self.matrix,self.nrows,self.ncols).neighbour_count()
		self.matrix=Generate(self.matrix,self.nrows,self.ncols).update_cell()
		
		return self.matrix
		
	def return_matrix(self):
		return self.matrix
		

	def input_update(self,circle_list):
		self.matrix=Generate(self.matrix,self.nrows,self.ncols).read_cell(circle_list)
		self.compute_next()		
		#self.display() 	#Displays the matrix. Each cell is represented by a 2 membered list in the terminal.
		

		circle_list=Generate(self.matrix,self.nrows,self.ncols).circle_updater()
		return circle_list
		
		
	     	
		
			
	
	def display(self):
		for x in range(self.nrows):
			print self.matrix[x]
		print " "
				


