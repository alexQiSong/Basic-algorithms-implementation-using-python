#############################################################
# By Qi Song
# 05/27/17
#############################################################
# Max heap is represented by a tree structure, where all the children
# nodes are smaller than their parents. The max heap tree is also
# a complete binary tree. Therefore, we can store the max heap
# in an array. In python, because array index starts with
# 0, the left child and right child of array[i] will be array[2*i+1]
# and array [2*i+2]

# -------------------------------------------------------------------
# Function for 'floating down' the value in the max heap. This
# assumes that the left and right subtrees are already the max heaps
#-------------------------------------------------------------------
def max_heapify(array,i):
    largest = i
    while 1:

        # Compare parent to left child and get the current largest
        if 2*i+1 <= len(array)-1 and array[2*i+1] >= array[i]:
            largest = 2*i+1

        # Compare the current largest to right child
        if 2*i+2 <= len(array)-1 and array[2*i+2] >= array[largest]:
            largest = 2*i+2

        # Exchange the current largest with the parent
        if largest != i:
            array[i],array[largest] = array[largest],array[i]
            i = largest
        else:
            break

#-----------------------------------------------------------------
# Function for building a max heap
#-----------------------------------------------------------------
def build_max_heap(array):
    if len(array)-1 % 2 == 1:
        last_parent_index = (len(array)-2)/2
    else:
        last_parent_index = (len(array)-1)/2-1

    for i in range(last_parent_index,-1,-1):
        max_heapify(array,i)

    return array

#-----------------------------------------------------------------
# Heap sort main function
#-----------------------------------------------------------------
def heap_sort(array):

    # Build the max heap first
    result = []
    build_max_heap(array)
    print array

    # Every time we get the largest value from the root. After we
    # exchange the root node with the last element of array, we
    # execute max_heapify() to ensure that the new tree still meets
    # the requirement of max heap
    while len(array)-1 > 0:
        array[0],array[-1] = array[-1],array[0]
        result.insert(0,array[-1])
        array.pop(-1)
        max_heapify(array,0)

    return result

# One test case
array = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
print heap_sort(array)