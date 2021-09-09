import time

time_str = "20 April, 2021"
time_object = time.strptime (time_str,"%d %B, %Y")
print(time_object)