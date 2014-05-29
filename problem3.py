#What is the largest prime factor of the number 600851475143 ?


import time
start =  time.time()
num = 13195
all = range(1,num+1)
factors = []
largest = []
for i in all:
    if (num%i == 0):
        factors.append(i)

print factors
length = len(factors)        
print length

for j in range(length,1):
    numm = factors[j]
    print numm
    for k in range(2,numm-1):
        if (numm%2 == 0):
            j = j - 1
        else:
            print numm   
          
print time.time() - start
