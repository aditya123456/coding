

def bestItem(v, w):
    maxValuePerWeight = 0
    bestItem= 0
    for i in range(1, len(v)):
        if w[i] >0:
            if v[i]/w[i] > maxValuePerWeight:
                maxValuePerWeight = v[i]/w[i]
                bestItem = i

    return bestItem


def KnapSackProblem(W, v, w):
    amount = [0 for i in range(n)]
    totalValue = 0

    for i in range(len(v)):
        if W == 0:
            return (totalValue, amount)
        j = bestItem(v, w)
        a = min(w[j], W)
        totalValue = totalValue + a * v[j]/w[j]
        w[j] = w[j] - a
        amount[j] = amount[j] + a
        W = W - a
    return (totalValue, amount)

