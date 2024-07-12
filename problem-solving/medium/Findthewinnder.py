class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [i for i in range(1, n+1)]
        first = players[0]
        index = 0
        while len(players) > 1:
            rm_index = (index + k -1)% len(players)
            players.pop(rm_index)
            index = rm_index
        return players[0]