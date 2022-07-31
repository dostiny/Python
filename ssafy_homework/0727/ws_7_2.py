def wordrelay(words):
    for num in range(1, len(words)):
        if words[num-1][-1] != words[num][0]:   # 마지막 문자로 시작을 안했을때 탈락!
            return f'{num+1}번 탈락!'
        elif words[num-1] == words[num]:    # 같은 값을 입력했을때 탈락
            return f'{num+1}번 탈락!'
        elif words[num-1] == 'done':    # done 입력되었을때 탈락
            return f'{num-1}번 탈락!'

words = ["round","dream","magnet","tweet","tweet","trick","kiwi"]
print(wordrelay(words)) # 5번째 참가자가 탈락하였습니다.