#!/usr/bin/env python3

import argparse
import os
import json
from collections import defaultdict
import matplotlib.pyplot as plt
import sys
import datetime

# Command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--input_path', required=True)
parser.add_argument('--output_path', required=True)
parser.add_argument('--hashtags', nargs='+', required=True)
parser.add_argument('--plot_output', required=True)
args = parser.parse_args()

# Initialize a dictionary to store the hashtags for each date
hashtags_per_date = defaultdict(lambda: defaultdict(int))

# Find all input files in the input path
for filename in os.listdir(args.input_path):
    if filename.startswith('geoTwitter') and filename.endswith('.zip.lang'):
        # Load the file
        path = os.path.join(args.input_path, filename)

        # Check if the filename contains 'geoTwitter'
        parts = filename.split('geoTwitter')
        if len(parts) < 2:
            print(f"Skipping {filename} because it does not contain 'geoTwitter'")
            continue

        # Extract the date
        date = parts[1].split('.zip.lang')[0]

        # Load the file
        with open(path) as f:
            data = json.load(f)

        # Remove language information and count hashtags
        for hashtag in data:
            if hashtag != '_all':
                for lang in data[hashtag]:
                    hashtags_per_date[date][hashtag] += data[hashtag][lang]

# Write the output path
with open(args.output_path, 'w') as f:
    f.write(json.dumps(dict(hashtags_per_date)))

# Create a dictionary to store the hashtag counts per day of the year
hashtag_counts = defaultdict(lambda: defaultdict(int))

# Populate the hashtag_counts dictionary
for date, hashtags in hashtags_per_date.items():
    date_parts = date.split('-')
    day_of_year = datetime.date(int(date_parts[0]), int(date_parts[1]), int(date_parts[2])).timetuple().tm_yday
    for hashtag, count in hashtags.items():
        hashtag_counts[hashtag][day_of_year] = count

# Create the line plot
plt.figure(figsize=(10, 6))
for hashtag in args.hashtags:
    x = sorted(hashtag_counts[hashtag].keys())
    y = [hashtag_counts[hashtag][day] for day in x]
    plt.plot(x, y, label=hashtag)

plt.xlabel('Day of the Year')
plt.ylabel('Number of Tweets')
plt.title('Hashtag Counts During 2020')
plt.legend()
plt.xticks(range(1, 366, 30))  # Set x-axis tick labels to every 30 days
plt.savefig(args.plot_output)
