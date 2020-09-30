def longest_substring_with_k_distinct(str, k):
    char_frequency = {}
    window_start = 0
    maxLength = float("-inf")

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
        maxLength = max(maxLength, window_end-window_start+1)
    return maxLength


print(longest_substring_with_k_distinct('aabacbebebe', 3))
