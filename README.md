Quick sort uses a similar strategy to binary search. It divides the array in half, ultimately shortening the runtime to n*logn (on average).

In binary search, we pick a middle value and check if we want to continue searching higher or lower 
(because the array is already sorted), but we can't quite do that with an unsorted list. 

Instead, we can pick a number at "random" and sort the array into values higher and lower than the number we picked. 
This way we're still breaking the problem down into two "halves" (even though we aren't explicitly picking the middle point)
and we can continue breaking them down, similar to how you do so in binary search.

The number we pick is called the "pivot" since you pivot the other numbers around this value. 
We then have two "halves" that we can call quickSort() on again (recursion!).

**Note**: <br />
As we recursively call quickSort, the same array is being used/sorted with each call. 
We aren't building the same kind of stack of calls as you would a recursive factorial algorithm.



We have an approach, so how do we implement it?
- We have to define a base case and a recursive case.
  - We're dealing with an array, so the base case is probably going to be a length of 0 or 1.
  - In the recursive case we want to call quickSort on the two halves we create.
- And we also need to pick a pivot and sort the array by values lower and higher than the pivot.

Doing all of that in quickSort here would packing in too much into this, so lets keep our function clean and just have it handle the recursion aspect. 

We then end up with something like this:

```diff
def quickSort(arr, low_index, high_index):
#   base case
    if len(arr) == 1: 
        return arr

#   recursive case
    if low_index < high_index:  
        part_index = partition(arr, low_index, high_index)
        quickSort(arr, low_index, part_index-1)
        quickSort(arr, part_index+1, high_index)
```
With that in place, what does the partition function have to do?

1) As we mentioned earlier, the partition has to rearrange the array so that everything to the left of the pivot is less than it, and everything to the right of the pivot is greater than the pivot.
    - If that is accomplished, that also means the pivot will end up in its final correct position
2) We need to return the position of the pivot so we can recursively quick sort the resulting "halves"


And how do we implement that?

To accomplish these goals, we need to do the following:
  - We have to select a "random" pivot.
  - We have to iterate over the array and compare each value to the pivot (and move any values that are higher/lower and on the "wrong" side of the pivot value to the correct side).
  - As we progress through the iteration, we have to keep track of if a particular index is "high" or "low" so we can swap it (and move lower values to the front).

 
```diff
def partition(arr, low_index, high_index):
#   if our pivot turns out to be the lowest value in the array, we   
#   will simply move it to position 0 at the end of the iteration.
    i = low_index  
#   "randomly" choose the last number as the pivot 
    pivot = arr[high_index] 
  
#   as we traverse the array, if a value is less than the pivot, we
#   want to move it to the left side of the array (we'll move the pivot
#   to its correct position at the end, after we know how many values
#   are less than it). 
#   we keep track of where the "low" side of the array ends with the
#   variable "i", which gets updated only when the current value
#   is less than the pivot (see below). The inverse case of this is
#   "i" DOES NOT get updated when the current iteration is greater 
#   than the pivot. So, when "j" is greater than the pivot, we just
#   continue until we find a value smaller than the pivot that needs to
#   be moved back to the "i" position, at the end of the "low" section.
#                  [i]                       [j]-->
#   [lower-than-pivot], [higher-than-pivot], [unsorted], [pivot] 
    for j in range(low_index, high_index): 
        if arr[j] <= pivot: 
            arr[i], arr[j] = arr[j], arr[i] 
            i += 1


#   after we've iterated through the array, we finally swap the pivot we 
#   initially chose with the index position that is just to
#   the right of the "low" partition of the pivot, resulting in
#   something like this:
#     [lower-than-the-pivot], [pivot], [higher-than-the-pivot]
     arr[i], arr[high_index] = arr[high_index], arr[i]
     return i
```

To review...

- We want to sort something and use a "binary" approach to achieve a better runtime.
- We decide to choose a pivot that will (hopefully/approximately) 'halve' the array.
- We write the quickSort function, which takes an array, 'min', and 'max', and define the base case and recursive case.
- In the recursive case, we need to rearrange the array around the pivot. After doing so, we're able to recursively call quickSort on the two 'halves' of the array and sort those segments.

The partition function responsible for rearranging the array picks an arbitrary pivot value 
(we pick the last value for simplicity sake since we'll be looping over the array and don't 
want to be moving it around as we iterate) and initializes a "bookmark" variable to track 
of where the "less-than-pivot" segment ends.

As we then iterate over the array, we compare the indices to the pivot and move any values 
less than the pivot to the left (swapping them with values larger than the pivot).

After we're done with the for loop, the bookmark variable is at the position just to the 
right of the last value that was less than the array ([less-than-pivot][pivot][…]), so 
we swap the pivot value with the value at that index (which is a value larger than the pivot)
and return the index of the pivot, which is now in its final position.

 

The recursion then takes over with the smaller segments and sorts the rest of the array!
