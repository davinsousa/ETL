def transform(legacy_data):
	
	new_data={}
	
	for k, v in legacy_data.items():
		temp_data={x.lower():k for x in v}
		new_data={**new_data, **temp_data}
	
	return new_data
