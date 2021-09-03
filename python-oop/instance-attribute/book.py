class Book:

	count =0
	def __init__(self,
					title: str,
					authors: str ='',
					publisher: str='',
					year: int=2020,
					edition: int=1):
		self.title = title
		self.authors=authors
		self.publisher=publisher
		self.year=year
		self.edition=edition
		self.__private =True
		Book.count+=1

	def to_string(self,brief=True):
		if brief:
			return f"{self.title} by {self.authors}"
		else:
			return f"{self.title} by {self.authors}, {self.edition} edition, {self.publisher}, {self.year}"

	def print(this, brief=False):
		print(this.to_string(brief))


#sử dụng class book 
b1= Book('Tự học lập trinh Python')
b1.authors='Gia Bảo'
b1.publisher='Tự học ICT'
b1.year=2021
b1.print()
print(Book.count)

b2 = Book("Python programming","Trump. D","The White house",2021)
print(b2.title,b2.authors)
print(Book.count)