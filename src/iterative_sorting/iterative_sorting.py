# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    current_index = 0
    while current_index < len(arr)-1:
        smallest_index = current_index
        for i in range(current_index+1, len(arr)):
            if arr[i] < arr[smallest_index]:
                smallest_index = i
        if smallest_index != current_index:
            arr[current_index], arr[smallest_index] = arr[smallest_index], arr[current_index]
        current_index += 1

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    done = False
    while not done:
        swaps = 0
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaps += 1
        done = swaps == 0

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
# index start at 0 so i need + 1 length so counts[maximum] is a valid index

# time complexity is O(n + m) where n is number of items in arr and 
# m is maximum value
# space complexity is O(m) where m is maximum since we make new list of
# m items

def counting_sort(arr, maximum=None):
    if maximum is None:
        return []

    counts = [0] * (maximum + 1)
    for num in arr:
        counts[num] += 1
    
    ret_arr = []
    for i in range(0, len(counts)):
        if counts[i] > 0:
            nums = [i] * counts[i]
            ret_arr += nums

    return ret_arr