class Person:
	def __init__(self, name,age):
		self.name=name
		self.age=age

	def print(self):
	 	print(f'{self.name} {self.age} years old')

	@staticmethod
	def elder(person):
		if person.age >= 75:
			return True
		return False

presidents = [ Person('Gia Bảo',20),
				Person('Anh Khoa',20), 
				Person('Trump',80),
				Person('Nixon',90)]

'''def elder(person):
	if person.age>=75 :
		return True
	return False'''

if __name__ == '__main__':
	'''sử dụng filter giống java, func trả về boolean	
		ứng với mỗi iterable vào func nếu true sẽ thêm vào list kết quả'''
		#giống where trong C#
	old_president = filter(Person.elder,presidents)
	for p in old_president :
		p.print()
