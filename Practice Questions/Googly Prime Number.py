# Googly Prime Number is defined as a number whose sum of individual digits results in a prime number.

num=int(input("Enter the number\n").strip())
d,sum_digit,k, num1=0,0,True,num

while(num>0):
    d=num%10
    sum_digit+=d
    num=num//10

for i in range(2,sum_digit):
    if sum_digit%i==0:
        k=False
        break

if k:
    print(f"{num1} is a Googly Prime Number")
else:
    print(f"{num1} is not a Googly Prime Number")








