from .element import Element
import pandapower

class Impedance(Element):
	def createElement(self, network):
		if not self.input.empty:
			pandapower.create_impedance(
				net=network, 
				from_bus=row['from_bus'], 
				to_bus=row['to_bus'], 
				rft_pu=row['rft_pu'], 
				xft_pu=row['xft_pu'], 
				sn_kva=row['sn_kva'], 
				rtf_pu=row['rtf_pu'], 
				xtf_pu=row['xtf_pu'])