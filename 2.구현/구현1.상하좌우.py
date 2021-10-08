start=[1,1]
#좌, 우 , 위, 아래
move=[[0,-1],[0,1],[-1,0],[1,0]]
n=int(input())
m = list(input().split(" "))
for m1 in m :
    if m1 =="L":
        if 1<start[1]<n+1:
            start[0]+= move[0][0]
            start[1]+= move[0][1]
    elif m1 == "R":
        if 0 < start[1] < n:
            start[0] += move[1][0]
            start[1] += move[1][1]
    elif m1 == "U":
        if 1 < start[0] < n + 1:
            start[0] += move[2][0]
            start[1] += move[2][1]
    elif m1 == "D":
        if 0 < start[0] < n:
            start[0] += move[3][0]
            start[1] += move[3][1]
print(start)
