# 순열과 조합 라이브러리
import itertools
# 입력값 공백으로 구분
n,m = map(int,input().split(" "))
# 1부터 n까지 리스트에 저장
arr=list(int(i) for i in range(1,n+1))
# 서로 다른 n개 중 m개를 고르는 순열
nPr=itertools.permutations(arr,m)
# 출력형태 변환 tuple> 문자로 변환
for a in list(nPr):
    print(' '.join(map(str,a)))