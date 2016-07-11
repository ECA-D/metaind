# Make python script executable
#!/usr/bin/python


# ==================================================
# Script to calculate indices from ensemble of RCMs
# on resolutions 0.44deg (50km)  for CLIPC
# This one does only PRECIP indices
# ==================================================


# ==========================================
# Author: I.Stepanov (igor.stepanov@knmi.nl)
# 29.02.2016 @KNMI
# ============================================================================================
# Updates list
# 29.02.2016. Script created as a derivative of EOBS import data to calculate climate indices
# 03.03.2016. Making the base script into version that calculates R95, TX90, RR1, FD
# ============================================================================================


# ==============================================================
# Should work for input parameters: precipitation (pr)
#                                 : tempearture (tas)
#                                 : minimum temperature (tasmin)
#                                 : maximum temperature (tasmax)
# ==============================================================

import netCDF4
import ctypes
import icclim
import datetime
import icclim.util.callback as callback
#cb = callback.defaultCallback


print
print '<<Loaded python modules>>'
print

# =====================================================================================================
# Define some paths

# RCM output data and output of calculated indices: All to no /nobackup, local
nobackup_stepanov='/nobackup/users/stepanov/'  # my locad HDD mount point

# Precip
in_path_RCM_pr_50km=nobackup_stepanov+"CLIPC/Model_data/pr/rcp45/50km/daily/SMHI_DBS43_2006_2100/"
out_path_RCM_pr_50km=nobackup_stepanov+"icclim_indices/RCM/pr/50km/"

# =====================================================================================================

# Every RCM output file has predictable root name (specific to resolution!)
# ==> Construct data file names


# 7/9 models. 2 more below in separate FOR loops.
#models_list_50km = ['CCCma-CanESM2','CNRM-CERFACS-CNRM-CM5','NCC-NorESM1-M',
#                    'MPI-M-MPI-ESM-LR','IPSL-IPSL-CM5A-MR','MIROC-MIROC5',
#                    'NOAA-GFDL-GFDL-ESM2M']

# debugging list. CCCma failed
#models_list_50km = ['MIROC-MIROC5'] #,
					#'NOAA-GFDL-GFDL-ESM2M']
model = 'MIROC-MIROC5'

periods_50km_list = ['19810101-19851231',
                     '19860101-19901231',
                     '19910101-19951231',
                     '19960101-20001231',
                     '20010101-20051231',
                     '20060101-20101231',
                     '20110101-20151231',
		             '20160101-20201231',
		             '20210101-20251231',
 	 	             '20260101-20301231',
 		             '20310101-20351231',
 		             '20360101-20401231',
 	                 '20410101-20451231',
		             '20460101-20501231',
		             '20510101-20551231',
		             '20560101-20601231',
		             '20610101-20651231',
		             '20660101-20701231',
                     '20710101-20751231',
                     '20760101-20801231',
                     '20810101-20851231',
                     '20860101-20901231',
                     '20910101-20951231',
                     '20960101-21001231']
	
# =========================================================================
# Processing periods

# Base period
base_dt1 = datetime.datetime(1981,01,02)
base_dt2 = datetime.datetime(2010,12,31)

# Analysis period
dt1 = datetime.datetime(2006,01,02)
dt2 = datetime.datetime(2100,12,31)
# =========================================================================


# Important!
# =========================================================================
# Declare which indices you want to calculate using lists
#indice_list_pp = ['RR1']  #R95p RX1day RR1
indice_pp = 'RR1'
# =========================================================================



# Construction data names and loops to import all separated data in

periods_50km_list = ['19810101-19851231',
                     '19860101-19901231',
                     '19910101-19951231',
                     '19960101-20001231',
                     '20010101-20051231',
                     '20060101-20101231',
                     '20110101-20151231',
		             '20160101-20201231',
		             '20210101-20251231',
 	 	             '20260101-20301231',
 		             '20310101-20351231',
 		             '20360101-20401231',
 	                 '20410101-20451231',
		             '20460101-20501231',
		             '20510101-20551231',
		             '20560101-20601231',
		             '20610101-20651231',
		             '20660101-20701231',
                     '20710101-20751231',
                     '20760101-20801231',
                     '20810101-20851231',
                     '20860101-20901231',
                     '20910101-20951231',
                     '20960101-21001231']


# Beggining of the outer loop for climatological models
#for model in models_list_50km:

pr_50km_file_root="prAdjust_EUR-44_"+model+"_rcp45_r1i1p1_SMHI-RCA4_v1-SMHI-DBS43-EOBS10-1981-2010_day_"
#print pr_50km_file_root

# Build output file name construction phase
calc_indice_pp = out_path_RCM_pr_50km+indice_pp+"_"+model+'_pp.nc'
print 'Going into output file:', calc_indice_pp
print

files_pr_50km = [None] * len(periods_50km_list)     # Creates empty list
print 'Empty list:', files_pr_50km

# =====================================================================================================
# Beggining of the inner loop for climatological periods
	
#for period_50km in periods_50km_list:

#	print 'list', files_pr_50km

#	file_pr_50km_RCM = in_path_RCM_pr_50km+pr_50km_file_root+period_50km+".nc"
#	print 'Files to be merged in a big list are:',file_pr_50km_RCM



#	files_pr_50km = [file_pr_50km_RCM]
#	files_pr_50km.extend(file_pr_50km_RCM)

	#files_pr_50km = files_pr_50km.append(file_pr_50km_RCM)



#aList = [123, 'xyz', 'zara', 'abc'];
#aList.append( 2009 );
#print "Updated List : ", aList



#	print 'Number of elements in this list is:', len(files_pr_50km)
#print 'All input Model files:', files_pr_50km
#quit()



print
print 'Done!'
print

quit()
