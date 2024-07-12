class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        maxDrink = 0
        while numBottles >= numExchange:
            maxDrink = maxDrink + numExchange
            numBottles = numBottles - numExchange

            numBottles += 1

        return maxDrink + numBottles

