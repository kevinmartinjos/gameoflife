class ComputeNeighbours:
	def __init__(self,matrix,nrow,ncol):		#Recieve a particular cell to process
		
		self.nrows=nrow				#No of rows in the game board
		self.ncols=ncol				#No of columns in the game board
		self.matrix=matrix
		self.tempmatrix=matrix			#A matrix to store the intermediate state of the game board
		self.ncount=0				#no of live neighbours for a particular cell
		#self.matrix=self.tempmatrix		#Assigning the calculated matrix (with no of neighbours) to original matrix
	
	def neighbour_count(self):
		for x in range(self.nrows):
			for y in range(self.ncols):
				if (x==0 or x==self.nrows-1) and (y!=0 and y!=self.ncols-1):
					self.tempmatrix[x][y] = [self.matrix[x][y][0],self.col_boundary_calc(x,y)]
				elif (y==0 or y==self.ncols-1) and (x!=0 and x!=self.nrows-1):
					self.tempmatrix[x][y]=[self.matrix[x][y][0],self.row_boundary_calc(x,y)]

				elif (y==0 and x==0) or (y==0 and x==self.nrows-1) or (y==self.ncols-1 and x==0) or (y==self.ncols-1 and x==self.nrows-1):
					self.tempmatrix[x][y]=[self.matrix[x][y][0],self.corner_calc(x,y)]
				else:
					self.tempmatrix[x][y]=[self.matrix[x][y][0],self.normal_calc(x,y)]
		return self.tempmatrix
					

	def col_boundary_calc(self,x,y):		 #If the cell is in the first or last row and not on a corner
			
		if x==0:				 #If the cell is in the first row (except on a corner)
			self.ncount=0			
			if self.matrix[x][y-1][0]==1:
				self.ncount=self.ncount+1		
			if self.matrix[x][y+1][0]==1:
				self.ncount=self.ncount+1
			if self.matrix[x+1][y-1][0]==1:
				self.ncount=self.ncount+1
			if self.matrix[x+1][y][0]==1:
				self.ncount=self.ncount+1
			if self.matrix[x+1][y+1][0]==1:
				self.ncount=self.ncount+1

			return self.ncount
		
		elif x==self.nrows-1:
			self.ncount=0			
			if self.matrix[x][y-1][0]==1:
				self.ncount=self.ncount+1
			if self.matrix[x][y+1][0]==1:
				self.ncount=self.ncount+1
			if self.matrix[x-1][y-1][0]==1:
				self.ncount=self.ncount+1
			if self.matrix[x-1][y][0]==1:
				self.ncount=self.ncount+1
			if self.matrix[x-1][y+1][0]==1:
				self.ncount=self.ncount+1
			return self.ncount
	

	def row_boundary_calc(self,x,y):		#If the cell is in the first or last column and not on a corner
		if y==0:
			self.ncount=0	
			if self.matrix[x-1][y][0]==1:
				self.ncount=self.ncount+1
			if self.matrix[x-1][y+1][0]==1:
				self.ncount=self.ncount+1
			if self.matrix[x][y+1][0]==1:
				self.ncount=self.ncount+1
			if self.matrix[x+1][y][0]==1:
				self.ncount=self.ncount+1
			if self.matrix[x+1][y+1][0]==1:
				self.ncount=self.ncount+1
			return self.ncount
			
		elif y==self.ncols-1:
			self.ncount=0
			if self.matrix[x-1][y][0]==1:
				self.ncount=self.ncount+1
			if self.matrix[x-1][y-1][0]==1:
				self.ncount=self.ncount+1
			if self.matrix[x][y-1][0]==1:
				self.ncount=self.ncount+1
			if self.matrix[x+1][y-1][0]==1:
				self.ncount=self.ncount+1
			if self.matrix[x+1][y][0]==1:
				self.ncount=self.ncount+1
			return self.ncount

	def corner_calc(self,x,y):
		if x==0 :				#Top corners
			self.ncount=0
			if y==0:
				if self.matrix[x][y+1][0]==1:
					self.ncount=self.ncount+1
				if self.matrix[x+1][y][0]==1:
					self.ncount=self.ncount+1
				if self.matrix[x+1][y+1][0]==1:
					self.ncount=self.ncount+1
				return self.ncount
			elif y==self.ncols-1:
				if self.matrix[x][y-1][0]==1:
					self.ncount=self.ncount+1
				if self.matrix[x+1][y][0]==1:
					self.ncount=self.ncount+1
				if self.matrix[x+1][y-1][0]==1:
					self.ncount=self.ncount+1
				return self.ncount
		if x==self.nrows-1:			#Bottom corners
			self.ncount=0			
			if y==0:
				if self.matrix[x][y+1][0]==1:
					self.ncount=self.ncount+1
				if self.matrix[x-1][y][0]==1:
					self.ncount=self.ncount+1
				if self.matrix[x-1][y+1][0]==1:
					self.ncount=self.ncount+1
				return self.ncount
			elif y==self.ncols-1:
				if self.matrix[x][y-1][0]==1:
					self.ncount=self.ncount+1
				if self.matrix[x-1][y][0]==1:
					self.ncount=self.ncount+1
				if self.matrix[x-1][y-1][0]==1:
					self.ncount=self.ncount+1
				return self.ncount
	def normal_calc(self,x,y):
		self.ncount=0
		if self.matrix[x-1][y-1][0]==1:
			self.ncount=self.ncount+1
		if self.matrix[x-1][y][0]==1:
			self.ncount=self.ncount+1
		if self.matrix[x-1][y+1][0]==1:
			self.ncount=self.ncount+1
		if self.matrix[x][y-1][0]==1:
			self.ncount=self.ncount+1
		if self.matrix[x][y+1][0]==1:
			self.ncount=self.ncount+1
		if self.matrix[x+1][y-1][0]==1:
			self.ncount=self.ncount+1
		if self.matrix[x+1][y][0]==1:
			self.ncount=self.ncount+1
		if self.matrix[x+1][y+1][0]==1:
			self.ncount=self.ncount+1
		return self.ncount

	def view_temp_board(self):
		for x in range(self.nrows):
			print self.tempmatrix[x]
		print " "
	def return_matrix(self):
		return self.matrix
		

class Generate:
	def __init__(self,matrix,nrows,ncols):
		self.nrows=nrows
		self.ncols=ncols
		self.matrix=matrix
		self.tempmatrix=matrix
						
		self.matrix=self.tempmatrix
		
	
	def update_cell(self):						#To make cells dead or alive based on no of neighbours
		for x in range(self.nrows):
			for y in range(self.nrows):
				if self.matrix[x][y][1]<=1:		#If no of neighbours is 1 or less
					self.tempmatrix[x][y][0]=0
				#elif self.matrix[x][y][1]==2:		# No change if no of neighbouring cells is 2	
					
				elif self.matrix[x][y][1]==3:		#If there are 3 live neighburs, make dead cell live
					if self.matrix[x][y][0]==0:
						self.tempmatrix[x][y][0]=1
				elif self.matrix[x][y][1]>3:		#If more than 3 live neighbours, cells become dead - overcrowding
					self.tempmatrix[x][y][0]=0	
		return self.tempmatrix	
			

	# read_cell() recieves the circle_list. circle_list contains the row and col no of those cells where there is a green dot
	# read_cell() makes the corresponding cells in the matrix alive (puts a 1 as first value)
	def read_cell(self,circle_list):	
		for x in circle_list:
			self.matrix[x[0]][x[1]]=[1,0]
		return self.matrix

	# After a turn, many cells die and many cells become alive. The list of cells that are alive now are put into the circle list and given 	to the Display class
	# This is because the green dots are put on a cell only if that cell is found in the circle_list under the Display class
	def circle_updater(self):
		circle_list=[]
		for x in range(self.nrows):
			for y in range(self.ncols):
				if self.matrix[x][y][0]==1:
					circle_list.append([x,y])
		return circle_list

	
	
