#############################################################
# By Qi Song
# 05/26/17
#############################################################
def find_max_subarray_recursive(array,pos):
    if pos == 0:
        return [0,0,0,0,0]
    else:
        start_max,end_max,start_right,sum_left,sum_right = find_max_subarray_recursive(array,pos-1)

        if sum_right+array[pos] >= array[pos]:
            sum_right += array[pos]
        else:
            sum_right = array[pos]
            start_right = pos

        if sum_left >= sum_right:
            return [start_max,end_max,start_right,sum_left,sum_right]
        else:
            return [start_right,pos,start_right,sum_right,sum_right]

# One test case
array = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
print find_max_subarray_recursive(array,len(array)-1)