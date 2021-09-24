import math
t = int(input())
rings= list(map(int,input().split(" ")))
for r in range(1,t):
    #print("{}/{}".format(rings[0]//rings[r],rings[r]//rings[r]))
    gcd = math.gcd(rings[0],rings[r])
    print("{}/{}".format(rings[0]//gcd,rings[r]//gcd))
    """최대공약수 import math math.gcd( a, b) 로 구할 수 있음"""