from .element import Element
import pandapower

class Transformer(Element):
	def updateResults(self, results):
		self.output = results

		self.output.insert(loc=0, column='trafo_name', value=self.input['trafo_name'])
		self.output.insert(loc=1, column='in_service', value=self.input['in_service'])

		self.output.loc[self.input['in_service']==False, 'loading_percent'] = 0
		self.output['loading_percent'] = self.output['loading_percent'].round(1)

	def createElement(self, network):
		if not self.input.empty:
			for index, row in self.input.iterrows():
				pandapower.create_transformer_from_parameters(
					net=network, 
					hv_bus=row['hv_bus'], 
					lv_bus=row['lv_bus'], 
					sn_kva=row['sn_kva'], 
					vn_hv_kv=row['vn_hv_kv'], 
					vn_lv_kv=row['vn_lv_kv'], 
					vsc_percent=row['vsc_percent'], 
					vscr_percent=row['vscr_percent'], 
					pfe_kw=row['pfe_kw'], 
					i0_percent=row['i0_percent'], 
					shift_degree=row['shift_degree'], 
					tp_side=row['tp_side'], 
					tp_mid=row['tp_mid'], 
					tp_max=row['tp_max'], 
					tp_min=row['tp_min'], 
					tp_st_percent=row['tp_st_percent'], 
					tp_st_degree=row['tp_st_degree'], 
					in_service=row['in_service'], 
					max_loading_percent=row['max_loading_percent'], 
					parallel=row['parallel'])