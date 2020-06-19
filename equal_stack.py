#!/bin/python

from __future__ import print_function

import os
import sys

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        self.stack.pop()
    
    def display(self):
        for i in self.stack: print(i)

    def sum_stack(self):
        return sum(self.stack)

    def reverse(self):
        self.stack = self.stack[::-1]

#  
# Complete the equalStacks function below.
#

def poper(mini, list_of_nums, diff):
    if mini == sum(list_of_nums):
        return list_of_nums
    else:
        if diff <= list_of_nums[0]:
            list_of_nums.pop(0)
            return list_of_nums
        else:
            popel = 0
            while (diff >= popel):
                popel +=list_of_nums.pop(0)
            return list_of_nums

def equalStacks(h1, h2, h3):
    #
    # Write your code here.
    #
    h1_sum = sum(h1)
    h2_sum = sum(h2)
    h3_sum = sum(h3)    
    
    while(h1_sum!=h2_sum and h1_sum!=h3_sum):
        mini = min(h1_sum, h2_sum, h3_sum)
        maxi = max(h1_sum, h2_sum, h3_sum)
        diff= maxi - mini
        h1 = poper(mini, h1, diff)
        h2 = poper(mini, h2, diff)
        h3 = poper(mini, h3, diff)
        h1_sum = sum(h1)
        h2_sum = sum(h2)
        h3_sum = sum(h3)
    
    return sum(h1)

if __name__ == '__main__':
    n1N2N3 = raw_input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = map(int, raw_input().rstrip().split())

    h2 = map(int, raw_input().rstrip().split())

    h3 = map(int, raw_input().rstrip().split())

    result = equalStacks(h1, h2, h3)

    print(result)