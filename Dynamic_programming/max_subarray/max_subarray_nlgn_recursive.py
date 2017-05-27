#############################################################
# By Qi Song
# 05/25/17
#############################################################

#------------------------------------------------------------
# This is the function for finding the maximum subarray
# crossing the mid point
def find_max_crossing_subarray(array,left,right,mid):

    # Initialize the
    max_left_sum = -float('Inf')
    max_right_sum = -float('Inf')
    left_sum = right_sum = 0
    max_left_pos = left
    max_right_pos = right

    # Find the maximum contiguous array starting
    # from the mid point to left most point
    for i in range(mid,left-1,-1):
        left_sum += array[i]
        if left_sum > max_left_sum:
            max_left_sum = left_sum
            max_left_pos = i

    # Find the maximum contiguous array starting
    # from the mid point to right most point
    for j in range(mid+1,right+1):
        right_sum += array[j]
        if right_sum > max_right_sum:
            max_right_sum = right_sum
            max_right_pos = j

    return [max_left_pos,max_right_pos,max_left_sum+max_right_sum]

#------------------------------------------------------------------
# Function for recursively finding the max subarray
def find_max_subarray_recursive(array,left,right):

    if left == right:
        return [left,right,array[left]] # This is the base case. When subarray only contains one element
    else:

        # When divide the array into two parts. We need to handle the case of odd length and even length
        if (right-left+1)%2 == 1:
            mid = (left+right)/2
        else:
            mid = (left+right-1)/2

        # Divide the array into left and right parts. Then recursively find the max subarray in the left
        # part, the right part. The max subarray crossing the mid point is found by the function
        # find_max_crossing_subarray(). This gives three maximal subarrays. Compare the three subarrays and
        # find the maximum one among the three.
        (low_left,high_left,max_left) = find_max_subarray_recursive(array,left,mid)
        (low_right,high_right,max_right) = find_max_subarray_recursive(array,mid+1,right)
        (low_cross,high_cross,max_cross) = find_max_crossing_subarray(array,left,right,mid)

        max_values = [max_left,max_right,max_cross]
        low_values = [low_left,low_right,low_cross]
        high_values = [high_left,high_right,high_cross]

        idx = max_values.index(max(max_values))

        return[low_values[idx],high_values[idx],max_values[idx]]

#---------------------------------------------------------------------
# A wrapper function
def find_max_subarray_dp(array):
    return find_max_subarray_recursive(array,0,len(array)-1)

# One test case copied from CLRS book, Chapter 4
array = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
print find_max_subarray_dp(array)
