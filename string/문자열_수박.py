def solution(n):
    word = "수박"
    a = n // 2
    b = n % 2
    answer = "수박" * a + "수" * b
    return answer