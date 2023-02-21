# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        count = 0

        if curr == None:
            return curr
        
        while curr.next:
            count += 1
            curr = curr.next
        count += 1
        k = k % count
        if k == 0:
            return head
        
        length = count - k
        point = prev = output = head
        while length:
            prev = point
            point = point.next
            length -= 1
        output = point
        curr.next = head
        prev.next = None
        return output


