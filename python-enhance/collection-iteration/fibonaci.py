#iterable là loại object container có khả năng trả lại lần lượt từng
# giá trị. dữ liệu thực thụ sẽ do iterator tải hoặc tạo ra.
#mỗi iterable phải có 1 iterator tương ứng

#bắt buộc phải có iter()
#ng dùng thao tác trên iterabale : bản châts gọi về iterator
class FibonacciIterable:
    def __init__(self, count=10):
        self.count = count

    #trả lại 1 object của iterator
    def __iter__(self):
        return FibonacciIterator(self.count)


#có nhiệm vụ tạo ra dữ liệu cho iterable
#iterator bắt buộc phải có phương thức next()
class FibonacciIterator:
    def __init__(self, count=10):
        self.a, self.b = 0, 1
        self.count = count
        self.__i = 0

    #tạo ra các phần tử cho iterable
    #nếu k còn phần tử nào phải phát ra ngoại lệ StopInteration
    def __next__(self):
        if self.__i > self.count:
            raise StopIteration()
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        self.__i += 1
        return value

    #có thể thực thi iter giúp 1 iterator thành iterable
     #def __iter__(self):
     #    return self


def test1():
    print('Test 1:', end=' ')
    iterable = FibonacciIterable(15)
    for f in iterable:
        print(f, end=' ')
    print()


def test2():
    print('Test 2:', end=' ')
    iterator = FibonacciIterator(15)
    for f in iterator:
        print(f, end=' ')
    print()


def test3():
    print('Test 3:', end=' ')
    iterator = FibonacciIterator(15)
    while True:
        try:
            f = next(iterator)
            print(f, end=' ')
        except StopIteration:
            break
    print()


def test4():
    print('Test 4:', end=' ')
    iterable = FibonacciIterable(15)
    iterator = iter(iterable)
    while True:
        try:
            f = next(iterator)
            print(f, end=' ')
        except StopIteration:
            break
    print()


if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()