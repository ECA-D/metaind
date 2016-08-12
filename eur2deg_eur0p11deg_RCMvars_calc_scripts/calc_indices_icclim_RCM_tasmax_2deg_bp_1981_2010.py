# Make python script executable
#!/usr/bin/python


# ==================================================
# Script to calculate indices from ensemble of RCMs
# on resolutions 2.0deg for CLIPC
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

# TASmax
in_path_RCM_tasmax_2deg=nobackup_stepanov+"CLIPC/Model_data/tasmax/rcp45/2deg/daily/SMHI_DBS43_2006_2100/"
out_path_RCM_tasmax_2deg=nobackup_stepanov+"icclim_indices/RCM/tasmax/2deg/"

# =====================================================================================================


# Every RCM output file has predictable root name (specific to resolution!)
# So, contrstruct data file names >>>>>>>>>

# #models_list_2deg = ['CanESM2','CNRM-CM5','NorESM1-M','IPSL-CM5A-MR','MIROC5','GFDL-ESM2M','MPI-ESM-LR']

# # Debug models list. NorESM & IPSL complain about time range error
# #models_list_2deg = ['NorESM1-M']#,'IPSL-CM5A-MR']
# models_list_2deg = ['IPSL-CM5A-MR']
# #models_list_2deg = ['NorESM1-M']


# # Last active list
# # Debug models list: everything except NorESM1-M and IPSL model
# #models_list_2deg = ['CanESM2','CNRM-CM5','MIROC5','GFDL-ESM2M','MPI-ESM-LR']


# for model in models_list_2deg:

# 	tasmax_2deg_file_root="tasmaxAdjust_day_"+model+"-EUR-2deg_rcp45_r1i1p1-SMHI-DBS43-EOBS10-1981-2010_"

# 	# Desired periods
# 	period_2deg_historical='19510101-20051231'
# 	period_2deg_projection='20060101-21001231'
# 	# Merged period
# 	period_2deg_merged='19510101-21001231'

 
# 	file_tasmax_2deg_RCM_ref        = in_path_RCM_tasmax_2deg+tasmax_2deg_file_root+period_2deg_historical+'.nc'
# 	file_tasmax_2deg_RCM            = in_path_RCM_tasmax_2deg+tasmax_2deg_file_root+period_2deg_projection+'.nc'
# 	file_tasmax_2deg_RCM_merged     = in_path_RCM_tasmax_2deg+tasmax_2deg_file_root+period_2deg_merged+'.nc'

# 	print file_tasmax_2deg_RCM_ref
# 	print file_tasmax_2deg_RCM

# 	#files_tasmax_2deg = [file_tasmax_2deg_RCM_ref,file_tasmax_2deg_RCM]
# 	files_tasmax_2deg = [file_tasmax_2deg_RCM_merged]


# # =========================================================================
# # Processing periods

# # Base period
# #	base_dt1 = datetime.datetime(1981,01,01)
# #	base_dt2 = datetime.datetime(2010,12,31)

# # Analysis period
# #	dt1 = datetime.datetime(2006,01,01)
# #	dt2 = datetime.datetime(2100,12,31)



# # Debugging periods for NorESM1-M:

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
# 	indice_list_max_temp = ['TX90p'] #TX90p
# # =========================================================================


# # =========================================================================
# # Calculate actual indices: ICCLIM syntax only
# # =========================================================================

# 	for indice_max_temp in indice_list_max_temp:
# 		print
# 		print 'Now calculating indice', indice_max_temp,':'
# 		print 'Using the model', model
# 		print


# # Build output file name construction phase
# 		calc_indice_max_temp = out_path_RCM_tasmax_2deg+indice_max_temp+"_"+model+'_temp_max.nc'
# 		print 'Going into output file:', calc_indice_max_temp
# 		print

	
# 		icclim.indice(indice_name=indice_max_temp,
# 	    	          in_files=files_tasmax_2deg,
# 	        	      var_name='tasmaxAdjust', 
#                 	  #slice_mode='AMJJAS', 
#                   	  time_range=[dt1,dt2], 
#                       base_period_time_range=[base_dt1, base_dt2],
#                       out_unit = 'days',
#                       out_file=calc_indice_max_temp, 
#                       callback=callback.defaultCallback2)



#=================================================================================================
# HadGEM mode (period ends iwth yyyy1230!)

models_list_2deg_HadGEM = ['HadGEM2-ES']

for model in models_list_2deg_HadGEM:


	tasmax_2deg_file_root="tasmaxAdjust_day_"+model+"-EUR-2deg_rcp45_r1i1p1-SMHI-DBS43-EOBS10-1981-2010_"

#	Desired periods
	period_2deg_historical='19510101-20051230'
	period_2deg_projection='20060101-21001230'


	file_tasmax_2deg_RCM_ref = in_path_RCM_tasmax_2deg+tasmax_2deg_file_root+period_2deg_historical+'.nc'
	file_tasmax_2deg_RCM     = in_path_RCM_tasmax_2deg+tasmax_2deg_file_root+period_2deg_projection+'.nc'

	print file_tasmax_2deg_RCM_ref
	print file_tasmax_2deg_RCM

	files_tasmax_2deg = [file_tasmax_2deg_RCM_ref,file_tasmax_2deg_RCM]


#=========================================================================
#Processing periods

#Base period
	base_dt1 = datetime.datetime(1981,01,01)   # 1981,01,01
	base_dt2 = datetime.datetime(2010,10,30)   # 2010,12,30

#Analysis period
	dt1 = datetime.datetime(2006,01,01)        # 2006,01,01
	dt2 = datetime.datetime(2100,10,30)        # 2100,12,30
#=========================================================================


# Important!
# =========================================================================
# Declare which indices you want to calculate using lists
	indice_list_max_temp = ['TX90p'] #TX90p ID
# =========================================================================


# =========================================================================
# Calculate actual indices: ICCLIM syntax only
# =========================================================================

	for indice_max_temp in indice_list_max_temp:
		print
		print 'Now calculating indice', indice_max_temp,':'
		print 'Using the model', model
		print


#Build output file name construction phase
		calc_indice_max_temp = out_path_RCM_tasmax_2deg+indice_max_temp+"_"+model+'_temp_max.nc'
		print 'Going into output file:', calc_indice_max_temp
		print

	
		icclim.indice(indice_name=indice_max_temp,
	    	          in_files=files_tasmax_2deg,
	        	      var_name='tasmaxAdjust', 
               	      #slice_mode='AMJJAS', 
                 	  time_range=[dt1,dt2], 
                      base_period_time_range=[base_dt1, base_dt2],
                      out_file=calc_indice_max_temp, 
                      callback=callback.defaultCallback2)



#=================================================================================================
# EC Earth model (r12i1pi in file name!)

# models_list_2deg_EC_EARTH = ['EC-EARTH']

# for model in models_list_2deg_EC_EARTH:

# 	tasmax_2deg_file_root="tasmaxAdjust_day_"+model+"-EUR-2deg_rcp45_r12i1p1-SMHI-DBS43-EOBS10-1981-2010_"

# #	Desired periods
# 	period_2deg_historical='19510101-20051231'
# 	period_2deg_projection='20060101-21001231'
# # Merged period
# 	period_2deg_merged='19510101-21001231'


# 	file_tasmax_2deg_RCM_ref        = in_path_RCM_tasmax_2deg+tasmax_2deg_file_root+period_2deg_historical+'.nc'
# 	file_tasmax_2deg_RCM            = in_path_RCM_tasmax_2deg+tasmax_2deg_file_root+period_2deg_projection+'.nc'
# 	file_tasmax_2deg_RCM_merged     = in_path_RCM_tasmax_2deg+tasmax_2deg_file_root+period_2deg_merged+'.nc'

# 	#print file_tasmax_2deg_RCM_ref
# 	#print file_tasmax_2deg_RCM

# 	#files_tasmax_2deg = [file_tasmax_2deg_RCM_ref,file_tasmax_2deg_RCM]
# 	files_tasmax_2deg = [file_tasmax_2deg_RCM_merged]

# 	print files_tasmax_2deg

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

# 	indice_list_max_temp = ['TX90p']   #TX90p
# # =========================================================================


# # =========================================================================
# # Calculate actual indices: ICCLIM syntax only
# # =========================================================================

# 	for indice_max_temp in indice_list_max_temp:
# 		print
# 		print 'Now calculating indice', indice_max_temp,':'
# 		print 'Using the model', model
# 		print


# # Build output file name construction phase
# 		calc_indice_max_temp = out_path_RCM_tasmax_2deg+indice_max_temp+"_"+model+'_temp_max.nc'
# 		print 'Going into output file:', calc_indice_max_temp
# 		print

	
# 		icclim.indice(indice_name=indice_max_temp,
# 	    	          in_files=files_tasmax_2deg,
# 	        	      var_name='tasmaxAdjust', 
#                	      #slice_mode='AMJJAS', 
#                  	  time_range=[dt1,dt2], 
#                       base_period_time_range=[base_dt1, base_dt2],
#                       out_file=calc_indice_max_temp, 
#                       callback=callback.defaultCallback2)




# Done with calculations

print
print 'Done!'
print

quit()
