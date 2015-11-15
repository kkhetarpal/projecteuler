def find_solution(num):
    diff = 0
    sum_of_square  = 0
    square_of_sum = 0
    for i in range(1, num+1):
        sum_of_square = sum_of_square  + pow(i,2)
        #print sum_of_square
	square_of_sum = pow((num * (num+1)/2),2)
	#print square_of_sum
        i = i+ 1
    diff = square_of_sum-sum_of_square

    return diff

if __name__ == '__main__':
    solution = find_solution(100)
    print "found an answer:", solution
