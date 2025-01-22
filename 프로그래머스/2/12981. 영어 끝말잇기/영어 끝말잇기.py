def solution(n, words):
    used_words = set()

    for i, word in enumerate(words):
        person = (i % n) + 1
        turn = (i // n) + 1

        if word in used_words or (i > 0 and words[i-1][-1] != word[0]):
            return [person, turn]


        used_words.add(word)


    return [0, 0]
