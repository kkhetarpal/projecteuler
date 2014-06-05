def palindrome(num):
    original = num
    reversed = 0
    
    if num < 10: return 1
    if num % 10 == 0: return 0

    while num >= 1:
        reversed = (reversed * 10) + (num % 10) 
        num = num / 10
    
    if original == reversed: return 1
    else: return 0

# number = 1114
# print palindrome(number)

i = 999
j = 999
check = 0
largest = 0
while i >= 99:
    product = 0
    j = 999
    while j >= 99:
        product = i * j
        #print i,j,product
        check = palindrome(product)
        if check == 1:
            if largest < product:
                largest = product
                print largest
        j = j -1
    i = i - 1
