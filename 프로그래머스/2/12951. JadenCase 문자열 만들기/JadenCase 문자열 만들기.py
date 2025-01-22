def solution(s):
    result = []  # 결과를 담을 리스트
    words = s.split(" ")  # 공백 기준으로 분리 (연속된 공백 유지)

    for word in words:
        if len(word) > 0:  # 단어가 비어 있지 않은 경우
            result.append(word[0].upper() + word[1:].lower())
        else:
            result.append("")  # 공백 유지

    return " ".join(result)  # 공백으로 다시 연결
