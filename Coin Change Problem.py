#===============================
# Problem:   Given a target integer and a list of integers, find all possible
#                     combinations of the list of integers that sum up the target.
#===============================


# ===============================
#  Recursion
# ===============================

def get_ways( total: int, values: list ):
        
        answer = []
        
        def find_ways( total:int, values: list, curr: list):
        # curr = list of current value used to reduce total
                final = []
                if total == 0:
                        new_curr = sorted(curr, reverse = True)
                        if new_curr not in answer:
                                answer.append(new_curr)
                
                else:
                        for index, item in enumerate(values):
                                result = total - item
                                if result >= 0:
                                        new_curr = curr + [item]
                                        find_ways(result, values, new_curr)                                

        find_ways(total, values, [])

        return answer

print(get_ways(10,[2,5,3,6]))
