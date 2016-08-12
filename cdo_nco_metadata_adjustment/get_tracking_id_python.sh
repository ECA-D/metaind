#!/bin/bash

echo Hi!


# Import the old tracking id from the RCM file for period 19660101-19701231,
# as it is the first used file to create historical indices:
# (e.g. tasmin_EUR-44_IPSL-IPSL-CM5A-MR_historical_r1i1p1_SMHI-RCA4_v1_day_19660101-19701231.nc)

#track_GCM_indice=$(

python << END


import netCDF4
from netCDF4 import Dataset
import ctypes
import icclim
import datetime
import icclim.util.callback as callback
#cb = callback.defaultCallback
from nco import Nco
nco=Nco()


print
#print '<<Loaded python modules>>'
print

# =====================================================================================================
# Define some paths

experiment='rcp45'
#experiment='rcp85'

# RCM output data and output of calculated indices
nobackup='/nobackup/users/stepanov/'

# Precip (non-bas corrected)
in_path_RCM_pr_nbc_50km=nobackup+"CLIPC/Model_data/no_bias_corr/EUR-44/"+experiment+"/day/pr/SMHI/all_models/"
out_path_RCM_pr_nbc_50km=nobackup+"indices_tracking_id_test/EUR-44/"+experiment+"/pr_no_bc/"

# =====================================================================================================

# Every RCM output file has predictable root name (specific to resolution!)
# ==> Construct data file names


#8/10 models. 2 more below in separate FOR loops.
models_list_50km = ['CCCma-CanESM2','CNRM-CERFACS-CNRM-CM5','NCC-NorESM1-M',
                    'MPI-M-MPI-ESM-LR','IPSL-IPSL-CM5A-MR','MIROC-MIROC5',
                    'NOAA-GFDL-GFDL-ESM2M','CSIRO-QCCCE-CSIRO-Mk3-6-0']


for model in models_list_50km:


	#  New root for non-bias corrected (!nbc!) files:
	pr_nbc_file_root_hist = "pr_EUR-44_"+model+"_historical_r1i1p1_SMHI-RCA4_v1_day_"
	pr_nbc_file_root_proj = "pr_EUR-44_"+model+"_"+experiment+"_r1i1p1_SMHI-RCA4_v1_day_"


	# Explicit list
	files_pr_nbc_50km_hist = in_path_RCM_pr_nbc_50km+pr_nbc_file_root_hist+"19660101-19701231.nc"
	files_pr_nbc_50km_proj = in_path_RCM_pr_nbc_50km+pr_nbc_file_root_proj+"20060101-20101231.nc"


	# Tell me which files you imported
	# print 'Historical input Model files:', files_pr_nbc_50km_hist   # sep='\n'
	# print 'Projection input Model files:', files_pr_nbc_50km_proj   # sep='\n'

	# Create datasets from netCDF files
	nc_in_hist = Dataset(files_pr_nbc_50km_hist,'r')
	nc_in_proj = Dataset(files_pr_nbc_50km_proj,'r')


	# Print current GCM tracking id
	print "", nc_in_hist.tracking_id

	print "", nc_in_proj.tracking_id
	# print 'GCM_tracking_id is:' gcm_tracking_id


quit()


END

)



# Create new tracking id for the new indice file
#track_id_indice=$(python  -c 'import uuid; print uuid.uuid4()')
#echo "Tracking id is:", $track_id_indice


#echo "GCM Tracking id for mode:" $track_GCM_indice

dir_in=/nobackup/users/stepanov/indices_tracking_id_test/EUR-44/rcp45/pr
indices=



ncatted -O -a invar_tracking_id,global,o,c,' ' -h ${dir_in}${indices}_*.nc