class Person:

    #dấu 2 gach __ trong hàm init thể hiện đây là biến private,
    #ngoài class k thể thay đổi được-> highly recommend
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


putin = Person()
putin.set_fname('Putin')
putin.set_lname('Vladimir')
putin.set_age(66)
print(putin.get_name())