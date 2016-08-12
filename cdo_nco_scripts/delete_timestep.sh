#!/bin/bash

# Executable bash script

# Remove last day of indices files so that ensemble with HadGEM on EUR-44 and
# EUR-11 can be processed into means


# Define some pahts
# ------------------------
# According to variable: Precip/Temp/Tmax/Tmin
path_indices_pr='/nobackup/users/stepanov/icclim_indices_DRS_conventions/RCM/pr/ensMulti-model'
#path_indices_pr_nobias='/nobackup/users/stepanov/icclim_indices_DRS_conventions/RCM/pr_no_bias_corr/'
#path_indices_tasmax='/nobackup/users/stepanov/icclim_indices_DRS_conventions/RCM/tasmax/'
#path_indices_tasmin='/nobackup/users/stepanov/icclim_indices_DRS_conventions/RCM/tasmin/'


# Indice category
# -------------------
PR_indices="PRCPTOT" #R95p RR1 RX1day"    # Precipitation, both bias and non-bias corrected
TASMAX_indices="ID" #TX90p               # Maximum temperature
TASMIN_indices="FD"                     # Minimum temperature


# 4 Parameters to set!
# --------------------------------------------

# In paths
path_indices=$path_indices_pr
#path_indices=$path_indices_pr_nobias
#path_indices=$path_indices_tasmax
#path_indices=$path_indices_tasmin


# Input path domain
#path_domain='2deg'
path_domain='50km'
#path_domain='12km'


# Domain type [for output file]
#ensemble='EUR-2deg' # 200km
ensemble='EUR-44'  # EUR-44
#ensemble='EUR-11'  # EUR-11


for indice in $PR_indices
#for indice in $TASMAX_indices
#for indice in $TASMIN_indices

# No more parameters to set
# --------------------------------------------


# --------------------------------------------
# Actual calculation

	do
        
 		echo
 		echo "-----"
 		echo "Calculating means for indice $indice"
 		echo "-----"
 		echo
	    
		cd $path_indices/$path_domain

		echo Where am i now
		echo
		pwd

		# general 
        #cdo ensmean $indice_* $(echo ${indice})_ens-multiModel-mean_$(echo ${ensemble}).nc
        # only projections now(incl. HadGEM)
		cdo ensmean $indice_*2006* $(echo ${indice})_ens-multiModel-mean_$(echo ${ensemble})_2006-2100.nc
        # only historical now(incl. HadGEM)
        #cdo ensmean $indice_*2005* $(echo ${indice})_ens-multiModel-mean_$(echo ${ensemble}).nc

 		#cdo ensmean $(echo ${indice})_* $(echo ${indice})_ens-multiModel-mean_$(echo ${ensemble})_1970-2005.nc
		
 		echo
 		echo "-----"
 		echo "Done calculating means for indice $indice"
 		echo "-----"
 		echo
 		echo

	done
# --------------------------------------------

