# 그룹단어란 단어에 존재하는 모든 문자에 대해서 각 문자가 연속해서 나타나는 경우만을 말한다.
#단어 n개를 입력받아 그룹단어 개수 출력
#단어는 알파벳 소문자로만 되어있고, 중복되지 않음.
n= int(input())
ans=n
for i in range(n):
    word=input()
    for j in range(len(word)-1):
        if word[j]==word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            ans-=1
            break
print(ans)