#week08-2.py
#374. Guess Number Higher or Lower

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
class Solution:
    def guessNumber(self, n: int) -> int:
        #for i in range(1, n+1): #錯誤暴力法for迴圈
        #if guess(i)==0: return i #猜中
        #不能用上面迴圈 因為n有20億
        #要用猜數字每次猜一半
        left, right = 1, n
        while left<right:
            mid = (left+right) // 2 #(猜)中間數
            if guess(mid)==0: return mid #猜到中間的數
            if guess(mid)>0: left = mid+1 #再高一點
            else: right = mid #再低點
        return left
