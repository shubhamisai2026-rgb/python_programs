num=int(input("enter a your number:"))
temp=num
num=num//2
i=2
for i in range(1,num+1):
    if(temp%2==0):
        break
if i>=num:
    print("number is prime")
else:
    print("number is not a prime")
