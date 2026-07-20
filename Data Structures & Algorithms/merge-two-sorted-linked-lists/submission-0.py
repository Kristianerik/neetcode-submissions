# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()
        curOne = list1
        curTwo = list2
        current = new_head

        while curOne or curTwo:
            if curOne and (not curTwo or curOne.val <= curTwo.val):
                current.next = curOne
                curOne = curOne.next
            else:
                current.next = curTwo
                curTwo = curTwo.next

            current = current.next
        
        return new_head.next