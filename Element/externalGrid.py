from .element import Element
import pandapower

class ExternalGrid(Element):
	def createElement(self, network):
		if not self.input.empty:
			for index, row in self.input.iterrows():
				pandapower.create_ext_grid(
					net=network, 
					bus=row['bus'], 
					vm_pu=row['vm_pu'], 
					va_degree=row['va_degree'], 
					in_service=row['in_service'])

	def updateResults(self, results):
		self.output = results
		self.output.insert(loc=0, column='grid_name', value=self.input['grid_name'])