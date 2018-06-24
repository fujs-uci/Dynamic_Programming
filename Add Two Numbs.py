# Definition for singly-linked list.
"""
Problem definition:
        given two linked lists of numbers in reverse order
        return a linked list of the sum of the two given linked lists

challenge:
        each linked list value is one place value
        much carry over a 1 when the place value is exceeded

completed:
        while loop method

attempt:
        recursive method
"""

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
        
class addTwoNumbers:

    def whileLoop(self, l1, l2):        
        value = 0
        r = 0
        curr_l1 = l1
        curr_l2 = l2
        head = None
        curr = None

        while(curr_l1 or curr_l2 or r == 1):
                
                if curr_l1 != None and curr_l2 != None:
                        value += curr_l1.val + curr_l2.val

                elif curr_l1 == None and curr_l2 == None:
                        pass
                        
                elif curr_l1 == None:
                        value += curr_l2.val
                        
                elif curr_l2 == None:
                        value += curr_l1.val

                if r == 1:
                        value += 1
                        r = 0
                        
                if value > 9:
                        value = value - 10
                        r = 1

                if head == None:
                        head = ListNode(value)
                        curr = head
                else:
                        curr.next = ListNode(value)
                        curr = curr.next

                value = 0
                curr_l1 = curr_l1.next if curr_l1 != None else None
                curr_l2 = curr_l2.next if curr_l2 != None else None
        
        return head

                


prob = addTwoNumbers()

one = ListNode(1)
one.next = ListNode(2)
one.next.next = ListNode(3)

two = ListNode(9)
two.next = ListNode(8)
two.next.next = ListNode(7)


c = prob.whileLoop(one,two)
print(c.val, c.next.val, c.next.next.val, c.next.next.next.val)

