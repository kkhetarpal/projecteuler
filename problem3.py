#What is the largest prime factor of the number 600851475143 ?

import math
import time
start =  time.time()
#num = 13195
num = 600851475143

factors = []
largest = []
for i in range(1,num+1):
    if (num%i == 0):
        factors.append(i)

<<<<<<< HEAD
#print factors
#print length
=======
print factors                                    #I get the factors in a list in ascending order
length = len(factors)        
print length                                    #this num has say 16 factors 

>>>>>>> a7be800643281d11174d7d381bb276dde75475ac

length = len(factors)
j = length-1


<<<<<<< HEAD
while j < length and j >= 0 :
    count = 0
    num  = factors[j]
    #print num 
    for k in range(2,num):
        if (num%k == 0):
           count = 1 
    #print count
    if (count == 0):
        print(num)
        break
    j = j - 1
      
=======
for j in range(length-1,1):                     #As output I get only factors and length : THe flow never gets here !
    numm = factors[j]                           #Any clue what am I doing wrong 
    print numm
    for k in range(2,numm-1):
        if (numm%2 == 0):
            j = j - 1
        else:
            print numm
        
          
>>>>>>> a7be800643281d11174d7d381bb276dde75475ac
#print time.time() - start
