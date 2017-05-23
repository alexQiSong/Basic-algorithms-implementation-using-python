#############################################################
# By Qi Song
# 05/23/17
#############################################################

# Function for merging two sorted arrays into
# one sorted array
def merge(seq,start,mid,end):

    left = seq[start:(mid+1)]+[float('Inf')]
    right = seq[(mid+1):(end+1)]+[float('Inf')]

    for i in range(start,end+1):
        if left[0] <= right[0]:
            seq[i] = left.pop(0)
        else:
            seq[i] = right.pop(0)

# Function for recursively implementing the merge sort
# algorithm.
def recursive_merge_sort(seq,start,end):

    # The length of array to be applied the recursive
    # merge sort to
    seq_len = end-start+1

    # Deal with odd length and even length separately
    # The mid point for odd length array is start+sequence_length/2 -1
    # And the mid point for even length array is start+sequence_length/2
    if seq_len % 2 == 0:
        mid = start+seq_len/2 - 1
    elif seq_len == 1:
        return
    else:
        mid = start+seq_len/2

    # Break down the sequence to two subsequences. Once the subseqeunces
    # are all sorted, merge them into one sorted sequence
    recursive_merge_sort(seq,start,mid)
    recursive_merge_sort(seq,mid+1,end)
    merge(seq,start,mid,end)

# Wrapper function
def merge_sort(seq):
    recursive_merge_sort(seq,0,len(seq)-1)
    return seq

# One test case
seq = [11,10,4,5,6,2,3,12,111,109,2,3,0,7,20]
print merge_sort(seq)