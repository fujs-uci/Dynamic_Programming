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
        recursive method

"""

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
        
class addTwoNumbers:

    def whileLoop(self, l1, l2):
        """Iterative method with a while loop"""
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

    def recursion(self, l1,l2):
        """recursive method that wil recursively call .next on each of the linked lists"""
        c = l1.val + l2.val
        r = 0
        
        if c > 9:
                c = c - 10
                r = 1

        ans = ListNode(c)
        
        def goingIn(ans, l1, l2, r):
                one = l1
                two = l2
                c = 0
                        
                if one != None:
                        c += one.val
                        
                if two != None:
                        c+= two.val

                if r == 1:
                        c += r
                        r = 0

                if c > 9:
                        c = c - 10
                        r = 1

                ans.next = ListNode(c)
                
                if one== None and two == None:
                        if r == 1:
                                goingIn(ans.next, None, None, r)
                        else:
                              if c == 0:
                                   ans.next = None

                                
                elif one != None and two != None:
                        goingIn( ans.next, l1.next, l2.next, r)
                        
                else:
                        if one != None:
                                goingIn(ans.next, l1.next, None, r)
                                
                        if two != None:
                                goingIn(ans.next, None, l2.next, r)


        goingIn(ans, l1.next, l2.next, r)
        
        return ans



                

"""
Test cases
"""
prob = addTwoNumbers()

one = ListNode(5)
#one.next = ListNode(4)
#one.next.next = ListNode(3)

two = ListNode(5)
#two.next = ListNode(6)
#two.next.next = ListNode(4)


c = prob.whileLoop(one,two)
print(c.val, c.next.val)#, c.next.next.val)

d = prob.recursion(one,two)

print(d.val, d.next.val)#, d.next.next.val)

