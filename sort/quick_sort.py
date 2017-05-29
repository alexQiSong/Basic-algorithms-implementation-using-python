#############################################################
# By Qi Song
# 05/28/17
#############################################################

# Function for partitioning the subarray into two subarrays
def partition(array,start,end):
    partition_value = array[end]
    i = start-1

    for j in range(start,end):
        if array[j] <= partition_value:
            i += 1
            array[j],array[i] = array[i],array[j]
    array[i+1],array[end] = array[end],array[i+1]

    return i+1

# Recursively sort the left subarray and the right subarray
def quick_sort_recursive(array,start,end):

    # This is the basic case, when there is only one element in the subarray
    if start == end:
        return start

    # Partition the array then recursively sort each part.
    partition_pos = partition(array,start,end)

    if partition_pos > start:
        quick_sort_recursive(array,start,partition_pos-1)

    if partition_pos < end:
        quick_sort_recursive(array,partition_pos+1,end)

# A wrapper function
def quick_sort(array):
    quick_sort_recursive(array,0,len(array)-1)
    return array

# One test case
array = [5,1,9,10,-11,17,105,3,2,13,0,3,4,5,6,3,2,-100]
print quick_sort(array)
