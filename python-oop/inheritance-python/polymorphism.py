class Person:
    def __init__(self, firstname: str, lastname: str, birthyear: int):
        self.first_name = firstname
        self.last_name = lastname
        self.birth_year = birthyear

    def display(self):
        print(f"{self.first_name} {self.last_name}, born {self.birth_year}")

class Student(Person):
    def __init__(self, firstname: str, lastname: str, birthyear: int, group: str):
        super().__init__(firstname, lastname, birthyear)
        self.group = group

    def display(self):
        print(f"{self.first_name} {self.last_name}, born {self.birth_year}, group {self.group}")

class Teacher:
    def __init__(self, firstname: str, lastname: str, birthyear: int, specialization: str):
        self.first_name = firstname
        self.last_name = lastname
        self.birth_year = birthyear
        self.specialization = specialization

    def display(self):
        print(f"{self.first_name} {self.last_name}, born {self.birth_year}, mastered in {self.specialization}")

def show_info(p):
    p.display()

if __name__ == '__main__':
    putin = Person('Vladimir', 'Putin', 1955)
    trump = Student('Donald', 'Trump', 1965, 'TWH_2017_2021')
    obama = Teacher('Barack', 'Obama', 1975, 'Computer Science')
    show_info(putin)
    show_info(trump)
    show_info(obama)