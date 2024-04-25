#!/usr/bin/bash

PDB_DIR=~/Documents/CX4803project

# Output directory for images
IMG_DIR=~/Documents/CX4803project/images

# Create the image directory if it doesn't exist
mkdir -p $IMG_DIR

# Loop through all .pdb files in the directory
for pdb_file in $PDB_DIR/*.pdb
do
    # Extract the base name for the PDB file
    base_name=$(basename $pdb_file .pdb)

    # Start PyMOL in command mode
    pymol -c -d "\
    load $pdb_file, myProtein; \
    rotate x, 90; png $IMG_DIR/${base_name}_front.png; \
    rotate x, -180; png $IMG_DIR/${base_name}_back.png; \
    rotate x, 90; rotate y, 90; png $IMG_DIR/${base_name}_left.png; \
    rotate y, -180; png $IMG_DIR/${base_name}_right.png; \
    rotate y, 90; rotate z, 90; png $IMG_DIR/${base_name}_top.png; \
    rotate z, -180; png $IMG_DIR/${base_name}_bottom.png; \
    delete all;"
done