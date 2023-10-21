def SearchingChallenge(strParam):
    # code goes here
    k = int(strParam[0])
    str = strParam[1:]
    char_freq = {}
    start = 0
    maxLenght = float('-inf')
    string = ''

    for n in range(len(str)):
        char1 = str[n]
        if char1 not in char_freq:
            char_freq[char1] = 1
        else:
            char_freq[char1] += 1

        while len(char_freq) > k:
            char2 = str[start]
            char_freq[char2] -= 1

            if char_freq[char2] == 0:
                del char_freq[char2]

            start += 1

        if n - start + 1 > maxLenght:
            string = str[start: n + 1]
    return string

# keep this function call here
print(SearchingChallenge(input()))