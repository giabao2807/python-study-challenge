class Trader:
	def __init__(self, name:str, city:str):
		self.name= name
		self.city= city

	#get-set
	def get_name(self):
		return self.name

	def set_name(self, a:str):
		self.name=a

	def get_city(self):
		return self.city

	def set_city(self,c:str):
		self.city=c

	namep = property(set_name,get_name)
	cityp = property(set_city,get_city)

	def __str__(self):
		return f'Trader: name= {self.name} in {self.city} city'
	'''def __repr__(self):
		return f'Trader: name= {self.name} in {self.city} city'''

