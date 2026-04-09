#week07-4.py
#394. Decode String
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        nowN, nowS = 0, ''
        for c in s:
            if c.isdigit(): #若是數字就用十進位組合起來
                nowN = nowN*10+int(c)
            elif c.isalpha(): #如果是字母就讓字串變長
                nowS += c
            elif c=='[': #上括號: 數字 字串放入stack
                stack.append( (nowN, nowS) )
                nowN, nowS = 0, '' #一組新的數字 字串
            elif c==']': #下括號:取出數字 字串
                prevN, prevS = stack.pop()
                nowS = prevS + prevN * nowS
        return nowS
