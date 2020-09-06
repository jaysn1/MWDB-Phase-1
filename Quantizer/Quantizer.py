# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 22:35:29 2020

@author: Jaysn
"""
import math
from scipy.integrate import quad

MEAN = 0
SD = 0.25
PI = math.pi 

def guassian(x):
    a = 1/ (SD * math.sqrt(2*PI))
    e = (-1 * math.pow((x - MEAN),2)) / (2 * math.pow(SD, 2))
    return a * math.exp(e)

def calculate_lengths(resolution):
    lengths = []
    ranges_starts = [-1]
    for i in range(1, (2 * resolution) + 1):
        lower_limit = (i - resolution - 1) / resolution
        upper_limit = (i - resolution) / resolution
        numerator = quad(guassian, lower_limit, upper_limit)[0]
        denominator = quad(guassian, -1, 1)[0]
        length = (2 * numerator) / denominator
        lengths.append(length)
        ranges_starts.append(ranges_starts[-1] + length)
    print(ranges_starts)
    return lengths

