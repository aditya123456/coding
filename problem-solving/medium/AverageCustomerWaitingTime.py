class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        finish = sum(customers[0])
        waitingtime = finish - customers[0][0]
        print(customers[1:])
        for i in customers[1:]:
            print()
            finish = max(i[0] + i[1], finish + i[1])
            waitingtime = waitingtime + finish - i[0]
            print(finish, waitingtime)
        return waitingtime / len(customers)

