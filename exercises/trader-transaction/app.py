from Trader import *
from Transaction import *
from functools import reduce

trades = [ Trader("Raoul","Cambridge"),Trader("Mario","Milan"), 
		Trader("Alan","Cambridge"), Trader("Brian", "Cambridge")]

transactions =[Transaction(trades[3],2011,200),
				Transaction(trades[0],2012,1000),
				Transaction(trades[0],2011,400),
				Transaction(trades[1],2012,710),
				Transaction(trades[1],2012,700),
				Transaction(trades[2],2012,250)]

''' input done
for a in trades:
	print(a)

print("==========")
for b in transactions:
	print(b)
'''
def printlist(listofO:list):
	for x in listofO:
		print(x)


#output:
if __name__ == '__main__':
	#1. Find all transactions in the year 2011 and sort them by value (small to high).
	cau1=list(filter(lambda p : p.year==2011,transactions))
	cau1.sort(key = lambda p: p.value)
	printlist(cau1)

	print("======================")
	#2. Find all transactions have value greater than 300 and sort them by trader’s city
	cau2 = list(filter(lambda p : p.value>300,transactions))
	cau2.sort(key = lambda p: p.trader.city)
	printlist(cau2)

	print("======================")
	#3. What are all the unique cities where the traders work?
	cau3 = set(map(lambda p: p.trader.city,transactions))
	printlist(cau3)

	print("======================")
	#4. Find all traders from Cambridge and sort them by name desc.
	cau4 =list(filter(lambda p:p.city== 'Cambridge',set(map(lambda p : p.trader,transactions))))
	cau4.sort(key = lambda p : p.name)
	printlist(cau4)

	print("======================")
	#5. Return a string of all traders’ names sorted alphabetically.
	cau5 = list(map(lambda p:p.name,set(map(lambda p : p.trader,transactions))))
	cau5.sort(key = lambda p: p)
	printlist(cau5)

	print("======================")
	#6. Are any traders based in Milan?
	cau6 = list(filter(lambda p:p.city=='Milan',set(map(lambda p : p.trader,transactions))))
	if len(cau6) > 0:
		print('Have trader based in Milan')

	print("======================")
	#7. Count the number of traders in Milan.
	print(len(cau6) , "trader based in milan")

	print("======================")
	#8. Print all transactions’ values from the traders living in Cambridge.
	cau8 = list(map(lambda p: p.value,filter(lambda p: p.trader.city== 'Cambridge',transactions)))
	printlist(cau8)

	print("======================")
	#9. What’s the highest value of all the transactions?
	cau9 = max(map(lambda p:p.value,transactions))
	print(cau9)

	print("======================")
	#10. Find the transaction with the smallest value.
	cau10 = min(map(lambda p :p.value,transactions))
	print(cau10)




