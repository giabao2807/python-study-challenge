'''yeild hoạt động tương tự như return có chỗ trả lại giá trị cho hàm gọi
,tuy nhiên lại không kết thúc việc thực hiện hàm
    Mô hình hoạt động giống next của iterator => giúp nó có thể sinh ra
iterator mà k cần thực thi phương thức next()'''
class FibonacciIterable:
    def __init__(self, count=10):
        self.a, self.b = 0, 1
        self.count = count

    '''cấu trúc sinh ra chuỗi giá trị sử dụng từ khoá yield: generator'''
    def __iter__(self):
        i = 0
        while True:
            if i > self.count:
                break
            yield self.a
            self.a, self.b = self.b, self.a + self.b
            i += 1


def test1():
    iterable = FibonacciIterable(20)
    for f in iterable:
        print(f, end='  ')


if __name__ == '__main__':
    test1()