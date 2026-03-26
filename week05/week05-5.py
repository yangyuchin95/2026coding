#week05-5.py
#1657. Determine if Two Strings Are Close
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter1 = Counter(word1) #統計用過的字母
        counter2 = Counter(word2)

        #用過字母是否是相同集合
        if set(counter1.keys()) != set(counter2.keys()):
            return False
        #把出現次數小到大排好 如兩邊一樣就可以換到一樣為止
        if sorted(counter1.values()) != sorted(counter2.values()):
            return False
        return True
