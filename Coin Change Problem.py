#===============================
# Problem:   Given a target integer and a list of integers, find all possible
#                     combinations of the list of integers that sum up the target.
#===============================


# ===============================
#  Recursion
# ===============================

def get_ways_r( total: int, values: list ):
        
        answer = []
        count = []
        def find_ways( total:int, values: list, curr: list):
        # curr = list of current value used to reduce total
        
                final = []
                if total == 0:
                        new_curr = sorted(curr, reverse = True)
                        if new_curr not in answer:
                                answer.append(new_curr)
                                #total = 0 so we append the curr into the answer list
                
                else:
                        for index, item in enumerate(values):
                                result = total - item
                                if result >= 0:
                                        new_curr = curr + [item]
                                        count.append(1)
                                        find_ways(result, values, new_curr)
                                        #recursion: result = recuded total; new_curr = curr with item appended

        find_ways(total, values, [])
        
        return len(count), answer

# ===============================
#  Memoization
#       create a default dict
#       the keys = the totals
#       values = list of curr that are called along the total
#       Before each call, check if the total, and the curr exist, if they do, skip.
# ===============================
from collections import defaultdict

def get_ways_m( total: int, values: list ):
        answer = []
        memoize = defaultdict(list)
        #new data structure to keep account of all {total:[curr]} occurences
        count = []

        def find_ways(total: int, values: list, curr: list):
                final = []
                if total == 0:
                        new_curr = sorted(curr, reverse = True)
                        if new_curr not in answer:
                                memoize[total].append(new_curr)
                                #add the answer into the memoize
                                #all answers should be in key = 0
                                answer.append(new_curr)

                else:
                        for index, item in enumerate(values):
                                result = total - item
                                if result >= 0:
                                        new_curr = sorted(curr + [item])
                                        if new_curr not in memoize[total]:
                                                #check memoize
                                                memoize[total].append(new_curr)
                                                count.append(1)
                                                find_ways(result, values, new_curr)
                
        find_ways(total, values, [])
        return len(count), answer


#=============================
# Analysis and Comparison of different methods
#=============================

test_cases = [10,20,30]
values = [2,5,3,6]

for tc in test_cases:
        m1, m2 = get_ways_m(tc, values)
        r1, r2 = get_ways_r(tc,values)

        #print( "total: {}, recursion: {}, memoization: {}".format(tc, r1, m1))
        
#number of recursive calls for each total value.
#total: 10, recursion: 49, memoization: 36
#total: 20, recursion: 2533, memoization: 322
#total: 30, recursion: 128228, memoization: 1287
                 
