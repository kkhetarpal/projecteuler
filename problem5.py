#The sum of the squares of the first ten natural numbers is,

#12 + 22 + ... + 102 = 385
#he square of the sum of the first ten natural numbers is,

#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.



def find_solution(num):
    sq = 0
    for i in range(1, num+1):
        sum_of_sqaure+ = pow(i,2)
	sqaure_of_sum = pow((num * (num+1)/2),2)

    return None

if __name__ == '__main__':
    solution = find_solution(100)
    print "found an answer:", solution
