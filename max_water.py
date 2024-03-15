class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_product = 0
        for i in range(len(height)):
            for j in range(len(height)):
                if i >= j:
                    item = min(height[i], j)
                else:
                    item = min(height[i], j - i)
                print(item)
                if item * item >= max_product:
                    max_product = item * item
        return max_product


