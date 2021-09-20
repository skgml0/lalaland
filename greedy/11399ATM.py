n= int(input())
line=list(map(int,input().split(" ")))
line=sorted(line)
sum_line=0
line_now =0
for i in line:
    line_now+=i
    sum_line+=line_now
print(sum_line)