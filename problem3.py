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

print factors                                    #I get the factors in a list in ascending order
length = len(factors)        
print length                                    #this num has say 16 factors 


#numm = []
# numm.append(factors[15])
# print numm


for j in range(length-1,1):                     #As output I get only factors and length : THe flow never gets here !
    numm = factors[j]                           #Any clue what am I doing wrong 
    print numm
    for k in range(2,numm-1):
        if (numm%2 == 0):
            j = j - 1
        else:
            print numm
        
          
#print time.time() - start
