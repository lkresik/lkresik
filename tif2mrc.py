#!/bin/bash

# Loop through all .tif files in the current directory
for file in *.tif; do
    # Extract filename without extensiont		
    filename=$(basename -- "$file" .tif)
    # Run tif2mrc command to convert .tif to .mrc
    tif2mrc "$file" "${filename}.mrc"
done

#Run from the folder with TIFs: bash tif2mrc.sh
