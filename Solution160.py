# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution160:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ha, hb = headA, headB
        while ha != hb:
            if ha != None:
                ha = ha.next
            else:
                ha = headB
            if hb != None:
                hb = hb.next
            else:
                hb = headA
        return ha