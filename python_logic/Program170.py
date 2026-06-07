num=int(input("enter a your number:"))
arr=[]
for i in range(0,num):
    arr.append(int(input("enter a your number:")))

search=int(input("ente serching index:"))
if search>num:
    print("not found")
else:
    print(arr[search])