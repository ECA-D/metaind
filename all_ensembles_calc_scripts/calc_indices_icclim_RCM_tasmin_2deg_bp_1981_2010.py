# Make python script executable
#!/usr/bin/python


# ==================================================
# Script to calculate indices from ensemble of RCMs
# on resolutions 2.0deg for CLIPC
# This one does only TASMIN indices
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

# RCM output data and output of calculated indices: All to no /nobackup

nobackup_stepanov='/nobackup/users/stepanov/'  # local HDD mount point

# Resolutions are 2deg, 50km and 12km.
# Can be looped later on to lighten structure, but no need for now.

# Minimum temperature 2deg
in_path_RCM_tasmin_2deg=nobackup_stepanov+"CLIPC/Model_data/tasmin/rcp45/2deg/daily/SMHI_DBS43_2006_2100/"
out_path_RCM_tasmin_2deg=nobackup_stepanov+"icclim_indices/RCM/tasmin/2deg/"

# =====================================================================================================
# Every RCM output file has predictable root name (specific to resolution!)
# Construct data file names


# 7/9 models. 2 more below with separate analysis time or paths/file names
#models_list_2deg = ['CanESM2','CNRM-CM5','NorESM1-M','IPSL-CM5A-MR','MIROC5','GFDL-ESM2M','MPI-ESM-LR']

# Debug model list. IPSL has time range issue
#models_list_2deg = ['CanESM2','CNRM-CM5','NorESM1-M','MIROC5','GFDL-ESM2M','MPI-ESM-LR']

# for model in models_list_2deg:

# 	tasmin_2deg_file_root="tasminAdjust_day_"+model+"-EUR-2deg_rcp45_r1i1p1-SMHI-DBS43-EOBS10-1981-2010_"


# # Desired periods
# 	period_2deg_historical='19510101-20051231'
# 	period_2deg_projection='20060101-21001231'


# 	file_tasmin_2deg_RCM_ref = in_path_RCM_tasmin_2deg+tasmin_2deg_file_root+period_2deg_historical+'.nc'
# 	file_tasmin_2deg_RCM     = in_path_RCM_tasmin_2deg+tasmin_2deg_file_root+period_2deg_projection+'.nc'

# 	print 'In file [historical]',file_tasmin_2deg_RCM_ref
# 	print 'In file [projections]',file_tasmin_2deg_RCM

# 	files_tasmin_2deg = [file_tasmin_2deg_RCM_ref,file_tasmin_2deg_RCM]

# #quit()


# # =========================================================================
# # Processing periods

# # Base period
# 	base_dt1 = datetime.datetime(1981,01,01)
# 	base_dt2 = datetime.datetime(2010,12,31)

# # Analysis period
# 	dt1 = datetime.datetime(2006,01,01)
# 	dt2 = datetime.datetime(2100,12,31)
# # =========================================================================


# # Important!
# # =========================================================================
# # Declare which indices you want to calculate using lists
# 	indice_list_tasmin = ['FD']
# # =========================================================================


# # =========================================================================
# # Calculate actual indices: ICCLIM syntax only
# # =========================================================================

# 	for indice_tasmin in indice_list_tasmin:
# 		print
# 		print 'Now calculating indice', indice_tasmin,':'
# 		print 'Using the model', model
# 		print


# # Build output file name construction phase
# 		calc_indice_tasmin = out_path_RCM_tasmin_2deg+indice_tasmin+"_"+model+'_tasmin.nc'
# 		print 'Going into output file:', calc_indice_tasmin
# 		print

	
# 		icclim.indice(indice_name=indice_tasmin,
# 	    	          in_files=files_tasmin_2deg,
# 	        	      var_name='tasminAdjust', 
#                 	  #slice_mode='AMJJAS', 
#          	          time_range=[dt1,dt2], 
#             	      base_period_time_range=[base_dt1, base_dt2],
#                 	  out_file=calc_indice_tasmin, 
#                  	  callback=callback.defaultCallback2)







#=================================================================================================
# HadGEM mode (period ends iwth yyyy1230!)

models_list_2deg_HadGEM = ['HadGEM2-ES']

for model in models_list_2deg_HadGEM:

	tasmin_2deg_file_root="tasminAdjust_day_"+model+"-EUR-2deg_rcp45_r1i1p1-SMHI-DBS43-EOBS10-1981-2010_"


#Desired periods
	period_2deg_historical='19510101-20051230'
	period_2deg_projection='20060101-21001230'


	file_tasmin_2deg_RCM_ref = in_path_RCM_tasmin_2deg+tasmin_2deg_file_root+period_2deg_historical+'.nc'
	file_tasmin_2deg_RCM     = in_path_RCM_tasmin_2deg+tasmin_2deg_file_root+period_2deg_projection+'.nc'

	print file_tasmin_2deg_RCM_ref
	print file_tasmin_2deg_RCM

	files_tasmin_2deg = [file_tasmin_2deg_RCM_ref,file_tasmin_2deg_RCM]


# =========================================================================
# Processing periods

# Base period
	base_dt1_HadGEM = datetime.datetime(1981,01,01)
	base_dt2_HadGEM = datetime.datetime(2010,12,30)

# Analysis period
	dt1_HadGEM = datetime.datetime(2006,01,01)
	dt2_HadGEM = datetime.datetime(2100,12,30)
# =========================================================================



# Important!
# =========================================================================
# Declare which indices you want to calculate using lists

	indice_list_tasmin = ['FD']

# =========================================================================



# =========================================================================
# Calculate actual indices: ICCLIM syntax only
# =========================================================================

	for indice_tasmin in indice_list_tasmin:
		print
		print 'Now calculating indice', indice_tasmin,':'
		print 'Using the model', model
		print


# Build output file name construction phase
		calc_indice_tasmin = out_path_RCM_tasmin_2deg+indice_tasmin+"_"+model+'_tasmin.nc'
		print 'Going into output file:', calc_indice_tasmin
		print

	
		icclim.indice(indice_name=indice_tasmin,
	    	          in_files=files_tasmin_2deg,
	        	      var_name='tasminAdjust', 
    	           	  slice_mode='AMJJAS', 
	       	          time_range=[dt1_HadGEM,dt2_HadGEM], 
         	          ignore_Feb29th=True,
           	          base_period_time_range=[base_dt1_HadGEM, base_dt2_HadGEM],
               	      out_file=calc_indice_tasmin, 
                	  callback=callback.defaultCallback2)




#=================================================================================================
# EC Earth model (r12i1pi in file name!)

# models_list_2deg_EC_EARTH = ['EC-EARTH']

# for model in models_list_2deg_EC_EARTH:

# 	tasmin_2deg_file_root="tasminAdjust_day_"+model+"-EUR-2deg_rcp45_r12i1p1-SMHI-DBS43-EOBS10-1981-2010_"


# # Desired periods
# 	period_2deg_historical='19510101-20051231'
# 	period_2deg_projection='20060101-21001231'


# 	file_tasmin_2deg_RCM_ref = in_path_RCM_tasmin_2deg+tasmin_2deg_file_root+period_2deg_historical+'.nc'
# 	file_tasmin_2deg_RCM     = in_path_RCM_tasmin_2deg+tasmin_2deg_file_root+period_2deg_projection+'.nc'

# 	print file_tasmin_2deg_RCM_ref
# 	print file_tasmin_2deg_RCM

# 	files_tasmin_2deg = [file_tasmin_2deg_RCM_ref,file_tasmin_2deg_RCM]

# #quit()


# # =========================================================================
# # Processing periods

# # Base period
# 	base_dt1 = datetime.datetime(1981,01,01)
# 	base_dt2 = datetime.datetime(2010,12,31)

# # Analysis period
# 	dt1 = datetime.datetime(2006,01,01)
# 	dt2 = datetime.datetime(2100,12,31)
# # =========================================================================



# # Important!
# # =========================================================================
# # Declare which indices you want to calculate using lists
# 	indice_list_tasmin = ['FD']
# # =========================================================================



# # =========================================================================
# # Calculate actual indices: ICCLIM syntax only
# # =========================================================================

# 	for indice_tasmin in indice_list_tasmin:
# 		print
# 		print 'Now calculating indice', indice_tasmin,':'
# 		print 'Using the model', model
# 		print


# # Build output file name construction phase
# 		calc_indice_tasmin = out_path_RCM_tasmin_2deg+indice_tasmin+"_"+model+'_tasmin.nc'
# 		print 'Going into output file:', calc_indice_tasmin
# 		print

	
# 		icclim.indice(indice_name=indice_tasmin,
# 	    	          in_files=files_tasmin_2deg,
# 	        	      var_name='tasminAdjust', 
#                 	  #slice_mode='AMJJAS', 
#          	          time_range=[dt1,dt2], 
#             	      base_period_time_range=[base_dt1, base_dt2],
#                 	  out_file=calc_indice_tasmin, 
#                  	  callback=callback.defaultCallback2)



# Done with calculations for all 9/9 models

print
print 'Done!'
print

quit()
