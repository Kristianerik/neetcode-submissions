# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:   
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        
        if n == count:
            return head.next
            
        cur, prev = head, head
        t = (count) - n
        count = 0

        while cur:
            if count == t:
                prev.next = cur.next
                break
            else:
                prev = cur
                cur = cur.next
                count += 1

        return head