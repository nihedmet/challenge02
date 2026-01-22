num=[2,5,85,456,157,123,15,32]
target=int(input("enter a num to search: "))
for i in range(len(num)):
    if num[i]==target:
        print("found in index: ",i)
        break
else:
        print("not found")
