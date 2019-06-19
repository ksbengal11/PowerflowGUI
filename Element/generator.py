from .element import Element
import pandapower

class Generator(Element):
	def createElement(self, network):
		if not self.input.empty:
			for index, row in self.input.iterrows():
				pandapower.create_gen(
					net=network, 
					bus=row['bus'], 
					p_kw=row['p_kw'], 
					index=row['index'], 
					name=row['name'])