from tkinter import W, messagebox
from tkinter.ttk import Button, Label, Style
from tkinter.filedialog import askopenfilename

#import numpy.core._methods
#import numpy.lib.format
#from scipy.sparse.csgraph import _validation

import PowerFlow
import pandapower

class GUI():
    
    def __init__(self, root):
        self.root = root
        self.readFilename=''
        self.writeFilename=''
        
        self.initUI()
        
        self.rFLabel = Label(self.root)
        self.rFLabel.grid(row=0, column=1, sticky=W, columnspan=2)
        
        self.wFLabel = Label(self.root)
        self.wFLabel.grid(row=1, column=1, sticky=W, columnspan=2)
        
        self.rFButton = Button(self.root, text="Read File",
                               command=self.getReadFileName)
        self.rFButton.grid(row=0, column=0, sticky=W)
        
        self.wFButton = Button(self.root, text="Write File",
                               command=self.getWriteFileName)
        self.wFButton.grid(row=1, column=0, sticky=W)
        
        self.runLFButton = Button(self.root, text="Run Power Flow",
                                  command=self.runLF)
        self.runLFButton.grid(row=3, column=0, sticky=W)
        
    def initUI(self):
        Style().configure("TButton", padding=(0,5,0,5), font='serif 10')
        
        self.root.columnconfigure(0, pad=3)
        self.root.columnconfigure(1, pad=3)
        self.root.columnconfigure(2, pad=3)
        
        self.root.rowconfigure(0, pad=3)
        self.root.rowconfigure(1, pad=3)
        self.root.rowconfigure(2, pad=3)
        
    def getReadFileName(self):
        self.readFilename = askopenfilename()
        self.rFLabel.configure(text=self.readFilename)
        
    def getWriteFileName(self):
        self.writeFilename = askopenfilename()
        self.wFLabel.configure(text=self.writeFilename)
        
    def runLF(self):
        if self.readFilename and self.writeFilename:
            self.root.config(cursor="wait")
            self.root.update()
            
            self.network = pandapower.create_empty_network()
            self.pf = PowerFlow.PowerFlow(self.readFilename, self.writeFilename)
            self.pf.run(self.network)
            
            self.root.config(cursor="")
            messagebox.showinfo("Load Flow", "Complete")
        else:
            messagebox.showerror("Error Message", 
                                 "Missing read/write filepath.")