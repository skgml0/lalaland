"""문제 : 주어진 수를 M번 더하여 가장 큰수 만들기, 단  배열의 특정 인덱스 수가 연속해서 k번 초과하여 더해질 수 없다."""
n,m,k = map(int,input().split())
arr = list(map(int,input().split(" ")))
arr.sort(reverse=True)
first= arr[0]
second= arr[1]
anser= (m // (k+1) * (first*k+second) + m %(k+1) *first)
print(anser)