#week09-2.py
#206. Reverse Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = [] #容易理解 把Linked List變陣列
        while head:
            a.append( head.val ) #塞到陣列a後
            head = head.next #換下一筆
        now = ans = ListNode() #答案將串到裡面
        N = len(a)
        for i in range(N-1, -1, -1):
            now.next = ListNode(a[i])
            now = now.next
        return ans.next
