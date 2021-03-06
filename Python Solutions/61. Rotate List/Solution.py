# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None or head.next==None:
            return head
        
        length = 0
        temp_list = head
        while temp_list!=None:
            length += 1
            temp_list = temp_list.next
        
        k = k % length
        if k == 0:
            return head
        
        for i in range(0,k):

            first = True
            temp_list = head
            initial_val = temp_list.val
            temp_val = temp_list.next.val
            while temp_list.next!=None:
                if first: 
                    temp_val = temp_list.next.val
                    temp_list.next.val = initial_val
                    first = False
                else: 
                    thirdval = temp_list.next.val
                    temp_list.next.val = temp_val
                    temp_val = thirdval

                temp_list = temp_list.next
                if temp_list.next == None:
                    head.val = temp_val
        return head