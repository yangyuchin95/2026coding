#week08-6.py
#875. Koko Eating Bananas
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(k):
            total = 0 #多少時間
            for pile in piles:
                total += pile // k #小時數

                if pile % k  > 0: total += 1
            return total <= h
        return bisect_left( range(1,max(piles)), True, key=helper ) + 1
