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
        #dictionary might make this extremely slow
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

# ===============================
# Iteration/ Dynamic Programming
# ===============================

def get_ways_i( total: int, values: list ):
        iterations = [0 for iters in range(total+1)]
        #think of this array representing the number you multiple the value in values to get the index
        # index = numbers in range(total+1)
        for value in values:
                for index, item in enumerate(iterations):
                        #iterations array becomes  like a two dimensional array as value in values iterates
                        # the previous iteration's array gets added to the current iteration's array
                        result = index - value
                        if result < 0:
                                continue
                        elif index == value:
                                iterations[index] += 1
                        else:
                                iterations[index] += iterations[result]
                                #adding the previous array to the current array
                        

        return iterations[total]
