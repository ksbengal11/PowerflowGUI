from Element import bus, externalGrid, generator, impedance, line, load, shunt, transformer
import pandas
import pandapower

class PowerFlow():
	def __init__(self, readFile, writeFile):
		self.__readFile = readFile
		self.__writeFile = writeFile

		self.__bus = bus.Bus()
		self.__grid = externalGrid.ExternalGrid()
		self.__gen = generator.Generator()
		self.__imp = impedance.Impedance()
		self.__line = line.Line()
		self.__load = load.Load()
		self.__shunt = shunt.Shunt()
		self.__trafo = transformer.Transformer()

	def readData(self):
		self.__bus.readData(self.__readFile, 'Bus')
		self.__grid.readData(self.__readFile, 'ExternalGrid')
		self.__gen.readData(self.__readFile, 'Generator')
		self.__imp.readData(self.__readFile, 'Impedance')
		self.__line.readData(self.__readFile, 'Line')
		self.__load.readData(self.__readFile, 'Load')
		self.__shunt.readData(self.__readFile, 'Shunt')
		self.__trafo.readData(self.__readFile, 'Transformer')

	def createElement(self, network):
		self.__bus.createElement(network)
		self.__grid.createElement(network)
		self.__gen.createElement(network)
		self.__imp.createElement(network)
		self.__line.createElement(network)
		self.__load.createElement(network)
		self.__shunt.createElement(network)
		self.__trafo.createElement(network)

	def runPowerFlow(self, network):
		pandapower.diagnostic(network)
		pandapower.runpp(net=network, algorithm='nr', max_iteration=10000, numba=False)

	def updateResults(self, network):
		self.__bus.updateResults(network.res_bus)
		self.__grid.updateResults(network.res_ext_grid)
		self.__gen.updateResults(network.res_gen)
		self.__imp.updateResults(network.res_impedance)
		self.__line.updateResults(network.res_line)
		self.__load.updateResults(network.res_load)
		self.__shunt.updateResults(network.res_shunt)
		self.__trafo.updateResults(network.res_trafo)

	def writeResults(self):
		writer = pandas.ExcelWriter(self.__writeFile)
		self.__bus.writeData(writer, 'Bus')
		self.__grid.writeData(writer, 'ExternalGrid')
		self.__gen.writeData(writer, 'Generator')
		self.__imp.writeData(writer, 'Impedance')
		self.__line.writeData(writer, 'Line')
		self.__load.writeData(writer, 'Load')
		self.__shunt.writeData(writer, 'Shunt')
		self.__trafo.writeData(writer, 'Transformer')
		writer.save()

	def run(self, network):
		self.readData()
		self.createElement(network)
		self.runPowerFlow(network)
		self.updateResults(network)
		self.writeResults()