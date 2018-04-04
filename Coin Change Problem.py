from collections import defaultdict
# 4, [1,2,3]
#[[1,1,1,1],[1,1,2],[2,2],[1,3]]

## Test case 1
goal = 10
test = [2,3,5,6]
test2 = [2,3,5,6]

memoize = defaultdict(list)

#correct numbers, but how to store them when retrning up the recursion....
# is this dynamic programming???

def get_ways( total: int, values: list ):
        
        memoize = defaultdict(list)
        
        values = sorted(values)
        print(values)
        def fill_memoize( total:int, values: list, curr: int):
                print(memoize, total, curr)
                input("...")
                final = []
                if total == 0:
                        return curr
                
                elif total in memoize.keys():
                        looped = []
                        print("in")
                        for index, item in enumerate(memoize[total]):
                                print("in", looped, total, item)
                else:
                        looped = []
                        for index, item in enumerate(values):
                                result = total - item
                                if result >= 0:
                                        memoize[total].append(total-item)
                                        looped.append(fill_memoize(result, values, item))
                                        print("not in", looped, total, item)
                                print("looped", looped)
                                final += looped
                        print("final", final)
                        return final


        result = fill_memoize(total, values, total)

        #set(item for item in result)
        print(memoize)
        return result

check = get_ways(10, [2,5,3,6])
print(check)


