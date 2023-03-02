# print("palindrome ")	

# n = int(input())

# temp = n;
# rem = 0;
# rev = 0;

# while (n>0) :
# 	dig = n % 10;
# 	rev = rev*10 + dig;
# 	n //= 10;	
# if rev == temp :
# 	print("yes")
# else :
# 	print("no")
	
# print("armstrong ")	
# x = int(input())

# tempo = x;
# rema = 0;
# summ = 0;

# while (x>0) :
# 	rema = x % 10 ;
# 	summ += rema*rema*rema ;
# 	x//= 10;
# if tempo == summ :
# 	print("yes")
# else :
# 	print('no')	
		
# print("greateast of three ")	
# a,b,c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)
# if a>b and a>c :
# 	print("a is greateast ",a)
	
# elif b>a and b>c :
# 	print("b is greateast ",b)
# else :
# 	print("c is greateast ",c)

print('armstrong')	
x = int(input())

temp = x ;
rem = 0;
summ = 0;

while (x>0) :
	rem = x%10 ;
	summ += pow(rem,3);
	x//= 10;
if temp == summ :	
	print('yes')
else  :	
	print('no')
	
print('palindrome')	
n = int(input())

tempo = n;
dig = 0;	
rev = 0;	

while (n>0) :
	dig = n%10 ;
	rev = rev*10 + dig ;
	n//=10 ;
if rev == tempo :
	print('yes')
else :
	print('no')	 

p = ("""this is how
		we write  a
	paragraph in python """)
print(p)	