#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    aver=0
    sum=0
    bill.remove(bill[k])
    for i in bill:
        sum+=i
    aver=int(sum/2)
    if aver==b:
        print("Bon Appetit")
    elif aver<b:
        print(b-aver)
    else:
        print(aver-b)
    
    # Write your code here

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
