nite= input()
row= int(nite[1])
column = int(ord(nite[0])) - int(ord('a'))+1
""" ord(문자) : 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환
"""
move = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
count=0
for m in move:
    next_row = row+m[0]
    next_column= column + m[1]

    if next_row >=1 and next_row<=8 and next_column>=1 and next_column<=8:
        count+=1
print(count)