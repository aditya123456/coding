class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for i in logs:
            if i != '../' and i != './':
                depth += 1
            elif i == './':
                depth = depth
            elif depth > 0:
                depth -= 1
        if depth < 0:
            return 0
        else:
            return depth
