from Trader import *
class Transaction:

	def __init__(self, trader:Trader, year:int, value:int):
		self.trader= trader
		self.year= year
		self.value= value

	def get_trader(self):
		return self.trader

	def set_trader(self, traders):
		self.trader=traders

	def get_year(self):
		return self.year

	def set_year(self,years):
		self.year=years

	def get_value(self):
		return self.value

	def set_value(self,values):
		self.value=values

	traderp = property(get_trader,set_trader)
	yearp =property(get_year,set_year)
	valuep=property(get_value,set_value)

	def __str__(self):
		return f'Trasaction: {self.trader} , {self.year} years , {self.value} values'