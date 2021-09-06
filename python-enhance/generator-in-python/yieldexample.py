class YieldSample:
	def __iter__(self):
		i=10;
		yield i+10
		yield i*10
		yield i/10
		yield i-10

if __name__ == '__main__':
	for value in YieldSample():
		print(value)