import time

print(time.ctime(0))
print(time.time()) #return  current seconds since epoch

print(time.ctime(time.time()))

print("==================")
time_object = time,time.localtime()
print(time_object)
local_time = time.strftime("%B %D %Y %H:%M:%S",time_object)
print(local_time)