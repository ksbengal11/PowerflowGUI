from .element import Element
import pandapower
import numpy as np

class Load(Element):
	def createElement(self, network):
		if not self.input.empty:
			for index, row in self.input.iterrows():
				pandapower.create_load(
					net=network, 
					bus=row['bus'], 
					p_kw=row['p_kw'], 
					q_kvar=row['q_kvar'])

	def updateResults(self, results):
		self.output = results
		self.output.insert(loc=0, column='load_name', value=self.input['load_name'])
		self.output['sn_kva'] = np.sqrt(self.output['p_kw']*self.output['p_kw'] + self.output['q_kvar']*self.output['q_kvar'])