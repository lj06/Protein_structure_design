#!/usr/bin/env python3

import os
import re

# gdb的文件路径
folder_path = "./gdb/"

for filename in os.listdir(folder_path):
    # 路径
    filepath = os.path.join(folder_path, filename)
    
    # 提取UniProt
    match = re.search(r'AF-(.+?)-F1', filename)
    if match:
        new_filename = match.group(1)
        
        # 保留.pdb的后缀
        file_extension = os.path.splitext(filename)[1]
        new_filepath = os.path.join(folder_path, new_filename + file_extension)
        
        # 重命名文件
        os.rename(filepath, new_filepath)
        print(f"Renamed {filename} to {new_filename}")
    else:
        print(f"No match found in {filename}")
