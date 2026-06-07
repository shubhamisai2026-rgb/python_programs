arr=[45,43,25,75,78,98,54]
iMax=arr[0]
iMin=arr[0]
for i in arr:
    if i>iMax:
        iMax=i
    if iMin>i:
        iMin=i
print("maximum number of array is:",iMax)
print("minimum number of array is:",iMin)