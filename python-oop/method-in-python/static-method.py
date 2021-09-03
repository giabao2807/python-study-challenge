class Person:
    count = 0
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.count += 1
    
    def print(self, format = True):
        """In thông tin ra console
        format: có định dạng thông tin hay không
        """
        if not format:
            print(self.name, self.age)
        else:
            print(f'{self.name}, {self.age} years old')

    @classmethod
    def show_count(cls): 
        """Trả lại số object trong chương trình"""
        print(f"Hiện có {cls.count} object Person trong chương trình")

    @staticmethod
    def calculate_birth_year(age : int) -> int:
        import datetime as dt
        year = dt.datetime.now().year
        return year - age

# sử dụng phương thức calculate_birth_year như sau:
my_birth_year = Person.calculate_birth_year(37)
print(my_birth_year) # kết quả 1983 (năm 2020)