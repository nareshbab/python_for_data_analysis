import pandas as pd
import matplotlib.pyplot as plt
import json
from collections import defaultdict, Counter
from pandas import DataFrame, Series
import numpy as np


path = "pydata-book/ch02/usagov_bitly_data2012-03-16-1331923249.txt"
# file = open(path, "r")
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
frame = DataFrame(records)

tz_counts = frame['tz'].value_counts()
print tz_counts[:10]

# filling the missing data
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unkown'
tz_counts = clean_tz.value_counts()

print type(tz_counts[:10])
# plt.interactive(False)

tz_counts[:10].plot(kind="barh", rot=1)
# plt.show()
# list columns of data frame
print frame.columns.values
print frame.a
results = Series([x.split()[0] for x in frame.a.dropna()])
print results[:5]

# filter not null on column a
cframe = frame[frame.a.notnull()]
print cframe.columns.values
operating_system = Series(np.where(cframe.a.str.contains("Windows"), "Windows", "Not Windows"))
by_tz_os = cframe.groupby(['tz', operating_system])
agg_counts = by_tz_os.size().unstack().fillna(0)
indexer = agg_counts.sum(1).argsort()
count_subset = agg_counts.take(indexer)[-10:]
count_subset.plot(kind="barh", stacked=True)
# plt.show()
normed_subset = count_subset.div(count_subset.sum(1), axis=0)
normed_subset.plot(kind="barh", stacked=True)
plt.show()