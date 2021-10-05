import sys
n,k= map(int,sys.stdin.readline().strip().split())
coin=[]
count=0
for i in range(n):
    coin.append(int(sys.stdin.readline().strip()))
coin=sorted(coin,reverse=True)

for one in coin:
    if k>=one:
        count+=(k//one)
        k=(k%one)
    elif k ==0:
        break
print(count)

