# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        current_node = ListNode(l1.val+l2.val)
        carry = 1 if current_node.val >= 10 else 0
        current_node.val = current_node.val - 10 if carry else current_node.val
        zero_node = ListNode(0)
        new_l = current_node
        while True:
            if not carry and not l1.next and not l2.next:
                break
            else:
                l1_next = l1.next or zero_node
                l2_next = l2.next or zero_node
                next_node = ListNode(l1_next.val+l2_next.val+carry)
                carry = 1 if next_node.val >= 10 else 0
                next_node.val = next_node.val - 10 if carry else next_node.val
                current_node.next = next_node
                current_node = next_node
                l1 = l1_next
                l2 = l2_next
        return new_l
                
