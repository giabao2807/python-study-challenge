class Person:
    count = 0

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.count += 1

    @classmethod
    def show_count(cls): 
        """Trả lại số object trong chương trình"""
        print(f"Hiện có {cls.count} object Person trong chương trình")

putin = Person('Putin Vladimir', 60)
trump = Person('Trump Donald', 60)
Person.show_count()


