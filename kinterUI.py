from tkinter import *  
from tkinter.ttk import Progressbar  
from tkinter import ttk
import random  
  

class StarMerchant:
	def __init__(self, master):
		self.master = master
		master.title("Star Merchant 1.0t")

		self.main_frame = Frame(master, bg="gray")
		self.main_frame.pack(expand = True, fill=BOTH)

	def greet(self):
		n = str(random.randint(0, 1000))
		self.label["text"] = n
		self.master.update()


root = Tk()
root.geometry("400x400")
App = StarMerchant(root)
root.mainloop()