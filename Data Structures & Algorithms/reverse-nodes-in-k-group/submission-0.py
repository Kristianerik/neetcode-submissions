# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prevGroupTail = dummy

        while True:
            kth = self.getKth(prevGroupTail, k)
            if not kth:
                break
            
            groupStart = prevGroupTail.next
            nextGroupStart = kth.next

            kth.next = None
            prevGroupTail.next = self.reverseList(groupStart)

            groupStart.next = nextGroupStart
            prevGroupTail = groupStart
        
        return dummy.next
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            
        return prev
    
    def getKth(self, node, k) -> ListNode:
        while k > 0:
            if node:
                node = node.next
                k -= 1
            else:
                return None
        return node