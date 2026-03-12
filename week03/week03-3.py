#week03-3.py
#1456. Maximum Number of Vowels in a Substring of Given Length
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        count = 0 #紀錄目前有幾個母音
        for i in range(k): #找前面k個字母 檢查看是不是母音
            if s[i] in vowels: count += 1
        ans = count
        N = len(s)
        for i in range(k, N): #右邊每個字母逐一檢查
            if s[i] in vowels: count += 1
            if s[i-k] in vowels: count -= 1
            ans = max(ans,count)
        return ans
