#!/usr/bin/python3
""" Test function find_peak """
def find_peak(list_of_integers):
    y=0
    i=0
    s = 0
    arr = list_of_integers
    for y in range(len(arr)):
        for i in range(len(arr) -1):
            if arr[i] <= arr[i+1]:
                s = arr[i]
                arr[i] = arr[i+1]
                arr[i+1]=s
    print(arr[0])
