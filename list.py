#!/usr/bin/env python3

import sys
import os

output_file_name = sys.argv[1]

def get_basenames(directory):
    basenames = []
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            basename, _ = os.path.splitext(filename)
            basenames.append(basename)
    return basenames

def save_to_txt(basenames, output_file):
    with open(output_file, 'w') as f:
        for basename in basenames:
            f.write(f"{basename}\n")

directory = "./data/"
output_file = output_file_name

basenames = get_basenames(directory)
save_to_txt(basenames, output_file)
