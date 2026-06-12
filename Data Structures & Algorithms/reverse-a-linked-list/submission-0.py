# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        for each node:
            1. temp = curr.next
            2. curr.next = prev
            3. curr = temp
        '''
        dummy = ListNode(0, head)
        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev