N= int(input())
count=0
while((N%5)!=0):
    N-=3
    count+=1
    if N<3:
        break
count += (N // 5)
N %= 5
#print("count {} , N {}".format(count,N))
if N!=0:
    print(-1)
else:
    print(count)

