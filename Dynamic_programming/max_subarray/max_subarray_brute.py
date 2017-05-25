# This function is for finding the maximum subarray using brute force method
def max_subarray_brute(array):

    # Initialize the left,right position and the maxmimum sum value
    max_left = max_right = 0
    max_sum = -float('Inf')

    for i in range(len(array)):
        for j in range(i,len(array)):
            cur_sum = sum(array[i:j+1])

            # Update the subarray position and current maximum sum value
            # for the subarray
            if cur_sum > max_sum:
                max_sum = cur_sum
                max_left = i
                max_right = j

    return [max_left,max_right,max_sum]

# One test case
array = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
print max_subarray_brute(array)