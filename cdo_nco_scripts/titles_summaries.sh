#!/bin/bash

# Executable bash script

# Import ensemble statistics and change title and summary global attributes accordingly
# to match the DRS standards v1.3

# Update list
#
# 09/08/2016 I.S. Created script
# -------------------------------------------------------------------------

# Define some pahts
# =========================================================================


### Precipitation

#
in_stat='20th percentile' 'median(50th percentile)' '80th percentile'
gcms=('CCCma-CanESM2' 'CNRM-CM5' 'CSIRO-Mk3-6-0' 'EC-EARTH' 'IPSL-CM5A-MR' 'MIROC5' 'HadGEM2-ES' 'MPI-ESM-LR' 'NorESM1-M' 'GFDL-ESM2M')
indices=('rx1day' 'r95p' 'r20mm' 'r1mm' 'r10mm' 'prcptot' 'cdd' 'cwd')


titles=("ensemble ${in_stat} of maximum one-day precipitation" \
	    "ensemble ${in_stat} very wet days" \
		"ensemble ${in_stat} of very heavy precipitation days" \
		"ensemble ${in_stat} of wet days" \
		"ensemble ${in_stat} of heavy precipitation days" \
		"ensemble ${in_stat} of total precipitation in wet days" \
		"ensemble ${in_stat} of consecutive dry days" \
		"ensemble ${in_stat} of consecutive wet days")

ncatted -O -a title,global,o,c,${titles} -h	${dir_in}${indices[k]}_${path_ic_inst}_${gcms[j]}_${exper[i]}_${path_real_bc}_${time_cov_start[i]}-${time_cov_end[i]}.nc
		
		
ncatted -O -a summary,global,o,c,"This is the ensemble ${in_stat} of ${indices}. The ensemble is constructed by the following models: ${gcms}. For the definition of ${indices} see ECA&D." -h	${dir_in}${indices[k]}_${path_ic_inst}_${gcms[j]}_${exper[i]}_${path_real_bc}_${time_cov_start[i]}-${time_cov_end[i]}.nc

	if [ "${indices[k]}" = "r95p" ]; then
		ncatted -O -a summary,global,o,c,"This is the ensemble ${in_stat} of r95p. The ensemble is constructed by the following models: ${gcms}. For the definition of r95p see ECA&D." -h	${dir_in}${indices[k]}_${path_ic_inst}_${gcms[j]}_${exper[i]}_${path_real_bc}_${time_cov_start[i]}-${time_cov_end[i]}.nc
	fi


### Tmax
titles=("ensemble ${in_stat} of icing days" \
		"ensemble ${in_stat} of summer days" \
		"ensemble ${in_stat} of mean of daily maximum temperature")
		
ncatted -O -a title,global,o,c,${titles} -h	${dir_in}${indices[k]}_${path_ic_inst}_${gcms[j]}_${exper[i]}_${path_real_bc}_${time_cov_start[i]}-${time_cov_end[i]}.nc
		
		
ncatted -O -a summary,global,o,c,"This is the ensemble ${in_stat} of ${indices}. The ensemble is constructed by the following models: ${gcms}. For the definition of ${indices} see ECA&D." -h	${dir_in}${indices[k]}_${path_ic_inst}_${gcms[j]}_${exper[i]}_${path_real_bc}_${time_cov_start[i]}-${time_cov_end[i]}.nc

	if [ "${indices[k]}" = "tx" ]; then
		ncatted -O -a summary,global,o,c,"This is the ensemble ${in_stat} of tx. The ensemble is constructed by the following models: ${gcms}. For the definition of tx see ECA&D." -h	${dir_in}${indices[k]}_${path_ic_inst}_${gcms[j]}_${exper[i]}_${path_real_bc}_${time_cov_start[i]}-${time_cov_end[i]}.nc
	fi

### Tmin
titles=("fd: ensemble ${in_stat} of frost days" \
		"tr: ensemble ${in_stat} of tropical nights" \
		"tn: ensemble ${in_stat} of mean of daily minimum temperature")

ncatted -O -a title,global,o,c,${titles} -h	${dir_in}${indices[k]}_${path_ic_inst}_${gcms[j]}_${exper[i]}_${path_real_bc}_${time_cov_start[i]}-${time_cov_end[i]}.nc
		
		
ncatted -O -a summary,global,o,c,"This is the ensemble ${in_stat} of ${indices}. The ensemble is constructed by the following models: ${gcms}. For the definition of ${indices} see ECA&D." -h	${dir_in}${indices[k]}_${path_ic_inst}_${gcms[j]}_${exper[i]}_${path_real_bc}_${time_cov_start[i]}-${time_cov_end[i]}.nc

	if [ "${indices[k]}" = "tn" ]; then
		ncatted -O -a summary,global,o,c,"This is the ensemble ${in_stat} of tn. The ensemble is constructed by the following models: ${gcms}. For the definition of tn see ECA&D." -h	${dir_in}${indices[k]}_${path_ic_inst}_${gcms[j]}_${exper[i]}_${path_real_bc}_${time_cov_start[i]}-${time_cov_end[i]}.nc
	fi

### Tas
titles=("hd17: ensemble ${in_stat} of heating degree days")
ncatted -O -a title,global,o,c,${titles} -h	${dir_in}${indices[k]}_${path_ic_inst}_${gcms[j]}_${exper[i]}_${path_real_bc}_${time_cov_start[i]}-${time_cov_end[i]}.nc
		
		
ncatted -O -a summary,global,o,c,"This is the ensemble ${in_stat} of hd17. The ensemble is constructed by the following models: ${gcms}. For the definition of hd17 see ECA&D." -h	${dir_in}${indices[k]}_${path_ic_inst}_${gcms[j]}_${exper[i]}_${path_real_bc}_${time_cov_start[i]}-${time_cov_end[i]}.nc

