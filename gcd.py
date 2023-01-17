num1=int(input('Enter First number :'))
num2=int(input('Enter Second number :'))
gcd=min(num1,num2)
while(gcd>=1):
    if(int(num1%gcd)==0 and int(num2%gcd)==0):
        break
    gcd=gcd-1
print("GCD of two numbers is : ",gcd)
