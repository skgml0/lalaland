a=input().split("-")
result=0
for i in a[0].split("+"):
    result+=int(i)

for i in a[1:]:
    for s in i.split("+"):
        result-=int(s)
print(result)