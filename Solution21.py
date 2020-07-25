# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution21:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None: 
            return l2
        if l2 == None: 
            return l1
        first = ListNode(0)
        temp = first
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        if l1:
            temp.next = l1 
        else:
            temp.next = l2
        return first.next