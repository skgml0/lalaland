def solution(answers):
    answer = []
    A = [1, 2, 3, 4, 5] * 2000
    B = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    C = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    count_a = 0;
    count_b = 0;
    count_c = 0

    for ans, a, b, c in zip(answers, A, B, C):
        if ans == a: count_a += 1
        if ans == b: count_b += 1
        if ans == c: count_c += 1
    tmp = [count_a, count_b, count_c]
    max_tmp = max(tmp)
    for i, v in enumerate(tmp):
        if v == max_tmp: answer.append(i + 1)
    return answer