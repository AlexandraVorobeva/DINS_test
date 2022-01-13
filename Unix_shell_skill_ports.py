#!/usr/bin/env python3

from collections import Counter

all_dpt = []

with open('ubuntu-s-1vcpu-1gb-dbl1-01.ufw.log') as file:
    for line in file:
        line = line.strip().split()
        dpt = line[20]
        all_dpt.append(dpt[4:])
most_common_dpt_host = Counter(all_dpt).most_common(20)
for dpt in most_common_dpt_host:
    print(dpt[0])