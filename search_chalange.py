# ["B:-1", "A:1", "B:3", "A:5"]

def search_challenge(string):
    lst = []
    alph = {}

    for item in string:
        lst.append(item.split(":"))

    print(lst)

    for char in lst:
        if char[0] not in alph:
            alph[char[0]] = int(char[1])

        else:
            alph[char[0]] += int(char[1])
    print(alph)

    new = {}

    for i in sorted(alph):
        new[i] = alph[i]

    print(new)


search_challenge(["B:-1", "A:1", "B:3", "A:5"])
