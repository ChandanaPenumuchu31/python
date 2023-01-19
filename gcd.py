import random
num1=random.randint(1,100000)
num2=random.randint(1,100000)
if(isinstance(num1,int) and isinstance(num2,int)):
    gcd=min(num1,num2)
    print("Number 1: ",num1)
    print("Number 2 : ",num2)
    while(gcd>=1):
       if(int(num1%gcd)==0 and int(num2%gcd)==0):
           break
       gcd=gcd-1
    print("GCD of two numbers is : ",gcd)
else:
    print("Type of numbers ")
    print("num1 : ",type(num1))
    print("num2 : ",type(num2))
