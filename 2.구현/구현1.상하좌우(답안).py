n=int(input())
x,y =1,1
plans = input().split()

# L,R,U,D에 따른 이동방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types= ['L','R','U','D']
# 이동 계획 하나씩 확인
for plan in plans:
    #이동후 좌표구하기
    # 한 계획 당 movetype4개 확인, 맞으면 좌표이동
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x+ dx[i]
            ny = y+ dy[i]
        if nx<1 or ny<1 or nx>n or ny>n:
            continue
        x,y = nx,ny
print(x,y)
