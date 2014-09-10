import os
from os import sys
import json

if len(sys.argv) < 3:
    print "e.g. $ python grand_sum [summary_folder] [output_file_name]"
    sys.exit(0)

summary_folder = sys.argv[1]
output_file_name = sys.argv[2]
summary = {}
for path in os.listdir(summary_folder):
    path_summary = json.load(open(os.path.join(summary_folder, path), "r"))
    if not len(summary):
        summary = path_summary
    else:
        summary = dict(summary.items() + path_summary.items())
json.dump(summary, open("grand_summary.json", "w"))
