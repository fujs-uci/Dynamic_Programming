import math

"""

for every possible n digit number
start -> 1*10^(n-1)
end -> 1*10^(n)
y = [3,4,5]

n - (y -1) = number of possible combinations

"""


def primeDigitSums(n):
        start = (1*(10**(n-1)))
        end = (1*(10**(n)))
        combos = [3,4,5]
        
        # n - ( [3,4,5] - 1) = # of combinations
        #for every n digit number
                #for digit in [3,4,5]
                        #for every possibility
                                #check sum = prime
        for i in range(start, end):
                break
        print(isPrime(n))
        print(indexInt(n))
        
def isPrime(n):
        prime = True
        check = math.sqrt(n)
        if math.ceil(check) == check:
                return False
        for i in range(2,math.ceil(check)):
                if n % i == 0:
                        prime = False
                        break
        return prime

def indexInt(n):
        #turns an int into a list of ints
        index = [int(i) for i in str(n)]
        return index

if __name__ == "__main__":
        #print(primeDigitSums(6))
##        for i in range(6):
##                print(primeDigitSums(i)
        primes = []
        for i in range(1000):
                if isPrime(i):
                        primes.append(i)

        primeDigitSums(6)






        

