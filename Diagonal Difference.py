#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    sum1 = 0
    sum2 = 0
    m = 0
    n = len(arr)-1
    a = 0
    b = 0 
    for i in range(len(arr)):
        sum1+=arr[a][b]
        sum2+=arr[m][n]
        a+=1
        b+=1
        m+=1
        n-=1
    return abs(sum1-sum2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
