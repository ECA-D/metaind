#!/bin/bash

# Executable bash script



# Loop adding the atts to all NC files !
# Credits to Maarten Plieger

# --------------------------------------------
#minx="21.917306" miny="-44.744855" maxx="72.635820" maxy="65.151456"/

for file in `find -name *.nc`; do
echo $file
ncatted -h -O -a geospatial_lat_max,global,o,f,65.151456 $file
ncatted -h -O -a geospatial_lat_min,global,o,f,-44.744855 $file
ncatted -h -O -a geospatial_lon_max,global,o,f,72.635820 $file
ncatted -h -O -a geospatial_lon_min,global,o,f,21.917306 $file
done


	done
# --------------------------------------------

