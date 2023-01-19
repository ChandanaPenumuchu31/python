import random
try:
    num1=random.randint(1,10000)
    try:
      num2=random.randint(1,100000)
      gcd=min(num1,num2)
      print("Number 1: ",num1)
      print("Number 2 : ",num2)
      while(gcd>=1):
        if(int(num1%gcd)==0 and int(num2%gcd)==0):
           break
        gcd=gcd-1
      print("GCD of two numbers is : ",gcd)
    except:
      print("num2 is not an integer")
except:
    print("num1 i not an integer")
