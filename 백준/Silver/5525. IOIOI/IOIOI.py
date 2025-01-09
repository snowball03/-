n = int(input())
l = int(input())
s = input()
cnt = 0  # P_N 패턴 개수
j = 0  # 탐색 인덱스

while j < l - 1:
    # IO 패턴이 나타날 때
    if s[j] == "I" and s[j + 1] == "O":
        length = 0  # IOI 길이를 추적
        while j < l - 1 and s[j] == "I" and s[j + 1] == "O":
            length += 1
            j += 2  # IO는 2칸씩 이동
            # 다음 "I"를 확인
            if j < l and s[j] == "I" and length >= n:
                cnt += 1  # P_N 패턴 완성

        # 반복이 끝나면 "I" 이후로 이동
    else:
        j += 1

print(cnt)


