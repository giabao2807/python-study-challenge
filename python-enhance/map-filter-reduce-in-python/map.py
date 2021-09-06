X=[x/100 for x in range(100,1000)]

def peform(x,a=1.0,b=0.0):
	return a * x  + b  

'''(1) lần lượt duyệt từng phần tử của x trong X
	(2) ứng với mỗi phần tử x áp dụng hàm perform
	(3) thêm giá trị y vào cuối cùng trong Y
	-> sau khi thực hiện hàm map trả về kiểu map nên phải chuyển về kiểu list
	map() trong python tương tự linq select trong C#'''
Y = list(map(peform,X))

for y in Y:
 	print (y, end= ' ')


'''cú pháp map(<hàm>, *<interable> :
	hàm áp dụng cho từng phần tử của interable, chỉ cần truyền tên hàm
	chỉ quan tâm kết quả trả về của hàm, bỏ qua các lệnh trong hàm'''