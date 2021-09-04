def makebold(f):
	return lambda: "<b>" + f() + "</b>"

def makeitalic(f):
	return lambda: "<i>" +f() + "<i>"

@makeitalic
@makebold
def say():
	return "hello"

print(say())