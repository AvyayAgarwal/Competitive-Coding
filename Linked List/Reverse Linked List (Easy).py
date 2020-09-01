# 206. Reverse Linked List - East
# Tags - Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        ptr = head
        while(ptr != None):
            temp = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = temp
        return prev