# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newhead=ListNode()
        diff=newhead
        right=head
        jackpot=False
        while right:
            while right.next and right.val==right.next.val:
                right=right.next
                jackpot=True
            if jackpot :
                right=right.next 
                if not right or not right.next or right.val!=right.next.val:
                    diff.next=right
                    diff=diff.next
                    jackpot=False
            else: 
                if  diff!=right:
                    diff.next=right
                    diff=diff.next
                right=right.next
        return newhead.next