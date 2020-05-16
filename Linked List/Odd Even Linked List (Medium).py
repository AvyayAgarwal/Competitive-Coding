# 328. Odd Even Linked List - Medium
# Tags - Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if(head is None or head.next is None):
            return head
        oddptr = head
        evenhead = head.next
        evenptr = head.next
        while(oddptr != None):
            if(evenptr.next is None):
                oddptr.next = evenhead
                break
            oddptr.next = evenptr.next
            oddptr = oddptr.next
            evenptr.next = oddptr.next
            evenptr = evenptr.next
            if(evenptr is None):
                oddptr.next = evenhead
                break
        return head