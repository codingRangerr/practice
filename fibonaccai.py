# def fib(n):
#     if n < 2:
#         return n

#     else:
#         return (fib(n) + fib(n-1))


# num = int(input("Enter Number"))

# for i in range(num):
#     print(fib(i))


def fib(n):
    a = 0
    b = 1

    if n < 2:
        return n

    else:
        for i in range(1, n):
            c = a+b
            a = b
            b = c

        return b


num = int(input("Enter Number"))

for i in range(num):
    print(fib(i))
