import pandas

class Element:
	def __init__(self):
		self.input = None
		self.output = None

	def readData(self, file, sheetName):
		self.input = pandas.read_excel(file, sheetName)
		self.input.dropna()

	def createElement(self, network):
		pass

	def updateResults(self, results):
		self.output = results

	def writeData(self, writer, sheetName):
		if not self.output.empty:
			self.output.to_excel(writer, sheetName)