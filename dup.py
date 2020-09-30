def check_duplicates(check_string):

    # chars = "abcdefghijklmnopqrstuvwxyz"
    #
    # for char in chars:
    #     count = check_string.count(char)
    #     print(count)
    #     if count > 1:
    #         print(char, ":", count)

    alph = {}
    ch = ''
    # count = 0

    for char in check_string:
        if char not in alph:
            alph[char] = 1

        else:
            alph[char] += 1

    for val in alph:
        if alph[val] > 1:
            # count = alph[val]
            # ch = val
            print(val, ":", alph[val])

    print(alph)


check_duplicates("amit kumar gautam")