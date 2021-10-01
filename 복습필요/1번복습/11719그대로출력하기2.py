while True:
    try:
        print(input())
    # 파일의 끝(end of file)을 의미하며, 갑자기 파일의 끝이 올 것을 예상하지 못했기 때문에 위와 같은 오류가 발생
    except EOFError:
        break
# 예외처리 try / except 문을 통해 처리. try블록 : 평소와 같이 입력 / except블럭: 예외 사황에 해당하는 오류 핸들러를 입력해주면 됨
