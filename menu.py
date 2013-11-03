import wx
from game import Game
from display import Display
class MainMenu:
	def __init__(self,width,height):
		self.main_menu=wx.App()	
		self.run_value=0
		self.frame=wx.Frame(None,0,'Main Menu',style=wx.CAPTION|wx.CLOSE_BOX,size=(width,height))
		self.panel=wx.Panel(self.frame,1)
		wx.StaticText(self.panel,1,'Select the dimension of the Game matrix ',(width/2-100,height/2-100))
		self.slider=wx.SpinCtrl(self.panel,2,' ',(width/2-25,height/2-40),(50,20))
		self.slider.SetRange(4,20)
		self.slider.SetValue(4)
		self.continous=False
		self.button=wx.Button(self.panel,1,'RUN',(width/2-25,height/2),size=(50,50))	#The Run button
		self.tbutton=wx.ToggleButton(self.panel,2,'Continous Mode',(width/2-80,height/2+80),size=(160,50))	
		self.panel.Bind(wx.EVT_TOGGLEBUTTON,self.continous_mode,id=2)
		self.panel.Bind(wx.EVT_BUTTON,self.run_game,id=1)				#Calls the run_game function when button pressed
		self.frame.Show()
		self.main_menu.MainLoop()
		
		
	def run_game(self,temp):	#temp is there to recieve whatever stuff the function call sent along. Some sort of handler i guess
					#Interpreter throws an argument error without the temp
					#Clicking the run button initialises the display, which inturn initialises everything else	
		
			dimension=self.slider.GetValue()
			Display(400,400,dimension,dimension,self.continous)	
	def continous_mode(self,temp):
		
		if self.continous==False:
			self.continous=True
			self.tbutton.SetBackgroundColour((102,178,255))
		else:
			self.continous=False
			self.tbutton.SetBackgroundColour((255,255,255))
		


