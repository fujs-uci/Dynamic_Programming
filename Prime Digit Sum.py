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
        if n == 0:
                return False
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

        count = 0
        number_list = []
        for item in range(start,end+1):
                if checkSet(item):
                        number_list.append(item)
                        count += 1
        
        return number_list


def checkSet(n: int):

        #p_sum = previous sum, first sum of the array
        #minus the first number, add the last number of increasing length subsets
        # add list[index] to previous sum

        first_list = indexInt(n) #first list is a list of length 1 already

        
        def checkSub(n: list,  length: int, end: int):
                new_list = []
                new_length = length + 1
                satisfies = True
                
                if length > end-1:
                        return satisfies
                for numb in range(len(n)):
                        if numb + 1 > len(n)-1:
                                break
                        prev = n[numb] if type(n[numb]) == list else [n[numb]]
                        new_numb = prev + [first_list[numb+ length]]
                        if len(new_numb) in [3,4,5]:
                                if not isPrime(sum(new_numb)):
                                        satisfies = False
                                        break
                        new_list.append(new_numb)
                return checkSub(new_list, length + 1, end) and satisfies


        pass

        return checkSub(first_list, 1, 5)
                        

        


if __name__ == "__main__":

        pds = primeDigitSums(6)
        print(pds)
        print(len(pds))

                        





        

