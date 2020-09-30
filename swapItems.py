lst = [89,91,30,57,72,79,90]
start = 0
end = len(lst) - 1

while start != end:
    if lst[start]%2==0:
        start +=1
    

    if lst[start]%2 != 0 and lst[end]%2 == 0:
        lst[start], lst[end] = lst[end], lst[start]
        start +=1
        end -= 1

    if lst[end]%2 != 0:
        end -= 1



print(lst)


