def sockMerchant(n, ar):
    dict1 = {}

    for i in ar:
        if i not in dict1:
            dict1[i] = 1

        else:
            dict1[i] += 1

    print(dict1)

    count = 0
    for item in dict1:
        if dict1[item] >1:
            count += (dict1[item]//2)

    print(count)


sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20,20,30,60, 50])