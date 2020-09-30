def smallest_positive(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.

    # new_list = []
    #
    # for item in in_list:
    #     if item > 0:
    #         new_list.append(item)
    #
    # return min(new_list)

    small_pos = 0

    for num in in_list:
        if num > 0:
            if small_pos == 0 or small_pos > num:
                small_pos = num

    return small_pos


# Test cases

print('Correct output:', smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print('Correct output:', smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2