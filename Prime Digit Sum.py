import math
        
def isPrime(n):
        #returns a prime number.
        # 0,1,2 are hard coded. This is an expensive function..
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
        # time complexity O(n)
        index = [int(i) for i in str(n)]
        return index

def primeDigitSums(n):
        # this is also expensive. loops through all possible n digit numbers
        # checks all 1,2,3,4,5 combinations
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
        # checks all combinations of length 1,2,3,4,5
        first_list = indexInt(n)

        
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

        return checkSub(first_list, 1, 5)
                        

        


if __name__ == "__main__":

        pds = primeDigitSums(6)
        print(pds)
        print(len(pds))

                        





        

