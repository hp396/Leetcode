# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = ""
        num2 = ""
        while l1 != None:
            num1 += str(l1.val)
            l1 = l1.next
        while l2 != None:
            num2 += str(l2.val)
            l2 = l2.next
        num1 = num1[::-1]
        num2 = num2[::-1]
        output = str(int(num1) + int(num2))[::-1]
        prevnode = None
        result = None
        for i in output:
            node = ListNode(i)
            if result is None:
                result = node
            if prevnode is not None:
                prevnode.next = node
            prevnode = node
        return result