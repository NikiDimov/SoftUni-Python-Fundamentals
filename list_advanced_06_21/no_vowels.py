vowels = ['a', 'o', 'u', 'e', 'i']

text = list(input())


def extract_no_vowels(text):
    result = [el for el in text if el.lower() not in vowels]
    return ''.join(result)


print(extract_no_vowels(text))
