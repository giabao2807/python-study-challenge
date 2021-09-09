#zip(*iterables) = aggreagat elements from two or more iterables (list,tuples,set,etc.)
#                   creates a zip object with paired elements stored in tuples for each elements


#=======using 2 iterables===============
usernames = ["Dube","Bro","Mister"]
passwords = ("p@ssword","abc123","guest")

#--------using list and zip type-----
#users = list(zip(usernames,passwords))

#print(type(users))
#for i in users:
#    print(i)

#---------using dict type------------
users = dict(zip(usernames,passwords))

print(type(users))
for key,value in users.items():
    print(key+ " " + value)

