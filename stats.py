#usr/bin/env python3

#import packages
import pandas as pd
import statistics
from statistics import mean
from statistics import median
import argparse
import re

#load in the data
dbd = pd.read_csv("dbd_scores.csv")
full = pd.read_csv("full_alignment_scores.csv")

#to int
dbd_nums = []
full_nums = []
for pos in dbd:
	dbd_num = re.findall("\d+", pos)
	dbd_nums.append(dbd_num)
for pos in full:
	full_num = re.findall("\d+", pos)
	full_nums.append(full_num)

print(dbd_nums)
print(full_nums)

#stats
dbd_mean = mean(dbd)
full_mean = mean(full)
print(dbd_mean, full_mean)

dbd_median = median(dbd)
full_median = median(full)
print(dbd_median, full_median)

#histograms

#box and whisker


