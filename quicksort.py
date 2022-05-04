#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
quicksort.py : quick sort, also known as a partition sort, 
    which uses a "Divide and Conquer" approach.
Time complexity:
Worst: O(n**2)
Best: O(nlogn)
Space Complexity: O(n)
"""

__author__ = "John Jennings"

def quickSort(arr, low_index, high_index):
#   base case
    if len(arr) == 1: 
        return arr

#   recursive case
    if low_index < high_index:  
        part_index = partition(arr, low_index, high_index)
        quickSort(arr, low_index, part_index-1)
        quickSort(arr, part_index+1, high_index)

    return arr

def partition(arr, low_index, high_index):
    i = low_index  
    pivot = arr[high_index] 
  
    for j in range(low_index, high_index): 
        if arr[j] <= pivot: 
            arr[i], arr[j] = arr[j], arr[i] 
            i += 1

    arr[i], arr[high_index] = arr[high_index], arr[i]
    return i

print(quickSort([2,4,56,32,64,746,0], 0, 6))