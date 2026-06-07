num=int(input("enter a your number:"))
iRevers=0
iDigit=0
while num!=0:
    iDigit=num%10
    iRevers=(iRevers*10)+iDigit
    num=num//10
print("the reverse number:",iRevers)