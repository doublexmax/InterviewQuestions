# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# adding one X prevents one house
# need to see if adding Y prevents > (Y/X) house -> choose it greedily


def solution(A, X, Y):
    if len(A) == 1:  # if just one house then compare cost of exact vs generator
        return min(X, Y)

    A.sort(reverse=True)  # leading O(NLOGN) operation
    i, j = 0, len(A) - 1

    curPower = 0
    cost = 0
    covered = 0

    # take the current greatest element and see if we turn it into a generator:
    # how many houses can we cover?
    # if the number of houses we can cover provides a better cost than simply
    # having each of the covered houses cover themselves,
    # then we pick that house as a generator
    # if not, then it's not worth it, so just let the house cover itself

    # this is a greedy solution and is optimal because since we don't care about the
    # order in which the houses generate power (does not need to be sequential)
    # then we simply just need to check if the most energy demanding house
    # provides a benefit via providing power to the least-demanding houses
    # and if not then no other house can do either
    # since we are checking the largest energy house, so we can safely turn it into a generator

    # two-pointer i,j solution (but based on ensuring coverage) therefore O(N)
    while covered < len(A):
        # print(i, j, curPower, covered, 'start')
        take = A[i] + curPower
        p = 1
        tj = j
        # run our pointer on the right and see how many houses we can cover
        while i < tj and take - A[tj] >= 0:
            p += 1
            take -= A[tj]
            tj -= 1

        if Y <= p * X:  # it's cheaper to use this house as a generator!
            # print('moving j', 'temp', tj)
            cost += Y
            j = tj
            curPower = take
            covered += p
            # print(j)
        else:  # oops, the number of houses it covered wasn't enough to justify the cost :(
            cost += X
            covered += 1
        i = i + 1  # always covering the starting house
        # print(i, j, curPower, covered, 'end')
    return cost

print(solution([3, 5, 2, 4], 10, 15))  # Expected output: 25
