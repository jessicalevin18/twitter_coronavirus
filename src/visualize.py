#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path', required=True, nargs='+')
parser.add_argument('--key', required=True, nargs='+')
parser.add_argument('--percent', action='store_true')
parser.add_argument('--title')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter, defaultdict
import matplotlib.pyplot as plt

# Iterate over each input path and key
for input_path in args.input_path:
    for key in args.key:
        # open the input path
        with open(input_path) as f:
            counts = json.load(f)

        # normalize the counts by the total values
        if args.percent:
            for k, v in counts.items():
                if k != '_all':
                    for k_in_v, val in v.items():
                        v[k_in_v] /= counts['_all'][k_in_v]

        # print the count values
        if key in counts:
            items = sorted(counts[key].items(), key=lambda item: item[1], reverse=False)
        else:
            print(f"Key '{key}' not found in {input_path}")
            continue

        # Get the top 10 keys
        top_10_items = items[-10:]

        # Create a bar graph
        plt.bar([k for k, v in top_10_items], [v for k, v in top_10_items])
        plt.xlabel('Keys')
        plt.ylabel('Values')
        #  plt.title(f'Top 10 {key} Results for {input_path}')
        if 'country' in input_path:
            plt.xlabel('Countries')
            plt.ylabel('Values')
            plt.title(f'Counts of Tweets with {key} by Top 10 Countries')
        elif 'lang' in input_path:
            plt.xlabel('Languages')
            plt.ylabel('Values')
            plt.title(f'Counts of Tweets with {key} by Top 10 Languages')
        else:
            plt.xlabel('Keys')
            plt.ylabel('Values')
            plt.title(f'Counts of {key}')
        plt.xticks(rotation=90)

        # Save the graph as a png file
        output_filename = f'{key}_{os.path.basename(input_path).split("_")[0]}.png'
        plt.tight_layout()
        plt.savefig(output_filename)

        # Show the graph
        plt.show()

        # Clear the figure
        plt.clf()

        # print the count values
        for k, v in top_10_items:
            print(k, ':', v)             
