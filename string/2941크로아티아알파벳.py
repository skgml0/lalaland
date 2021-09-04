import re
croatia=['c=','c-','dz=','d-','lj','nj','s=','z=']
string=input()
count=0
for i in croatia :
    if i in string:
        count+=string.count(i)
        string=re.sub(i,"-",string)
        #print(string)
string= [i for i in string if i!='-'] #'-'을 제외하고 string에 넣는법.
#print(string)
count+=len(string)
print(count)