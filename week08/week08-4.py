#week08-4.py
#2300. Successful Pairs of Spells and Potions
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort() #藥水小到大排好
        p = len(potions)
        ans = []
        for spell in spells:
            now = p - bisect_left(potions, success/spell)
            ans.append(now) #全部p瓶-會失敗的藥水??瓶
        return ans
