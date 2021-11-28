import itertools
n= int(input())
arr= list(map(int,input().split(" ")))
nPr=itertools.permutations(arr,n)
count=-1
for a in nPr:
    count+=1
    b = ' '.join(map(str, a))
    if b == ' '.join(map(str, arr)):
            break
nPr = list(nPr)
print(' '.join(map(str,nPr[count])))
