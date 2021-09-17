from collections import deque
n,m=map(int,input().split())
n_li= deque(i for i in range(1,n+1))
counts=0
pic_pass=0
pick_num= map(int,input().split(" "))
for pick in pick_num:
    pic_pass+=1
    #print("n_li",n_li,"index",n_li.index(pick),"pick",pick,"counts",counts)
    if n_li.index(pick)<=n/2:
        while(n_li[0]!=pick):
            left_num=n_li[0]
            n_li.append(left_num)
            n_li.popleft()
            counts+=1
        n_li.popleft()
        n-=1
    else:
        while(n_li[0]!=pick):
            right_num=n_li[-1]
            n_li.appendleft(right_num)
            n_li.pop()
            counts+=1
        n_li.popleft()
        n -= 1
print(counts)



