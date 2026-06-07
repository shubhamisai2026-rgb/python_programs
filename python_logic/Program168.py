num=int(input("enter a your number:"))
temp=num
iDigit=0
iReverse=0
while num!=0:
    iDigit=num%10
    iReverse=(iReverse*10)+iDigit
    num=num//10
if(temp==iReverse):
    print("this is the palindrome number.....")
else:
    print("this is not palindrome number.......")
