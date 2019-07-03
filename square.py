n=int(input())
s=0
while n>0:
	p=n%10
	s=s+(p*p)
	n=n//10
print(s)	
