#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#Eliminating the divisibility check by removing 1( every integer is evenly divisible by 1)
#Keeping 20 means we can remove 4,5,2
##Keeping 18 means we can remove 3,6,9
#Keeping all primes; 11,13,17,19
#Keeping 14 means we can remove 7,2


check_list = [11, 13, 14, 16, 17, 18, 19, 20] #Eliminating multiples of these
def find_solution(step):
    for num in xrange(step, 999999999, step):
        if all(num % n == 0 for n in check_list):
            return num
    return None

if __name__ == '__main__':
    solution = find_solution(20)
    if solution is None:
        print "No answer found"
    else:
        print "found an answer:", solution
