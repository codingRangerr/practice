def SearchingChallenge(strParam):
    k = int(strParam[0])
    str = strParam[1:]
    char_frequency = {}
    window_start = 0
    maxLength = float("-inf")
    string = ""

    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 1
        else:
            char_frequency[right_char] += 1

        while len(char_frequency) > k:
            left_char = str[window_start]

            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1
        if window_end - window_start + 1 > maxLength:
            string = str[window_start:window_end + 1]

    return string


print(SearchingChallenge('2aabbcbbbadef'))
