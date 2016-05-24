# Make python script executable
#!/usr/bin/python


# ==================================================
# Script to calculate indices from ensemble of RCMs
# on resolutions 0.11deg (12km)  for CLIPC
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
# Parallel run add-ons
from joblib import Parallel, delayed  
import multiprocessing


print
print '<<Loaded python modules>>'
print

# =====================================================================================================
# Define some paths

# RCM output data and output of calculated indices: All to no /nobackup, local
nobackup_stepanov='/nobackup/users/stepanov/'  # my locad HDD mount point

# Precip
in_path_RCM_pr_12km=nobackup_stepanov+"CLIPC/Model_data/pr/rcp45/12km/daily/SMHI_DBS43_2006_2100/"
out_path_RCM_pr_12km=nobackup_stepanov+"icclim_indices/RCM/pr/12km/"

# =====================================================================================================

# Every RCM output file has predictable root name (specific to resolution!)
# ==> Construct data file names


# 7/9 models. 2 more below in separate FOR loops.
# models_list_12km = ['CCCma-CanESM2','CNRM-CERFACS-CNRM-CM5','NCC-NorESM1-M',
#                     'MPI-M-MPI-ESM-LR','IPSL-IPSL-CM5A-MR','MIROC-MIROC5',
#                     'NOAA-GFDL-GFDL-ESM2M']

models_list_12km = ['CNRM-CERFACS-CNRM-CM5']

	
# =========================================================================
# Processing periods

# Base period
# base_dt1 = datetime.datetime(1981,01,01)
# base_dt2 = datetime.datetime(2010,12,31)

#Analysis period
# dt1 = datetime.datetime(2006,01,01)
# dt2 = datetime.datetime(2100,12,31)


# Debugging processing periods

# Base period
#base_dt1 = datetime.datetime(1981,01,01)
#base_dt2 = datetime.datetime(2010,12,31)

# debug memory
base_dt1 = datetime.datetime(1981,01,01)
base_dt2 = datetime.datetime(2010,12,31)

#Analysis period
#dt1 = datetime.datetime(2011,01,01)
#dt2 = datetime.datetime(2015,12,31)

# debug memory
dt1 = datetime.datetime(2011,01,01)
dt2 = datetime.datetime(2015,12,31)


# =========================================================================


# Important!
# =========================================================================
# Declare which indices you want to calculate using lists
indice_list_pp = ['R95p']  #R95p RX1day RR1
indice_pp = 'R95p'
# =========================================================================


for model in models_list_12km:


	pr_12km_file_root="prAdjust_EUR-11_"+model+"_rcp45_r1i1p1_SMHI-RCA4_v1-SMHI-DBS43-MESAN-1989-2010_day_"
	#print pr_50km_file_root

	# Explicit list
	files_pr_12km = [in_path_RCM_pr_12km+pr_12km_file_root+"19810101-19851231.nc",
					 in_path_RCM_pr_12km+pr_12km_file_root+"19860101-19901231.nc",
	                 in_path_RCM_pr_12km+pr_12km_file_root+"19910101-19951231.nc",
	                 in_path_RCM_pr_12km+pr_12km_file_root+"19960101-20001231.nc",
	                 in_path_RCM_pr_12km+pr_12km_file_root+"20010101-20051231.nc",
	                 in_path_RCM_pr_12km+pr_12km_file_root+"20060101-20101231.nc",
	                 in_path_RCM_pr_12km+pr_12km_file_root+"20110101-20151231.nc"]#,
		            # in_path_RCM_pr_12km+pr_12km_file_root+"20160101-20201231.nc"]#,
		             # in_path_RCM_pr_12km+pr_12km_file_root+"20210101-20251231.nc",
	 	            #  in_path_RCM_pr_12km+pr_12km_file_root+"20260101-20301231.nc",
		             # in_path_RCM_pr_12km+pr_12km_file_root+"20310101-20351231.nc",
		             # in_path_RCM_pr_12km+pr_12km_file_root+"20360101-20401231.nc"]#,
	              #    in_path_RCM_pr_12km+pr_12km_file_root+"20410101-20451231.nc",
		             # in_path_RCM_pr_12km+pr_12km_file_root+"20460101-20501231.nc",
		             # in_path_RCM_pr_12km+pr_12km_file_root+"20510101-20551231.nc",
		             # in_path_RCM_pr_12km+pr_12km_file_root+"20560101-20601231.nc",
		             # in_path_RCM_pr_12km+pr_12km_file_root+"20610101-20651231.nc",
		             # in_path_RCM_pr_12km+pr_12km_file_root+"20660101-20701231.nc",
	              #    in_path_RCM_pr_12km+pr_12km_file_root+"20710101-20751231.nc",
	              #    in_path_RCM_pr_12km+pr_12km_file_root+"20760101-20801231.nc",
	              #    in_path_RCM_pr_12km+pr_12km_file_root+"20810101-20851231.nc",
	              #    in_path_RCM_pr_12km+pr_12km_file_root+"20860101-20901231.nc",
	              #    in_path_RCM_pr_12km+pr_12km_file_root+"20910101-20951231.nc",
	              #    in_path_RCM_pr_12km+pr_12km_file_root+"20960101-21001231.nc"]

	print 'All input Model files:', files_pr_12km



#=======================================================================================
# Code mutation single thread to parallel
# for i in inputs
#     results[i] = processInput(i)
# end
# #// now do something with results



# # what are your inputs, and what operation do you want to 
# # perform on each input. For example...


# inputs = range(100000000)  
# def processInput(i):  
#     return i * i

# num_cores = multiprocessing.cpu_count()

# results = Parallel(n_jobs=num_cores)(delayed(processInput)(i) for i in inputs)  

# print(results)
#=======================================================================================


# =========================================================================
# Calculate actual indices: ICCLIM syntax only
# =========================================================================

# Build output file name construction phase
	calc_indice_pp = out_path_RCM_pr_12km+indice_pp+"_"+model+'_pp_parallel.nc'
	print 'Going into output file:', calc_indice_pp
	print

	#for indice_pp in indice_list_pp:
	def indices(indice_pp):
		return icclim.indice(indice_name=indice_pp,
		    		         in_files=files_pr_12km,
		        	         var_name='prAdjust', 
	               	         #slice_mode='AMJJAS', 
	        	             time_range=[dt1,dt2], 
	           	             base_period_time_range=[base_dt1, base_dt2],
	               	         out_file=calc_indice_pp, 
	                         callback=callback.defaultCallback2)




	num_cores = multiprocessing.cpu_count()
	#num_cores = 1
	print 'Using this many cores', num_cores
		
	results = Parallel(n_jobs=num_cores)(delayed(indices)(indice_pp) for indice_pp in indice_list_pp)

	print(results)

#=================================================================================================
# HadGEM mode (period ends iwth yyyy1230!)

# models_list_50km_HadGEM = ['MOHC-HadGEM2-ES']

# for model in models_list_50km_HadGEM:

# 	pr_50km_file_root="prAdjust_EUR-44_"+model+"_rcp45_r1i1p1_SMHI-RCA4_v1-SMHI-DBS43-EOBS10-1981-2010_day_"


# 	# Explicit list
# 	files_pr_50km = [in_path_RCM_pr_50km+pr_50km_file_root+"19810101-19851230.nc",
# 					 in_path_RCM_pr_50km+pr_50km_file_root+"19860101-19901230.nc",
# 	                 in_path_RCM_pr_50km+pr_50km_file_root+"19910101-19951230.nc",
# 	                 in_path_RCM_pr_50km+pr_50km_file_root+"19960101-20001230.nc",
# 	                 in_path_RCM_pr_50km+pr_50km_file_root+"20010101-20051230.nc",
# 	                 in_path_RCM_pr_50km+pr_50km_file_root+"20060101-20101230.nc",
# 	                 in_path_RCM_pr_50km+pr_50km_file_root+"20110101-20151230.nc",
# 		             in_path_RCM_pr_50km+pr_50km_file_root+"20160101-20201230.nc",
# 		             in_path_RCM_pr_50km+pr_50km_file_root+"20210101-20251230.nc",
# 	 	             in_path_RCM_pr_50km+pr_50km_file_root+"20260101-20301230.nc",
# 		             in_path_RCM_pr_50km+pr_50km_file_root+"20310101-20351230.nc",
# 		             in_path_RCM_pr_50km+pr_50km_file_root+"20360101-20401230.nc",
# 	                 in_path_RCM_pr_50km+pr_50km_file_root+"20410101-20451230.nc",
# 		             in_path_RCM_pr_50km+pr_50km_file_root+"20460101-20501230.nc",
# 		             in_path_RCM_pr_50km+pr_50km_file_root+"20510101-20551230.nc",
# 		             in_path_RCM_pr_50km+pr_50km_file_root+"20560101-20601230.nc",
# 		             in_path_RCM_pr_50km+pr_50km_file_root+"20610101-20651230.nc",
# 		             in_path_RCM_pr_50km+pr_50km_file_root+"20660101-20701230.nc",
# 	                 in_path_RCM_pr_50km+pr_50km_file_root+"20710101-20751230.nc",
# 	                 in_path_RCM_pr_50km+pr_50km_file_root+"20760101-20801230.nc",
# 	                 in_path_RCM_pr_50km+pr_50km_file_root+"20810101-20851230.nc",
# 	                 in_path_RCM_pr_50km+pr_50km_file_root+"20860101-20901230.nc",
# 	                 in_path_RCM_pr_50km+pr_50km_file_root+"20910101-20951230.nc",
# 	                 in_path_RCM_pr_50km+pr_50km_file_root+"20960101-20991130.nc"]

# 	print 'All input Model files:', files_pr_50km


# # =========================================================================
# # Processing periods (spicific to HadGem for the missing 31.12.)

# # Base period
# 	base_dt1_HadGEM = datetime.datetime(1981,01,01)
# 	base_dt2_HadGEM = datetime.datetime(2010,12,30)

# # Analysis period
# 	dt1_HadGEM = datetime.datetime(2006,01,01)
# 	dt2_HadGEM = datetime.datetime(2099,11,30)
# # =========================================================================


# # =========================================================================
# # Calculate actual indices: ICCLIM syntax only
# # =========================================================================

# 	for indice_pp in indice_list_pp:
# 		print
# 		print 'Now calculating indice', indice_pp,':'
# 		print 'Using the model', model
# 		print

# #Build output file name construction phase
# 		calc_indice_pp = out_path_RCM_pr_50km+indice_pp+"_"+model+'_pp.nc'
# 		print 'Going into output file:', calc_indice_pp
# 		print

	
# 		icclim.indice(indice_name=indice_pp,
# 	    	          in_files=files_pr_50km,
# 	        	      var_name='prAdjust', 
#               	 	  #slice_mode='AMJJAS', 
#       	        	  time_range=[dt1_HadGEM,dt2_HadGEM], 
#         	          #ignore_Feb29th=True,
#            	    	  base_period_time_range=[base_dt1_HadGEM, base_dt2_HadGEM],
#                		  out_file=calc_indice_pp, 
#                 	  callback=callback.defaultCallback2)







#=================================================================================================
# EC Earth model (r12i1pi in file name!)

#models_list_50km_EC_EARTH = ['ICHEC-EC-EARTH']

#for model in models_list_50km_EC_EARTH:

#	pr_50km_file_root="prAdjust_EUR-44_"+model+"_rcp45_r12i1p1_SMHI-RCA4_v1-SMHI-DBS43-EOBS10-1981-2010_day_"


# Desired periods
#	period_50km_historical='19510101-20051231'
#	period_50km_projection='20060101-21001231'


#	file_pr_50km_RCM_ref = in_path_RCM_pr_50km+pr_50km_file_root+period_50km_historical+'.nc'
#	file_pr_50km_RCM     = in_path_RCM_pr_50km+pr_50km_file_root+period_50km_projection+'.nc'

#	print file_pr_50km_RCM_ref
#	print file_pr_50km_RCM

#	files_pr_50km = [file_pr_50km_RCM_ref,file_pr_50km_RCM]

#quit()


# =========================================================================
# Processing periods

# Base period
#	base_dt1 = datetime.datetime(1981,01,01)
#	base_dt2 = datetime.datetime(2010,12,31)

# Analysis period
#	dt1 = datetime.datetime(2006,01,01)
#	dt2 = datetime.datetime(2100,12,31)
# =========================================================================



# Important!
# =========================================================================
# Declare which indices you want to calculate using lists
#	indice_list_pp = ['R95p','RX1day']
# =========================================================================



# =========================================================================
# Calculate actual indices: ICCLIM syntax only
# =========================================================================

#	for indice_pp in indice_list_pp:
#		print
#		print 'Now calculating indice', indice_pp,':'
#		print 'Using the model', model
#		print


# Build output file name construction phase
#		calc_indice_pp = out_path_RCM_pr_50km+indice_pp+"_"+model+'_pp.nc'
#		print 'Going into output file:', calc_indice_pp
#		print

	
#		icclim.indice(indice_name=indice_pp,
#	    	          in_files=files_pr_50km,
#	        	      var_name='prAdjust', 
 #               	  #slice_mode='AMJJAS', 
  #       	          time_range=[dt1,dt2], 
   #         	      base_period_time_range=[base_dt1, base_dt2],
    #            	  out_file=calc_indice_pp, 
     #            	  callback=callback.defaultCallback2)



# Done with calculations for all 9/9 models

print
print 'Done!'
print

quit()
