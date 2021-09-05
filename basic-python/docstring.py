def sum_range(start: int, stop: int, step: int = 1) -> int:
    '''Tính tổng các số trong khoảng [start, stop)
    start: giá trị đâu khoảng
    stop: giá trị cuối khoảng
    step: khoảng giữa hai giá trị liền nhau
    '''
    sum = 0
    for i in range(start, stop, step):
        sum += i
    return sum

sum_range(1, 100)