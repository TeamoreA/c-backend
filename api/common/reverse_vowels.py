def reverse_vowels(message):
    vowels = ['a', 'e', 'i', 'o', 'u']
    chars_list = list(message)
    vowels_list = []

    for i in range(len(chars_list)):
        if chars_list[i].lower() in vowels:
            vowels_list.append(chars_list[i])

    for i in range(len(chars_list)):
        if chars_list[i].lower() in vowels:
            chars_list[i] = vowels_list.pop()

    response = ''.join(chars_list)
    return response
