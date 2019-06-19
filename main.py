def main():
	if not DEBUG:
		root = Tk()
		root.title('Load Flow')
		app = PowerFlowGUI.GUI(root)
		root.mainloop()
	else:
		network = pandapower.create_empty_network()
		pf = PowerFlow.PowerFlow(readFile, writeFile)
		pf.run(network)

if __name__ == '__main__':
	DEBUG = False

	if DEBUG:
		import pandapower
		import PowerFlow
		readFile = 'debug_input_looped.xlsx'
		writeFile = 'debug_output_looped.xlsx'
	else:
		from tkinter import Tk 
		import PowerFlowGUI

	main()