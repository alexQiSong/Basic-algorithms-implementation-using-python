#############################################################
# By Qi Song
# 05/26/17
#############################################################

#--------------------------------------------------------------------------
# This is a linear and non-recursive algorithm for finding maximum subarray
def find_max_subarray(array):

    # Initialization max_sum: the current maximum subarray in [0,i]
    #                max_start: the start position of current maximum subarray
    #                max_end: the end position of current maximum subarray
    #                right_sum: the current maximum subarray which ends at i
    #                right_start: the start position of current maximum subarray which ends at i
    max_sum = max_start = max_end = 0
    right_sum = right_start = 0

    for i in range(len(array)):

        # Whether to update the maximum subarray which ends at i.
        # If we denote this subarray as sub_A[i]. Then
        # this subarray will either be array[i] itself or sub_A[i-1]+array[i]
        if right_sum + array[i] >= array[i]:
            right_sum += array[i]
        else:
            right_sum = array[i]
            right_start = i

        # If the sum of sub_A[i] is greater than the current maximum subarray.
        # We let current maximum subarray = sub_A[i]
        if right_sum > max_sum:
            max_start = right_start
            max_end = i
            max_sum = right_sum

    return [max_start,max_end,max_sum]

# One test case
array = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
print find_max_subarray(array)