#GCD (Greatest Common Divisor) 
a=int(input("enter first number "))
b=int(input("enter second number "))
while(a!=b):
  if(a>b):
    a-=b
  else:
    b-=a
print("GCD of", a," and", b," is", a)

a=int(input("enter first number "))
b=int(input("enter second number "))

for i in range(1,a+1):
  for i in range(1,b+1):
    if(a%i==0 and b%i==0):
      g=i
            
print("GCD of", a," and", b," is",g)    

