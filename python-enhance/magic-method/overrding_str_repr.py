class Vector:
    """A class for vector"""
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x}, {self.y})'
    def __repr__(self):
       return f'({self.x}, {self.y})'


if __name__ == '__main__':
	v1= Vector(0,1)
	print(v1)
	