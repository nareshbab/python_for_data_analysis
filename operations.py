import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
from collections import defaultdict, Counter


path = "/Users/naresh/workspace/pydata-book/ch02/usagov_bitly_data2012-03-16-1331923249.txt"
file = open(path, "r")
records = [json.loads(line) for line in open(path)]
print records[0]
print records[0]['t']
print records[0]['tz']

time_zones = [rec['tz'] for rec in records if 'tz' in rec]
print time_zones


def get_counts(sequence):
    count = {}
    for x in sequence:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
    return count


def get_counts2(sequence):
    count = defaultdict(int)
    for x in sequence:
        count[x] += 1
    return count


print get_counts(time_zones)
print get_counts2(time_zones)
counts = get_counts2(time_zones)
print counts['America/New_York']
print len(time_zones)


def top_counts(count_dict, size):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-size:]


top_tzs = top_counts(counts, 10)
print type(top_tzs)

# same can be achieved with counter from collections
counter = Counter(time_zones)
print counter.most_common(10)

# achieving same with pandas
from pandas import DataFrame, Series
frame = DataFrame(records)
print frame.head(10)
