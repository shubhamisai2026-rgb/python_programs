iCount=0 
oCount=0
for i in range(1,101):
    if(i%2==0):
        iCount=iCount+1
    else:
        oCount=oCount+1
print("total even numbers:",iCount)
print("total odd numbers:",oCount)

