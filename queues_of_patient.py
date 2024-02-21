
def minimumWaitinTime(n, timear):
    waitingTime = 0
    treated = [0 for i in range(n)]
    for i in range(1, n):
        tmin = 9999999
        minIndex = 0
        for j in range(1, n):
            if treated[j]==0 and timear[j] < tmin:
                tmin = timear[j]
                minIndex = j
        waitingTime = waitingTime + (n-i) *tmin
        treated[minIndex] = 1
    return waitingTime

print(minimumWaitinTime(5, [20, 15, 35, 10, 12]))
