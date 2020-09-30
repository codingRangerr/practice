def ArrayChallenge(arr):

    # code goes here
    for i in arr:
        for j in arr:
            if i*j > 2*(sum(arr)):
                return True

    return False


# keep this function call here
print(ArrayChallenge([2, 2, 2, 2, 4, 1]))
