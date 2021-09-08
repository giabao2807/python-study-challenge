from Trader import *
from Transaction import *

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




