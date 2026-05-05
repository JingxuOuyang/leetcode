from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        n = 0
        cur = head
        while cur.next:
            n += 1
            cur = cur.next
        if n == 0:
            return None
        k = k % n
        if k == 0:
            return head
        k = n - k
        tail = cur
        cur = head
        while k > 1:
            k -= 1
            cur = cur.next
        tail.next = head.next
        head = cur.next
        cur.next = None
        return head
        
        