s = int(input())
n=1
while(True):
    if n*(n+1)/2 > s:
        print(n-1)
        break
    n+=1
    """
    자연수 n까지의 합 : (n+1)*n / 2 
    
    """