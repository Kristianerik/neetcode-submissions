# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
            
        slow, fast, prev = head, head, head
        mid = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        mid = slow
        prev.next = None
        prev = None
        cur = mid

        while cur: 
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        
        cur = head

        while cur and prev:
            left = cur.next 
            right = prev.next 
            cur.next = prev
            if prev and left: prev.next = left
            prev = right
            cur = left

        