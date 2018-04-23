class Solution:
#problem descriptions:
        # given a list and a target, return the first set of numebrs that adds up to the target.
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        
        def findSums(nums, target, curr):
            if target == 0:
                ans.append( curr )
            
            
            for index, item in enumerate(nums):

                if index in curr: continue
                result = target - item
                
                if result < 0:
                    continue
                new_curr = curr + [index]
                findSums(nums, result, new_curr)

        
        findSums( nums, target, [])
        return ans

checking = Solution()

test1 = [8,2,5,3]
test2 = [11,15,25,2,1,4]
test3 =[100,23,26,4,5,11,17]

all_test = [test1,test2,test3]
for each in all_test:
        break
print(checking.twoSum(test1,11))
