def convert(lst):

    dict1 = {}

    new_lst = []

    sum_lst = []

    for item in lst:
        a = item.split(':')

        new_lst.append(a)

    print(new_lst)

    # for i in new_lst:
    #     if i in new_lst:
    #         sum_lst.append(int(i[1]))

    # print(sum_lst)

    # dict1[a[0]] = int(a[1])

    # return dict1


print(convert(["B:-1", "A:1", "B:3", "A:5"]))


print({'B': '-1', 'A': '1', 'B': '3', 'A': '5'})
