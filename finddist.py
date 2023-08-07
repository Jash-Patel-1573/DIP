#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 11:35:20 2023

@author: bmiit202006100110116
"""

# import required libraries
import math
import os

x1 = int(input("enter x1 value :"))
x2 = int(input("enter x2 value :"))
y1 = int(input("enter y1 value :"))
y2 = int(input("enter y2 value :"))


# 0,367  0,405

De =int (math.sqrt((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2)))

D4 =int (abs(x1 - x2) + abs( y1 - y2 ))

D8 = int (max(abs( x1 - x2 ),abs( y1 - y2 )))


print(De)
print(D4)
print(D8)
