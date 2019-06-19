from .element import Element
import pandapower

class Line(Element):
	def createElement(self, network):
		if not self.input.empty:
			for index, row in self.input.iterrows():
				pandapower.create_line_from_parameters(net=network, from_bus=row['from_bus'], to_bus=row['to_bus'], length_km=row['length_km'], r_ohm_per_km=row['r_ohm_per_km'], x_ohm_per_km=row['x_ohm_per_km'], c_nf_per_km=row['c_nf_per_km'], max_i_ka=row['max_i_ka'], index=row['index'], in_service=row['in_service'])

	def updateResults(self, results):
		self.output = results

		self.output.insert(loc=0, column='line_name', value=self.input['line_name'])
		self.output.insert(loc=1, column='conductor', value=self.input['conductor'])
		self.output.insert(loc=2, column='length_m', value=self.input['length_km']*1000)

		self.output['line_status'] = self.input['conductor']
		self.output.fillna(0, inplace=True)

		self.output.loc[self.output['loading_percent']<0.05, 'line_status'] = 'OFFLINE'
		self.output['loading_percent'] = self.output['loading_percent'].round(1)