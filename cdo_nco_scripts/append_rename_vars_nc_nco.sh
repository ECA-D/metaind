#!/bin/bash

# Executable bash script

# Location: /usr/people/stepanov/sh_scripts
# Name:     append_rename_vars_nc_nco.sh
  
# Append variables to icclim calculated indices files using NCO. Vars are:
# rlon, then renamed as x
# rlat, then renamed as y
# rotated_pole

# ==========================================
# Author: I.Stepanov (igor.stepanov@knmi.nl)
# 15.06.2016 @KNMI
# ============================================================================================
# Updates list
# 
# 23.06.2016. I.S. Added short handles to path and source.target files

# ============================================================================================


# Some paths and var names
# ---------------------------------------------------------------

# Path to source file containing rlat,rlon on EUR-44 grid/ensemble
# Early mistake was using RCM for rlat,rlon resulting in rotated map on climate4impact visualization

#file_with_rlon_rlat='/nobackup/users/stepanov/CLIPC/Model_data/pr/rcp45/50km/daily/SMHI_DBS43_2006_2100/prAdjust_EUR-44_NOAA-GFDL-GFDL-ESM2M_rcp45_r1i1p1_SMHI-RCA4_v1-SMHI-DBS43-EOBS10-1981-2010_day_19510101-19551231.nc'
file_with_rlon_rlat='/nobackup/users/stepanov/icclim_indices_DRS_conventions/RCM/pr/50km/PRCPTOT_icclim_NOAA-GFDL-GFDL-ESM2M_rcp45_r1i1p1_SMHI-RCA4_v1-SMHI-DBS43-EOBS10-1981-2010_EUR-44_1970_2005--1980-2010.nc'

# Path to target file
path_ensMultiModel='/nobackup/users/stepanov/icclim_indices_DRS_conventions/RCM/pr/50km/ensMulti-model/coordinates_appended/'


# # PRCPTOT

# # Indice in file (for adding global attribute to it)
# indice='PRCPTOT'
# # ---------------------------------------------------------------

# for file_ensMultiModel in PRCPTOT_ens-multiModel-20perc_icclim-4-1-0_KNMI_RCP45_r1i1p1_EUR-44_yr_19700101-20051231.nc \
# 					      PRCPTOT_ens-multiModel-20perc_icclim-4-1-0_KNMI_RCP45_r1i1p1_EUR-44_yr_20060101-20991231.nc \
# 					      PRCPTOT_ens-multiModel-80perc_icclim-4-1-0_KNMI_RCP45_r1i1p1_EUR-44_yr_19700101-20051231.nc \
# 					      PRCPTOT_ens-multiModel-80perc_icclim-4-1-0_KNMI_RCP45_r1i1p1_EUR-44_yr_20060101-20991231.nc \
# 						  PRCPTOT_ens-multiModel-mean_icclim-4-1-0_KNMI_RCP45_r1i1p1_EUR-44_yr_19700101-20051231.nc \
# 						  PRCPTOT_ens-multiModel-mean_icclim-4-1-0_KNMI_RCP45_r1i1p1_EUR-44_yr_20060101-20991231.nc \
# 						  PRCPTOT_ens-multiModel-median_icclim-4-1-0_KNMI_RCP45_r1i1p1_EUR-44_yr_19700101-20051231.nc \
# 						  PRCPTOT_ens-multiModel-median_icclim-4-1-0_KNMI_RCP45_r1i1p1_EUR-44_yr_20060101-20991231.nc

# # RX1day

# # Indice in file (for adding global attribute to it)
# indice='RX1day'
# # ---------------------------------------------------------------


# for file_ensMultiModel in RX1day_ens-multiModel-20perc_icclim-4-1-0_KNMI_RCP45_r1i1p1_EUR-44_yr_19700101-20051231.nc \
# 						  RX1day_ens-multiModel-20perc_icclim-4-1-0_KNMI_RCP45_r1i1p1_EUR-44_yr_20060101-20991231.nc \
# 			        	  RX1day_ens-multiModel-80perc_icclim-4-1-0_KNMI_RCP45_r1i1p1_EUR-44_yr_19700101-20051231.nc \
# 						  RX1day_ens-multiModel-80perc_icclim-4-1-0_KNMI_RCP45_r1i1p1_EUR-44_yr_20060101-20991231.nc \
# 						  RX1day_ens-multiModel-mean_icclim-4-1-0_KNMI_RCP45_r1i1p1_EUR-44_yr_19700101-20051231.nc \
# 						  RX1day_ens-multiModel-mean_icclim-4-1-0_KNMI_RCP45_r1i1p1_EUR-44_yr_20060101-20991231.nc \
# 						  RX1day_ens-multiModel-median_icclim-4-1-0_KNMI_RCP45_r1i1p1_EUR-44_yr_19700101-20051231.nc \
# 						  RX1day_ens-multiModel-median_icclim-4-1-0_KNMI_RCP45_r1i1p1_EUR-44_yr_20060101-20991231.nc

# # RR1

# # Indice in file (for adding global attribute to it)
# indice='RR1'
# # ---------------------------------------------------------------

# for file_ensMultiModel in RR1_ens-multiModel-20perc_icclim-4-1-0_KNMI_RCP45_r1i1p1_EUR-44_yr_19700101-20051231.nc \
# 						  RR1_ens-multiModel-20perc_icclim-4-1-0_KNMI_RCP45_r1i1p1_EUR-44_yr_20060101-20991231.nc \
# 						  RR1_ens-multiModel-80perc_icclim-4-1-0_KNMI_RCP45_r1i1p1_EUR-44_yr_19700101-20051231.nc \
# 					 	  RR1_ens-multiModel-80perc_icclim-4-1-0_KNMI_RCP45_r1i1p1_EUR-44_yr_20060101-20991231.nc \
# 						  RR1_ens-multiModel-mean_icclim-4-1-0_KNMI_RCP45_r1i1p1_EUR-44_yr_19700101-20051231.nc \
# 						  RR1_ens-multiModel-mean_icclim-4-1-0_KNMI_RCP45_r1i1p1_EUR-44_yr_20060101-20991231.nc \
# 						  RR1_ens-multiModel-median_icclim-4-1-0_KNMI_RCP45_r1i1p1_EUR-44_yr_19700101-20051231.nc \
# 						  RR1_ens-multiModel-median_icclim-4-1-0_KNMI_RCP45_r1i1p1_EUR-44_yr_20060101-20991231.nc

# R95p

# Indice in file (for adding global attribute to it)
indice='R95p'
# ---------------------------------------------------------------

for file_ensMultiModel in R95p_ens-multiModel-20perc_icclim-4-1-0_KNMI_RCP45_r1i1p1_EUR-44_yr_19700101-20051231_1980-2010.nc \
						  R95p_ens-multiModel-20perc_icclim-4-1-0_KNMI_RCP45_r1i1p1_EUR-44_yr_20060101-20991231_1980-2010.nc \
						  R95p_ens-multiModel-80perc_icclim-4-1-0_KNMI_RCP45_r1i1p1_EUR-44_yr_19700101-20051231_1980-2010.nc \
						  R95p_ens-multiModel-80perc_icclim-4-1-0_KNMI_RCP45_r1i1p1_EUR-44_yr_20060101-20991231_1980-2010.nc \
						  R95p_ens-multiModel-mean_icclim-4-1-0_KNMI_RCP45_r1i1p1_EUR-44_yr_19700101-20051231_1980-2010.nc \
						  R95p_ens-multiModel-mean_icclim-4-1-0_KNMI_RCP45_r1i1p1_EUR-44_yr_20060101-20991231_1980-2010.nc \
						  R95p_ens-multiModel-median_icclim-4-1-0_KNMI_RCP45_r1i1p1_EUR-44_yr_19700101-20051231_1980-2010.nc \
						  R95p_ens-multiModel-median_icclim-4-1-0_KNMI_RCP45_r1i1p1_EUR-44_yr_20060101-20991231_1980-2010.nc



do


	echo "-----"
	echo "Modifying file $file_ensMultiModel"
	echo "-----"
	echo

	# This gets the selected 2 variables appended
	# ---------------------------------------------------------------

	# Now with handles
	ncks -A -v rlat,rlon,rotated_pole $(echo ${file_with_rlon_rlat}) $(echo ${path_ensMultiModel})/$(echo ${file_ensMultiModel})


	# Here a midstep is needed to rename rlon,rlat-->x,y
	ncrename -v rlat,y $(echo ${path_ensMultiModel})/$(echo ${file_ensMultiModel})
	ncrename -v rlon,x $(echo ${path_ensMultiModel})/$(echo ${file_ensMultiModel})


	# Add attribute to the variable
	ncatted -O -h -a grid_mapping,$(echo ${indice}),c,c,"rotated_pole" $(echo ${path_ensMultiModel})/$(echo ${file_ensMultiModel})


done

