#tham số biến động trong python
#loại tham số với số lượng k xác định

def sum(start, *numbers):
    for n in numbers:
        start += n
    return start

print(sum(0, 1, 2)) # = 3
print(sum(1, 2, 3)) # = 6
print(sum(0, 1, 2, 3, 4, 5, 6)) # = 21