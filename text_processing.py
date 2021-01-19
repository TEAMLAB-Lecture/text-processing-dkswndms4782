def normalize(input_string):
    splited_string = input_string.split()
    normalized_string = ""
    for i in range(0,len(splited_string)-1):
        normalized_string += (splited_string[i] + " ")
    normalized_string += splited_string[len(splited_string) - 1]
    return normalized_string.lower()


def no_vowels(input_string):
    vowel = ['a','e','i','o','u','A','E','I','O','U']
    no_vowel_string = input_string
    for i in vowel:
        no_vowel_string = no_vowel_string.replace(i,"")
    return no_vowel_string
