from .element import Element
import pandapower

class Shunt(Element):
	def createElement(self, network):
		if not self.input.empty:
			for index, row in self.input.iterrows():
				pandapower.create_shunt(
					net=network, 
					bus=row['bus'], 
					p_kw=row['p_kw'], 
					q_kvar=row['q_kvar'], 
					vn_kv=row['vn_kv'], 
					name=row['shunt_name'], 
					in_service=row['in_service'], 
					index=row['index'])