def solution(priorities, location):
    count = 0  # 내가 인쇄한 요청 문서가 몇 번째로 인쇄되는지 횟수
    while (len(priorities) != 0):  # priorities가 0으로 빌 때까지 반복
        if location == 0:  # 요청 문서가 맨 앞일 경우
            if priorities[0] < max(priorities):  # 더 중요도가 큰 문서가 있으면
                priorities.append(priorities.pop(0))  # 맨 뒤로 보냄
                location = len(priorities) - 1  # 요청문서 맨끝으로 보냄 (배열길이-1(0부터시작이므로))
            else:  # 더 우선순위가 높은 것이 없다면 내꺼가 출력되는 것이므로 return으로 끝냄
                return count + 1  # 첫번째 출력

        else:  # 요청한 문서가 첫번째가 아닐때
            if priorities[0] < max(priorities):  # 중요도가 더 큰 문서가 뒤에 있을떄
                priorities.append(priorities.pop(0))  # 앞 문서를 맨 뒤로 추가
                location -= 1  # 맨앞 요소가 뒤로 갔기 때문에 요청문서 인덱션 하나 줄어듬
            else:  # 중요도가 맨 앞 문서가 클때
                priorities.pop(0)  # 맨 앞 문서 출력
                location -= 1  # 맨앞 요소 출력, location 하나 줄어듬
                count += 1
    return count
# 중요도가 큰 문서가 앞에 있으면 출력, 뒤에 있을 경우 앞 요소 뒤로 보내기 & 요청문서 인덱스 -1
# 요청문서가 0번째 인덱스(가장 처음)오면 출력.