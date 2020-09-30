def max_game_score(cells):
    # Write your code here
    lst = []
    for num in cells:
        if num > 3 or num < -3:
            for i in range(2,num):
                if num%i ==0:
                    break
                else:
                    lst.append[num]
    return sum(lst)


print(max_game_score())