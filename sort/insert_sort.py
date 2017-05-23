
# This function implements the insert sort algorithm
# by ascending order
def insert_sort(seq):

    for i in range(1,len(seq)):

        # Current value
        key = seq[i]

        # Loop over the seq from seq[0] to seq[i-1], find a position where
        # current value could be inserted
        for j in range(i):
            if seq[j] > key:
                del seq[i]

                # Note that current value could also be inserted before the first
                # element of seq
                if j is 0:
                    seq = [key]+seq
                else:
                    seq = seq[0:j]+[key]+seq[j:]
                break

    return seq

seq = [4,5,1,5,2,8,1,3,1,3,90,11]
print insert_sort(seq)