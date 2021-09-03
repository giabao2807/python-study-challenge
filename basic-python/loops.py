#list primes
primes = [2,3,5,7]
for prime in primes:
	print(prime)

print("===================")
#print 01,2,3,4
for x in range(5):
	print(x)

print("===================")
#print 3,4,5
for x in range(3,6): 
	print(x)

print("===================")
#print 3,5,7
for x in range(3,8,2):
	print(x)

print("===================")
# Prints out 0,1,2,3,4
count = 0
while count < 5:
    print(count)
    count += 1 

# Prints out 0,1,2,3,4
print("===================")
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

print("===================")
# Prints out only odd numbers  1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)

# else in loops
# Prints out 0,1,2,3,4 and then it prints "count value reached 5"
print("===================")
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

print("===================")
# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")