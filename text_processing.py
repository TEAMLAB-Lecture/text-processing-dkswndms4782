def normalize(input_string):
    # 띄어쓰기 기준으로 단어들의 배열 만들기
    splited_string = input_string.split()
    normalized_string = ""
    # "          "같은 경우 예외처리
    if len(splited_string) == 0:
        return ""
    # 각 단어들 더해주고 한칸만 띄워주기
    for i in range(len(splited_string)):
        normalized_string += splited_string[i] + " "
    # 마지막 단어 다음에 띄어쓰기를 없애주기 위해 [:-1]슬라이싱 추가
    return normalized_string[:-1].lower()


def no_vowels(input_string):
    # 모음 배열 생성
    vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    no_vowel_string = input_string
    # 모음이 해당 string에 있을때 그 모음을 ""로 대체
    for i in vowel:
        no_vowel_string = no_vowel_string.replace(i, "")
    return no_vowel_string