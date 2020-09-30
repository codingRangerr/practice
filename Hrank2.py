
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    count = 0
    height = 0
    prev_height = 0

    for i in path:
        if i== "D":
            height -= 1

        elif i =="U":
            height += 1

        print(i)

        if height == 0 and prev_height < 0:
            count += 1

        prev_height = height

    print(count)

countingValleys(8,"UDDDUDUU")
