"""
Problem:
        find the median of two sorted arrays

Completed:
        while loop

Attempt:
        recursion
"""


class findMedianSortedArrays:
        
        def whileLoop(self, nums1, nums2):
                """140 ms, 22 percentile: BAD"""
                l1 = nums1
                l2 = nums2
                final1 = 0
                final2 = 0
                
                while((len(l1) > 0 or len(l2) > 0)):
                        small = 0
                        large = 0
                        change1 = 0
                        change2 = 0
                        
                        if ((len(l1) >0) and (len(l2) > 0)):
                                if l1[0] < l2[0]:
                                        small = l1[0]
                                        change1 -=2
                                else:
                                        small = l2[0]
                                        change1 -=3

                                if l2[-1] > l1[-1]: 
                                        large = l2[-1]
                                        change2 +=3
                                else:
                                        large = l1[-1]
                                        change2 +=1
                        elif len(l1) == 0:
                                small = l2[0]
                                large = l2[-1]
                                change1 -=3
                                change2 +=3
                        elif len(l2) == 0:
                                small = l1[0]
                                large = l1[-1]
                                change1 -=2
                                change2 +=1

                        if small > large:
                                break
                        
                        else:
                                check = change1 + change2
                                if check == -1:
                                        l1 = l1[1:-1]
                                elif check == 1:
                                        l1 = l1[1:]
                                        l2 = l2[:-1]
                                elif check == -2:
                                        l1 = l1[:-1]
                                        l2 = l2[1:]
                                elif check == 0:
                                        l2 = l2[1:-1]

                                final1 = small
                                final2 = large
                                
                return ((final1 + final2)/2)
                                
                        
        def recursion(self, nums1, nums2):
                """228 ms, 2 percentile: BAD very BAD"""
                def findThem(nums1, nums2):
                        if len(nums1) == 0 and len(nums2) == 0:
                                return 0
                        
                        elif len(nums1) == 1 and len(nums2) == 1:
                                return ((nums1[0] + nums2[0])/2)
                        
                        elif len(nums1) == 1 and len(nums2) == 0:
                                return float(nums1[0])
                        
                        elif len(nums1) == 0 and len(nums2) == 1:
                                return float(nums2[0])
                        elif len(nums1) == 2 and len(nums2) == 0:
                                return ((nums1[0] + nums1[-1])/2)
                        elif len(nums1) == 0 and len(nums2) == 2:
                                return ((nums2[0] + nums2[-1])/2)
                        
                        else:
                                if len(nums1) >= 1 and len(nums2) >= 1:
                                        if nums1[0] < nums2[0]:
                                                if nums1[-1] > nums2[-1]:
                                                        return findThem(nums1[1:-1], nums2)
                                                else:
                                                        return findThem(nums1[1:], nums2[:-1])
                                        else:
                                                if nums1[-1] > nums2[-1]:
                                                        return findThem(nums1[:-1], nums2[1:])
                                                else:
                                                        return findThem(nums1, nums2[1:-1])
                                else:

                                        if len(nums1) == 0 and len(nums2) > 1:
                                                return findThem(nums1, nums2[1:-1])
                                        else:
                                                return findThem(nums1[1:-1], nums2)
                return findThem(nums1, nums2)

        
                                                                
                

test1 = (([1,3], [2]), 2.0)
test2 = (([1,2], [3,4]), 2.5)
test3 = (([1,5,7],[6,8,12]), 6.5)
test4 = (([1,1,1,1],[7,8,8,8,10,11]), 7.5)
test5 = (([],[]), 0.0)
test6 = (([0],[0]),0)

testSol = [test1, test2,test3,test4,test5, test6]
c = findMedianSortedArrays()

f = [2]
print("While loop test...")
for tests, sol in testSol:
        val = c.whileLoop(tests[0], tests[1])
        try:
                assert ( val == sol )
                print(tests[0], tests[1], val)
        except:
                print("***fail***", tests[0], tests[1], sol, val)

print("recursion test...")
for tests, sol in testSol:
        val = c.recursion(tests[0], tests[1])
        try:
                assert( val == sol)
                print(tests[0], tests[1], val)
        except:
                print("***fail***", tests[0],tests[1], sol, val)
        
