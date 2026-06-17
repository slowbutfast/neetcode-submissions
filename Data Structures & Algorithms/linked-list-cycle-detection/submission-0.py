# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        slow fast pointer
        """

        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow and fast:
            if slow is fast:
                return True
            
            if not fast.next or not fast.next.next:
                return False
            
            slow = slow.next
            fast = fast.next.next