def mth_to_last(n, arr):

    lst = arr.split(" ")
    if n > len(lst):
        return "NIL"

    else:
        return lst[0 - n]


print(mth_to_last(2, "1 2 3 4 5 6 7 8 9 10"))

print(mth_to_last(20, "1 2 3 4 5 6 7 8 9 10"))