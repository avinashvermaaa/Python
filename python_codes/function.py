#wap to print sum of two number from a function.

x = int(input())
y = int(input())

def sum(x=3,y=5):
	return x + y
print("summation is : ",sum(x,y))

def diff(x,y):
	return x - y
print("difference is : ",diff(x,y))


def mul(x,y):
	return x * y
print("mulitplication is : ",mul(x,y))


def div(x,y):
	return x / y
print("divison is : ",div(x,y))


	
def summ(a=5,b=6):
	return a+b
r = summ(5,5)
print(r)	