def recur(n):
    if n ==0 :
        return 0
    elif n==1:
        return 1
    else:
        return recur(n-1)+recur(n-2)

print(recur(int(input())))