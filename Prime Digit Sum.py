import math

"""

for every possible n digit number
start -> 1*10^(n-1)
end -> 1*10^(n)
y = [3,4,5]

n - (y -1) = number of possible combinations

"""
        
def isPrime(n):
        prime = True
        check = math.sqrt(n)
        if n == 1:
                return False
        if n == 2:
                return True
        for i in range(2,math.ceil(check)+1):
                if n % i == 0:
                        prime = False
                        break
        return prime

def indexInt(n):
        #turns an int into a list of ints
        index = [int(i) for i in str(n)]
        return index

def primeDigitSums(n):
        start = (1*(10**(n-1)))
        end = (1*(10**(n)))
        combos = [3,4,5]
        
        # n - ( [3,4,5] - 1) = # of combinations
        #for every n digit number
                #for digit in [3,4,5]
                        #for every possibility
                                #check sum = prime

        #3,4,5 property only applies to lengths that it applies to.
        ans = []
        pass

def checkSet(n: int):

        #p_sum = previous sum, first sum of the array
        #minus the first number, add the last number of increasing length subsets
        # add list[index] to previous sum

        first_list = indexInt(n) #first list is a list of length 1 already

        satisfies = True
        
        def checkSub(n: list,  length: int, end: int):
                new_list = []
                new_length = length + 1
                if length > end-1:
                        return
                for numb in range(len(n)):
                        if numb + 1 > len(n)-1:
                                break
                        prev = n[numb] if type(n[numb]) == list else [n[numb]]
                        new_numb = prev + [first_list[numb+ length]]

                        if length in [3,4,5]:
                                if not isPrime(sum(new_numb)):
                                        satisfies = False
                                        break
                        new_list.append(new_numb)

                checkSub(new_list, length + 1, end)


        pass

        checkSub(first_list, 1, 5)
                        
        return satisfies
        


if __name__ == "__main__":
        #print(primeDigitSums(6))
##        for i in range(6):
##                print(primeDigitSums(i)

        #primeDigitSums(6)
        print(checkSet(101501))
                        





        

