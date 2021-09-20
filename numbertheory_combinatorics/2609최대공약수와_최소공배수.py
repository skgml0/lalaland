a,b = map(int,input().split())
A,B= a,b

while b!= 0:
    a= a%b
    a,b= b,a
#gcd
print(a)
#lcm
print(A*B//a)

