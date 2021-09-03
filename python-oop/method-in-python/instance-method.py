#tương tự c#

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def print(self, format = True):
        """In thông tin ra console
        format: có định dạng thông tin hay không
        """
        if not format:
            print(self.name, self.age)
        else:
            print(f'{self.name}, {self.age} years old')
            

putin = Person('Putin Vladimir', 60)
Person.print(putin) # cho kết quả 'Putin, 60 years old'
Person.print(putin, False) # cho kết quả 'Putin 60'

