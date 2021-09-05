class Vector:
    """A class for vector"""

    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __add__(self, v):
        x = self.x + v.x
        y = self.y + v.y
        return Vector(x, y)

    def __sub__(self, v):
        x = self.x - v.x
        y = self.y - v.y
        return Vector(x, y)

    def __mul__(self, n):
        x = self.x * n
        y = self.y * n
        return Vector(x, y)

    def __neg__(self):
        return Vector(self.x * -1, self.y * -1)

if __name__ == '__main__':
     v1 = Vector(1, 2)
     v2 = Vector(1,3)
     print(v1 + v2) # phép cộng
     print(v1 - v2) # phép trừ
     print(v1 * 2) # phép nhân vô hướng
     print(-v1) # nghịch đảo
