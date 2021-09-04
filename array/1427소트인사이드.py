import sys
from sys import stdin, stdout
n= list(stdin.readline().rstrip())
m=sorted(n,reverse=True)
for i in m:
    sys.stdout.write(i+"")