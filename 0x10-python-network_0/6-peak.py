#!/usr/bin/python3
""" Test function find_peak """
def find_peak(list_of_integers):
    
    arr = list_of_integers
    for y in range(len(arr)):
        for i in range(len(arr) -1):
            if arr[i] <= arr[i+1]:
                s = arr[i]
                arr[i] = arr[i+1]
                arr[i+1]=s
    try:
        return arr[0]
    except:
        return None
