vn = ('Vietnam', 2500)
us = ('USA', 400)

print(vn)
print(us)

 sg = ('Singapore', ('Chinese', 'English'))

 # truy xuất 1 phần tử
print(sg[0])

 # truy xuất một tuple con sử dụng range slice
 print(sg[0:1])
 print(sg[:1])

 # đối với nested tuple
print(sg[1]) # kết quả là một tuple khác\
print(sg[1][1]) # truy xuất phần tử số 1 của tuple lồng

