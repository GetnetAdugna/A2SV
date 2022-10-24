#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    output=[]
    for elem in grades:
        if elem <38:
            output.append(elem)
        elif elem>=38:
            fiveMultipleNum=math.ceil(elem/5)*5
            if((fiveMultipleNum-elem)<3):
                output.append(fiveMultipleNum)
            else:
                output.append(elem)
    return output    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
