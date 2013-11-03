class Board():
	def __init__(self,rows,cols): 	#Recieve the no of rows and columns in the game area
	        
		self.nrows=rows
		self.ncols=cols
		self.matrix=[]
		self.create_matrix()
		
		self.row_boundaries=[]	#A list of row boundary cells
		self.col_boundaries=[]	#A list of column boundaries
		self.corners=[]		#A list of corner cells

		
		
		
	def create_matrix(self):	#Create a list that stores tuples. First value is status and the second value is no of live neighbours
			self.matrix=[[[0,0]]*self.ncols for x in range(self.nrows)]	#initialise to 0. Every cell is dead
			return self.matrix			
		

	
    	
		
		 		
