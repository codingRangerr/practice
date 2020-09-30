max = int(input("Enter Maximum Number: "))

for i in range(max):
    if i == 0 or i == (max-1):
        print("0" * max)

    else:
        print("0", "1" * (max-2), "0", sep="")