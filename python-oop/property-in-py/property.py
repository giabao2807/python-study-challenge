class Person:
    def __init__(self, fname: str = '', lname: str = '', age: int = 18):
        self.__fname = fname
        self.__lname = lname
        self.__age = age

    def set_age(self, age: int):
        if age > 0:
            self.__age = age
    def get_age(self):
        return self.__age

    def get_lname(self):
        return self.__lname
    def set_lname(self, lname: str):
        if lname.isalpha():
            self.__lname = lname    

    def get_fname(self):
        return self.__fname
    def set_fname(self, fname: str):
        if fname.isalpha():
            self.__fname = fname

    def get_name(self):
        return f'{self.__fname} {self.__lname}'

    #property in python property(getter,setter,deleter)
    #deleter ít dùng dùng để gọi del
    #nếu thiếu setter -> read-only
    first_name = property(get_fname, set_fname)
    last_name = property(get_lname, set_lname)
    full_name = property(get_name)
    age = property(get_age, set_age)

    def print(self, format = True):
        if not format:
            print(self.name, self.age)
        else:
            print(f'{self.full_name}, {self.age} years old')


putin = Person()
putin.first_name = 'Putin'
putin.last_name = 'Vladimir'
putin.age = 66
print(putin.full_name, putin.age)