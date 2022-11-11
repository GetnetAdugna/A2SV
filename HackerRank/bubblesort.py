#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    counter=0
    
    for  j in range(len(a)):
        i=0
        while(i<len(a)):
            flag=0
            if i==0:
                pass
            elif(a[i]<a[i-1]):
                flag=1
                temp=a[i-1]
                a[i-1]=a[i]
                a[i]=temp
            if (flag==1):
             counter+=1
            i+=1
    print(f"Array is sorted in {counter} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
    
#     Array is sorted in 3 swaps.
# First Element: 1
# Last Element: 3
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
