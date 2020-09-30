def minimumBribes(q):

    moves = 0

    q = [P-1 for P in q]

    for i,P in enumerate(q):

        if P - i > 2:
            print("Too chaotic")
            return

        for j in range(max(P-1,0),i):
            if q[j] > P:
                moves += 1
    print(moves)