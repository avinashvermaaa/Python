n = int(input())

temp = n;
dig = 0;
som = 0;
while (n>0) :
	dig = n % 10 ;
	som = som + dig*dig*dig;
	n //= 10 ;
if temp == som :
	print("It is a armstrong number");
else  :
	print("It isn't a armstrong number");	