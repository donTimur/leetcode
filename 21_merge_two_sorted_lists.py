#https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode):
    if l1 is None:
        return l2

    if l2 is None:
        return l1

    head = tail = ListNode(0)

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return head.next