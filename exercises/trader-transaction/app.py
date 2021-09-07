from Trader import *
from Transaction import *

trades = [ Trader("Raoul","Cambridge"),Trader("Mario","Milan"), 
		Trader("Alan","Cambridge"), Trader("Brian", "Cambridge")]

transactions =[Transaction(trades[3],2011,500),
				Transaction(trades[0],2012,1000),
				Transaction(trades[0],2011,400),
				Transaction(trades[1],2012,710),
				Transaction(trades[1],2012,700),
				Transaction(trades[2],2012,950)]

''' input done
for a in trades:
	print(a)

print("==========")
for b in transactions:
	print(b)
'''


#output:
if __name__ == '__main__':
	#1. Find all transactions in the year 2011 and sort them by value (small to high).
	cau1=list(filter(lambda p : p.year==2011,transactions))
	cau1.sort(key = lambda p: p.value)
	for a in cau1 :
		print(a)

	#2. Find all transactions have value greater than 300 and sort them by trader’s city
	cau2=
