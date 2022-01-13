#!/usr/bin/env python3

from collections import Counter

APR_6_7_src = []

with open('ubuntu-s-1vcpu-1gb-dbl1-01.ufw.log') as file:
    for line in file:
        line = line.strip().split()
        if line[0] == 'Apr' and ((line[1] == '6' and line[2] >= '09:00:00') or
                                 (line[1] == '7' and line[2] < '09:00:00')):
            src = line[11]
            APR_6_7_src.append(src[4:])
most_common_src_host = Counter(APR_6_7_src).most_common(20)
for src in most_common_src_host:
    print(src[0])
