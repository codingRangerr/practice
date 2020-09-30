def rotate_left(arr, n):

    lst = []

    for i in range(n, len(arr)):
        lst.append(arr[i])

    for j in range(n):
        lst.append(arr[j])

    return lst


print(rotate_left([1, 2, 3, 4, 5], 3))