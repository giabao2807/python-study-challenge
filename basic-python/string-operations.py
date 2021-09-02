astring = "giabao1"
astring2 = 'giabao1'

print(astring)
print(astring2)

#lenghth
print("lenghth of string %d" %len(astring))

print("index of o %d" %astring.index("o"))
print("count a %d" %astring.count("a"))

print("cut index 2->5 %s" %astring[2:5])
print(astring[2:5:2])

#reverse
astring3 = "Hello world!"
print(astring3[::-1])

#true fale
astring4 = "Hello world!"
print(astring4.startswith("Hello"))
print(astring4.endswith("asdfasdfasdf"))

#split string
astring5 = "Hello world!"
afewwords = astring5.split(" ")
print(afewwords)

#ex
s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))
print("The first occurrence of the letter a = %d" % s.index("a"))
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5])#0-5
print("The next five characters are '%s'" % s[5:10])#5-10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))
