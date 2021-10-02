t=int(input())
arr={}
for t in range(t):
    key,value = input().split(" ")
    arr[key]= int(value)
print(min(arr,key=arr.get))