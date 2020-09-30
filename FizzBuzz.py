for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    elif i % 3 == 0:
        print("Fizz")

    elif i % 5 == 0:
        print("Buzz")

    else:
        print(i)
        
  ####################################
def fizzbuzz(num)
    a="Fizz"
    b="Buzz"
    for x in range(1,num):
        print(a+b if x%15==0 else a if x%3==0 else b if x%5==0 else x)
        
