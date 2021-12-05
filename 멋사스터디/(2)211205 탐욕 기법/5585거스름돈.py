n= int(input())
money=1000-n
type=[500,100,50,10,5,1]
result=0
for i in type:
    result +=(money // i)
    money %=i
    #print("result {} money {}".format(result,money))
    if money==0:
        break
print(result)