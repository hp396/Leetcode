# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first_head =second_head= head
        
        for i in range(n):
            second_head = second_head.next
            
            
        if second_head == None:
            return first_head.next
        
        while second_head.next != None:
            second_head = second_head.next
            first_head = first_head.next
            
        first_head.next = first_head.next.next
        return head