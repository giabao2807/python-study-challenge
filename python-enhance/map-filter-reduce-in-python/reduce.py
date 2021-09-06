'''muốn sử dụng reduce phải import ở đầu file vì k phải hàm built-in'''
from functools import reduce

#imperative factorial function
def imp_fact(n:int):
    p=1
    for i in range(1,n+1):
        p*=i 
    return p

'''
    Cách hoạt động reduce như sau:
    1.Giả sử n=3 thì range(1,4) cho ra giá trị 1,2,3
    2.Áp dụng mult cho 2 phần tử đầu tiên mult(1,2) được 2
    3.lấy kết quả trên làm tham số thứ nhất lấy phâng tử tiếp theo làm 
    tham số thứ 2 cho mult(2,3)
    4.ds k còn giá trị trả về 6.
'''
#functional factorial function
''' lưu ý cho reduce:
    1. reduce(<func>,<iterable>)
    2. func phải là 1 hàm có 2 tham số
    3. tham số trong func cùng kiểu với giá trị iterable
    4.kết quả reduce cùng kiểu với kết quả trả về của func
'''
def fun_fac(n:int):
    def mult(x,y): 
        return x*y
    return reduce(mult,range(1,n+1))

def test1():
   n=3
   f=imp_fact(3)
   print(f'{n}! = {f}')

def test2():
    n=3
    f= fun_fac(n)
    print(f'{n}! = {f}') 

if __name__ == '__main__':
    test1()
    test2()