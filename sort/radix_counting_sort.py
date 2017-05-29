#############################################################
# By Qi Song
# 05/29/17
#############################################################

#-------------------------------------------------------------------
# Sort the array using specified digit
#-------------------------------------------------------------------
def counting_sort(array,digit):
    count = [0]*10
    result = [0]*len(array)
    for i in range(len(array)):
        num = int(array[i][digit])
        count[num] += 1

    for j in range(1,len(count)):
        count[j] += count[j-1]

    for i in range(len(array)-1,-1,-1):
        num = int(array[i][digit])
        result[count[num]-1] = array[i]
        count[num] -= 1
    return result

#---------------------------------------------------------------------
# Now the radix sort function only takes non-negative numbers as input
#---------------------------------------------------------------------
def radix_sort(array):

    # Convert to string array and get the maximum number of digits
    array = map(str,array)
    max_digit = max(map(len,array))

    # Complement the left most positions with zero, if the number of
    # digits for current number is smaller than max_digit
    for i in range(len(array)):
        array[i] = "0"*(max_digit-len(array[i]))+array[i]

    # For each digit call counting_sort() to sort the array
    for i in range(max_digit-1,-1,-1):
        array = counting_sort(array,i)

    # Remove all the preceding zeros
    for i in range(len(array)):
        while array[i][0] == 0 and len(array[i]) > 1:
            array[i] = array[i][1:]
        array[i] = int(array[i])
    return array

# One test case
array = [1,24,3,4,6,714,1,3,5,3,2,1,9,1,44,60,1,1]
print radix_sort(array)