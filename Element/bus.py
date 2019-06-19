from .element import Element
import pandapower

class Bus(Element):
	def createElement(self, network):
		if not self.input.empty:
			for index, row in self.input.iterrows():
				pandapower.create_bus(net=network, vn_kv=row['vn_kv'], index=row['index'], in_service=row['in_service'])

	def updateResults(self, results):
		self.output = results
		self.output.insert(loc=0, column='bus_name', value=self.input['bus_name'])
