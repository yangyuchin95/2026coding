#week01-4.py
#1431. Kids With the Greatest Number of Candies
#給額外的extraCandies後 小朋友手上的糖果會不會是最多
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        #不上傳
        ans = []
        best = max(candies)
        for candie in candies: #逐一檢查
            if candie + extraCandies >= best: ans.append(True)
            else: ans.append(False)  #他會不會>=最多 依序塞入ans
        return ans
