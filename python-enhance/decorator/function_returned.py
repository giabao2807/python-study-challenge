"đây là hàm bình thường"
def hello(name):
	print(f"Hello, {name}. Welcome to my chanel!")

"đây là hàm bậc cao, kết quả ytrar về là một hàm khác"
def welcome():
	return hello

xxx= welcome()
xxx("Anh Khoa")
