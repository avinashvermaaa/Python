#tempavik template
    
n = int(input())
temp = n;
123
rev = 0;

while (n>0) :
	dig = n % 10 ;
	rev = rev * 10 + dig ;
	n //= 10 ;
	 
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")