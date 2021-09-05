class Employee:
	def __new__(cls,*args,**kwargs):
		print('__new__ is being called')
		instance = object.__new__(cls)
		return instance

	def __init__(seft, name: str):
		print('__init__ is being called')
		seft.name=name

	def print(seft):
		print(seft.name)


if __name__ == '__main__':
	giabaone = Employee("Gia Bao ne")
	giabaone.print()

	anhkhoa = Employee('Anh khoa ne')
	anhkhoa.print()