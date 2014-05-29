#What is the largest prime factor of the number 600851475143 ?


import time
start =  time.time()
num = 13195
#num = 600851475143
#all = xrange(1,num+1)
factors = []
largest = []
for i in xrange(1,num+1):
    if (num%i == 0):
        factors.append(i)

#print factors
length = len(factors)        
#print length

length = len(factors)
j = length-1


while j < length and j >= 0 :
    count = 0
    num  = factors[j]
    #print num 
    for k in xrange(2,num):
        if (num%k == 0):
           count = 1 
    #print count
    if (count == 0):
        print num
        break
    j = j - 1
      
#print time.time() - start
