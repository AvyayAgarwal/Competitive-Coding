# 21. Merge Two Sorted Lists - Easy
# Tags - Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        ptr = head
        
        while(l1 != None or l2 != None):
            if l1 is None:
                ptr.next = l2
                break
            if l2 is None:
                ptr.next = l1
                break
                
            if l1.val <= l2.val:
                ptr.next = l1
                l1 = l1.next
                ptr = ptr.next
            else:
                ptr.next = l2
                l2 = l2.next
                ptr = ptr.next
        return head.next