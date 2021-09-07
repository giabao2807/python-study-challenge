'''
	try:
    # thực hiện các lệnh có nguy cơ lỗi
	except:
    # thực hiện nếu phát sinh lỗi trong khối try
	else:
    # thực hiện nếu KHÔNG phát sinh lỗi trong khối try
	finally:
    # LUÔN thực hiện, dù trong khối try có phát sinh lỗi hay không
'''

try:
    a=5
    b='0'
    print(a/b)
except:
    print('Xảy ra lỗi gì đó.')
print("Ngoài khối try .. except.")

print("=================")
try:
    a=5
    b='0'
    print (a+b)
except TypeError:
    print('Phép toán không hợp lệ')
print("Ngoài khối try .. except.")

print("===================")
try:
    a=5
    b=0
    print (a/b)
except TypeError as te:
    print(f'Unsupported operation: {te.args}')
except ZeroDivisionError as zde:
    print (f'Division by zero not allowed: {zde.args}')
print ('Out of try except blocks')

print("===================")
try:
    print("try block")
    x=int(input('Enter a number: '))
    y=int(input('Enter another number: '))
    z=x/y
except ZeroDivisionError:
    print("except ZeroDivisionError block")
    print("Division by 0 not accepted")
else:
    print("else block")
    print("Division = ", z)
finally:
    print("finally block")
    x=0
    y=0
print ("Out of try, except, else and finally blocks." )