#week09-5.py
#2095. Delete the Middle Node of a Linked List
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = fast = slow = head

        while fast != None and fast.next != None:
            fast = fast.next.next #兔子跳2格
            prev = slow
            slow = slow.next #烏龜走1格
        #print( slow.val ) #當兔子到終點時，烏龜在中間
        prev.next = slow.next
        return head
