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

def checkSet(n: list):

        #p_sum = previous sum, first sum of the array
        #minus the first number, add the last number of increasing length subsets
        # add list[index] to previous sum

        def checkSub( p_sum: int, n: list, numb: int):

                for numb in range(len(n)):
                        break

        pass
                        
        
        


if __name__ == "__main__":
        #print(primeDigitSums(6))
##        for i in range(6):
##                print(primeDigitSums(i)

        #primeDigitSums(6)
        print(isPrime(121))
                        





        

