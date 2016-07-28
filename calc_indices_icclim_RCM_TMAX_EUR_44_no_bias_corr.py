# Make python script executable
#!/usr/bin/python

# File name: calc_indices_icclim_RCM_TMAX_50km_bp_1981_2010_no_bias_corr.py

# ==================================================
# Script to calculate indices from ensemble of RCMs
# on resolutions 0.44deg (50km)  for CLIPC
# This one does only PRECIP indices and only
# non bias corrected data
# ==================================================


# ==========================================
# Author: I.Stepanov (igor.stepanov@knmi.nl)
# 29.02.2016 @KNMI
# ============================================================================================
# Updates list
# 29.02.2016. Script created as a derivative of EOBS import data to calculate climate indices
# 03.03.2016. Making the base script into version that calculates R95, TX90, RR1, FD
# 03.05.2016. Included CSIRO model and transient periods (1970-2005) for Juliane
# 20.05.2016. Including non-bias corrected precip data
# 24.05.2016. Indice file output file naming conventions match DRS document May 2016 (version....?)
# 24.05.2016. HadGEM indices to be run only from 360_days GH branch, via virtualenv
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

#experiment='rcp45'
experiment='rcp85'

# RCM output data and output of calculated indices
nobackup='/nobackup/users/stepanov/'

# Precip (non-bas corrected)
in_path_RCM_tasmax_nbc_50km=nobackup+"CLIPC/Model_data/no_bias_corr/EUR-44/"+experiment+"/day/tasmax/SMHI/all_models/"
out_path_RCM_tasmax_nbc_50km=nobackup+"icclim_indices_v4.2.3/EUR-44/"+experiment+"/tasmax_no_bc/"

# =====================================================================================================

# Every RCM output file has predictable root name (specific to resolution!)
# ==> Construct data file names


#7/9 models. 2 more below in separate FOR loops.
# models_list_50km = ['CCCma-CanESM2','CNRM-CERFACS-CNRM-CM5','NCC-NorESM1-M',
#                     'MPI-M-MPI-ESM-LR','IPSL-IPSL-CM5A-MR','MIROC-MIROC5',
#                     'NOAA-GFDL-GFDL-ESM2M','CSIRO-QCCCE-CSIRO-Mk3-6-0']
	
# # =========================================================================
# # Processing periods

# # Base period
# base_dt1 = datetime.datetime(1971,01,01)
# base_dt2 = datetime.datetime(2000,12,31)

# # Analysis period 
# yy_dt1=1970
# mm_dt1=01
# dd_dt1=01
# #
# yy_dt2=2005
# mm_dt2=12
# dd_dt2=31
# #
# dt1 = datetime.datetime(yy_dt1,mm_dt1,dd_dt1)
# dt2 = datetime.datetime(yy_dt2,mm_dt2,dd_dt2)
# # =========================================================================


# # Important!
# # =========================================================================
# # Declare which indices you want to calculate using lists
# indice_list_pp = ['ID','SU','TX']  
# # Counting  : 'ID','SU','TX','TX90p'
# #indice_pp = 'RR1'
# # =========================================================================


# for model in models_list_50km:


# 	#  New root for non-bias corrected (!nbc!) files:
# 	tasmax_nbc_file_root_hist = "tasmax_EUR-44_"+model+"_historical_r1i1p1_SMHI-RCA4_v1_day_"
# 	tasmax_nbc_file_root_proj = "tasmax_EUR-44_"+model+"_"+experiment+"_r1i1p1_SMHI-RCA4_v1_day_"


# 	# Explicit list
# 	files_tasmax_nbc_50km = [in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_hist+"19660101-19701231.nc",
# 	                     in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_hist+"19710101-19751231.nc",
# 		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_hist+"19760101-19801231.nc",
# 		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_hist+"19810101-19851231.nc",
# 						 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_hist+"19860101-19901231.nc",
# 		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_hist+"19910101-19951231.nc",
# 		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_hist+"19960101-20001231.nc",
# 		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_hist+"20010101-20051231.nc",
# 		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20060101-20101231.nc",
# 		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20110101-20151231.nc",
# 			             in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20160101-20201231.nc",
# 			             in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20210101-20251231.nc",
# 		 	             in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20260101-20301231.nc",
# 			             in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20310101-20351231.nc",
# 			             in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20360101-20401231.nc",
# 		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20410101-20451231.nc",
# 			             in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20460101-20501231.nc",
# 			             in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20510101-20551231.nc",
# 			             in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20560101-20601231.nc",
# 			             in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20610101-20651231.nc",
# 			             in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20660101-20701231.nc",
# 		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20710101-20751231.nc",
# 		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20760101-20801231.nc",
# 		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20810101-20851231.nc",
# 		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20860101-20901231.nc",
# 		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20910101-20951231.nc",
# 		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20960101-21001231.nc"]


# 	print 'All input Model files:', files_tasmax_nbc_50km   # sep='\n'


# # =========================================================================
# # Calculate actual indices: ICCLIM syntax only
# # =========================================================================

# 	for indice_pp in indice_list_pp:
# 		print
# 		print 'Now calculating indice', indice_pp,':'
# 		print 'Using the model', model
# 		print

# 		# Build output file name construction phase
# 		# begin
# 		year_dt1=str(yy_dt1)
# 		month_dt1=str(mm_dt1).zfill(2)
# 		day_dt1=str(dd_dt1).zfill(2)
# 		# end
# 		year_dt2=str(yy_dt2)
# 		month_dt2=str(mm_dt2)
# 		day_dt2=str(dd_dt2)


#         # ----------------------------------------------------------------
# 		# Pre-change or rr1 indice into r1m when writing output file:
# 		indice_pp_fout=indice_pp
# 		print "indice_pp_fout is: ",indice_pp_fout

# 		if indice_pp == 'RR1':
#     			indice_pp_fout='R1MM' 
#     		else:
#     			indice_pp_fout=indice_pp
# 		print "new indice_pp_fout is: ",indice_pp_fout 

# 		#quit()
#         # ----------------------------------------------------------------
#         # Pre-change of 
#         # model name in output file for models:
#         # indice into r1m when writing output file:
#         #
#         # NCC-NorESM1-M --> NorESM1-M
#         # MIROC-MIROC5 --> MIROC5

# 		model_fout=model
# 		print "input model_fout is: ",model

# 		if model == 'NCC-NorESM1-M': model_fout='NorESM1-M' 
#     		elif model == 'MIROC-MIROC5': model_fout='MIROC5'
#     		elif model == 'CNRM-CERFACS-CNRM-CM5': model_fout='CNRM-CM5'
#     		elif model == 'MPI-M-MPI-ESM-LR': model_fout='MPI-ESM-LR'
#     		elif model == 'IPSL-IPSL-CM5A-MR': model_fout='IPSL-CM5A-MR'
#     		elif model == 'NOAA-GFDL-GFDL-ESM2M': model_fout='GFDL-ESM2M'
#     		elif model == 'CSIRO-QCCCE-CSIRO-Mk3-6-0': model_fout='CSIRO-Mk3-6-0'
#     		else: model_fout=model
# 		print "new model_fout is: ",model_fout 

# # 		#quit()


# 		# ====================== NON-BIAS Corrected ====================== #

# 		indice_out_name = out_path_RCM_tasmax_nbc_50km+\
# 		                indice_pp_fout.lower()+\
# 		                "_icclim-4-2-3"+\
# 		                "_KNMI_"+\
# 		                model_fout+\
# 		                "_historical"+\
# 		                "_r1i1p1_"+\
# 		                "SMHI-RCA4_v1_EUR-44_"+\
# 		                "yr_"+\
# 		                year_dt1+month_dt1+\
# 		                day_dt1+\
# 		                "-"+\
# 		                year_dt2+month_dt2+day_dt2+\
# 		                '.nc'

# #"_historical"+\
# #"_rcp45"+\
# #"_rcp85"+\


# 		print 'Going into output file:', indice_out_name
# 		print
		
# 		icclim.indice(indice_name=indice_pp,
# 		    	      in_files=files_tasmax_nbc_50km,
# 		        	  var_name='tasmax', 
# 	               	  slice_mode='year', 
# 	        	      time_range=[dt1,dt2], 
# 	           	      base_period_time_range=[base_dt1, base_dt2],
# 	               	  out_file=indice_out_name,
# 	                  callback=callback.defaultCallback2)



#=================================================================================================
# # HadGEM mode (period ends iwth yyyy1230!)

# models_list_50km_HadGEM = ['MOHC-HadGEM2-ES']

# # Important!
# # =========================================================================
# # Declare which indices you want to calculate using lists
# indice_list_pp = ['ID','SU','TX']
# # Counting  : 'ID','SU','TX','TX90p'
# #indice_pp = 'RR1'
# # =========================================================================


# # =========================================================================
# # Processing periods (specific to HadGem for the missing 31.12.)

# # Base period
# base_dt1_HadGEM = datetime.datetime(1971,01,01)
# base_dt2_HadGEM = datetime.datetime(2000,12,30)

# # Analysis period
# yy_dt1=1970
# mm_dt1=01
# dd_dt1=01
# #
# yy_dt2=2005
# mm_dt2=12  # 12 for historical, 11 for projections :)
# dd_dt2=30
# #
# dt1_HadGEM = datetime.datetime(yy_dt1,mm_dt1,dd_dt1)
# dt2_HadGEM = datetime.datetime(yy_dt2,mm_dt2,dd_dt2)

# # =========================================================================


# for model in models_list_50km_HadGEM:

# 	#  New root for non-bias corrected (!nbc!) files:
# 	tasmax_nbc_file_root_hist = "tasmax_EUR-44_"+model+"_historical_r1i1p1_SMHI-RCA4_v1_day_"
# 	tasmax_nbc_file_root_proj = "tasmax_EUR-44_"+model+"_"+experiment+"_r1i1p1_SMHI-RCA4_v1_day_"

# 	# Explicit list
# 	files_tasmax_nbc_50km = [in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_hist+"19660101-19701230.nc",
# 		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_hist+"19710101-19751230.nc",
# 		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_hist+"19760101-19801230.nc",
# 	                     in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_hist+"19810101-19851230.nc",
# 						 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_hist+"19860101-19901230.nc",
# 		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_hist+"19910101-19951230.nc",
# 		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_hist+"19960101-20001230.nc",
# 		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_hist+"20010101-20051230.nc",
# 		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20060101-20101230.nc",
# 		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20110101-20151230.nc",
# 			             in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20160101-20201230.nc",
# 			             in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20210101-20251230.nc",
# 		 	             in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20260101-20301230.nc",
# 			             in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20310101-20351230.nc",
# 			             in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20360101-20401230.nc",
# 		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20410101-20451230.nc",
# 			             in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20460101-20501230.nc",
# 			             in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20510101-20551230.nc",
# 			             in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20560101-20601230.nc",
# 			             in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20610101-20651230.nc",
# 			             in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20660101-20701230.nc",
# 		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20710101-20751230.nc",
# 		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20760101-20801230.nc",
# 		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20810101-20851230.nc",
# 		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20860101-20901230.nc",
# 		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20910101-20951230.nc",
# 		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20960101-20991230.nc"]

# 	print ('All input Model files:', files_tasmax_nbc_50km)

# # =========================================================================
# # Calculate actual indices: ICCLIM syntax only
# # =========================================================================

# 	for indice_pp in indice_list_pp:
# 		print
# 		print 'Now calculating indice', indice_pp,':'
# 		print 'Using the model', model
# 		print

# 		# Build output file name construction phase
# 		# begin
# 		year_dt1=str(yy_dt1)
# 		month_dt1=str(mm_dt1).zfill(2)
# 		day_dt1=str(dd_dt1).zfill(2)
# 		# end
# 		year_dt2=str(yy_dt2)
# 		month_dt2=str(mm_dt2)
# 		day_dt2=str(dd_dt2)

#         # ----------------------------------------------------------------
# 		# Pre-change or rr1 indice into r1m when writing output file:
# 		indice_pp_fout=indice_pp
# 		print "indice_pp_fout is: ",indice_pp_fout

# 		if indice_pp == 'RR1':
#     			indice_pp_fout='R1MM' 
#     		else:
#     			indice_pp_fout=indice_pp
# 		print "new indice_pp_fout is: ",indice_pp_fout 

# 		#quit()
#         # ----------------------------------------------------------------
#         # Pre-change of 
#         # model name in output file for models:
#         # indice into r1m when writing output file:
#         #
#         # NCC-NorESM1-M --> NorESM1-M
#         # MIROC-MIROC5 --> MIROC5

# 		model_fout=model
# 		print "input model_fout is: ",model

# 		if model == 'NCC-NorESM1-M': model_fout='NorESM1-M' 
#     		elif model == 'MIROC-MIROC5': model_fout='MIROC5'
#     		elif model == 'CNRM-CERFACS-CNRM-CM5': model_fout='CNRM-CM5'
#     		elif model == 'MPI-M-MPI-ESM-LR': model_fout='MPI-ESM-LR'
#     		elif model == 'IPSL-IPSL-CM5A-MR': model_fout='IPSL-CM5A-MR'
#     		elif model == 'NOAA-GFDL-GFDL-ESM2M': model_fout='GFDL-ESM2M'
#     		elif model == 'CSIRO-QCCCE-CSIRO-Mk3-6-0': model_fout='CSIRO-Mk3-6-0'
#     		else: model_fout=model
# 		print "new model_fout is: ",model_fout 

# # 		#quit()


# #Build output file name construction phase
# 		# ====================== NON-BIAS Corrected ====================== #

# 		indice_out_name = out_path_RCM_tasmax_nbc_50km+\
# 		                indice_pp_fout.lower()+\
# 		                "_icclim-4-2-3"+\
# 		                "_KNMI_"+\
# 		                model[5:15]+\
# 		                "_historical"+\
# 		                "_r1i1p1_"+\
# 		                "SMHI-RCA4_v1_EUR-44_"+\
# 		                "yr_"+\
# 		                year_dt1+month_dt1+\
# 		                day_dt1+\
# 		                "-"+\
# 		                year_dt2+month_dt2+day_dt2+\
# 		                '.nc'

# #"_historical"+\
# # #"_rcp45"+\
# # #"_rcp85"+\

# 		print 'Going into output file:', indice_out_name
# 		print
	
# 		icclim.indice(indice_name=indice_pp,
# 	    	          in_files=files_tasmax_nbc_50km,
# 	        	      var_name='tasmax', 
#               	 	  slice_mode='year', 
#       	        	  time_range=[dt1_HadGEM,dt2_HadGEM], 
#         	          #ignore_Feb29th=True,
#            	    	  base_period_time_range=[base_dt1_HadGEM, base_dt2_HadGEM],
#                		  out_file=indice_out_name,
#                 	  callback=callback.defaultCallback2)


#=================================================================================================
# EC Earth model (r12i1pi in file name!)
models_list_50km_EC_EARTH = ['ICHEC-EC-EARTH']


# Important!
# =========================================================================
# Declare which indices you want to calculate using lists
indice_list_pp = ['ID','SU','TX']   
# Counting  : 'ID','SU','TX'
#indice_pp = 'RR1'
# =========================================================================


# =========================================================================
# Processing periods

# Base period
base_dt1 = datetime.datetime(1971,01,01)
base_dt2 = datetime.datetime(2000,12,31)

# Analysis period
yy_dt1=1970
mm_dt1=01
dd_dt1=01
#
yy_dt2=2005
mm_dt2=12
dd_dt2=31
#
dt1 = datetime.datetime(yy_dt1,mm_dt1,dd_dt1)
dt2 = datetime.datetime(yy_dt2,mm_dt2,dd_dt2)
# =========================================================================


for model in models_list_50km_EC_EARTH:

	#  New root for non-bias corrected (!nbc!) files:
	tasmax_nbc_file_root_hist = "tasmax_EUR-44_"+model+"_historical_r12i1p1_SMHI-RCA4_v1_day_"
	tasmax_nbc_file_root_proj = "tasmax_EUR-44_"+model+"_"+experiment+"_r12i1p1_SMHI-RCA4_v1_day_"

	# Explicit list
	files_tasmax_nbc_50km = [in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_hist+"19660101-19701231.nc",
		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_hist+"19710101-19751231.nc",
		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_hist+"19760101-19801231.nc",
	                     in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_hist+"19810101-19851231.nc",
						 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_hist+"19860101-19901231.nc",
		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_hist+"19910101-19951231.nc",
		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_hist+"19960101-20001231.nc",
		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_hist+"20010101-20051231.nc",
		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20060101-20101231.nc",
		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20110101-20151231.nc",
			             in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20160101-20201231.nc",
			             in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20210101-20251231.nc",
		 	             in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20260101-20301231.nc",
			             in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20310101-20351231.nc",
			             in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20360101-20401231.nc",
		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20410101-20451231.nc",
			             in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20460101-20501231.nc",
			             in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20510101-20551231.nc",
			             in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20560101-20601231.nc",
			             in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20610101-20651231.nc",
			             in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20660101-20701231.nc",
		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20710101-20751231.nc",
		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20760101-20801231.nc",
		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20810101-20851231.nc",
		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20860101-20901231.nc",
		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20910101-20951231.nc",
		                 in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20960101-21001231.nc"]

	print 'All input Model files:', files_tasmax_nbc_50km


# =========================================================================
# Calculate actual indices: ICCLIM syntax only
# =========================================================================

	for indice_pp in indice_list_pp:
		print
		print 'Now calculating indice', indice_pp,':'
		print 'Using the model', model
		print

		#Build output file name construction phase
		year_dt1=str(yy_dt1)
		month_dt1=str(mm_dt1).zfill(2)
		day_dt1=str(dd_dt1).zfill(2)
		# end
		year_dt2=str(yy_dt2)
		month_dt2=str(mm_dt2)
		day_dt2=str(dd_dt2)

        
        # ----------------------------------------------------------------
		# Pre-change or rr1 indice into r1m when writing output file:
		indice_pp_fout=indice_pp
		print "indice_pp_fout is: ",indice_pp_fout

		if indice_pp == 'RR1':
    			indice_pp_fout='R1MM' 
    		else:
    			indice_pp_fout=indice_pp
		print "new indice_pp_fout is: ",indice_pp_fout 

		#quit()
        # ----------------------------------------------------------------
        # Pre-change of 
        # model name in output file for models:
        # indice into r1m when writing output file:
        #
        # NCC-NorESM1-M --> NorESM1-M
        # MIROC-MIROC5 --> MIROC5

		model_fout=model
		print "input model_fout is: ",model

		if model == 'NCC-NorESM1-M': model_fout='NorESM1-M' 
    		elif model == 'MIROC-MIROC5': model_fout='MIROC5'
    		elif model == 'CNRM-CERFACS-CNRM-CM5': model_fout='CNRM-CM5'
    		elif model == 'MPI-M-MPI-ESM-LR': model_fout='MPI-ESM-LR'
    		elif model == 'IPSL-IPSL-CM5A-MR': model_fout='IPSL-CM5A-MR'
    		elif model == 'NOAA-GFDL-GFDL-ESM2M': model_fout='GFDL-ESM2M'
    		elif model == 'CSIRO-QCCCE-CSIRO-Mk3-6-0': model_fout='CSIRO-Mk3-6-0'
    		else: model_fout=model
		print "new model_fout is: ",model_fout 

# 		#quit()


		# ====================== NON-BIAS Corrected ====================== #
		# W/ & W/O base period
		indice_out_name = out_path_RCM_tasmax_nbc_50km+\
		                indice_pp_fout.lower()+\
		                "_icclim-4-2-3"+\
		                "_KNMI_"+\
		                model[6:14]+\
		                "_historical"+\
		                "_r12i1p1_"+\
		                "SMHI-RCA4_v1_EUR-44_"+\
		                "yr_"+\
		                year_dt1+month_dt1+\
		                day_dt1+\
		                "-"+\
		                year_dt2+month_dt2+day_dt2+\
		                '.nc'

#"_historical"+\
# #"_rcp45"+\
# #"_rcp85"+\


		print 'Going into output file:', indice_out_name
		print

		# # =========================================================================
	
		icclim.indice(indice_name=indice_pp,
	    	          in_files=files_tasmax_nbc_50km,
	        	      var_name='tasmax', 
               	 	  slice_mode='year', 
        	          time_range=[dt1,dt2], 
           	      	  base_period_time_range=[base_dt1, base_dt2],
               	  	  out_file=indice_out_name, 
                	  callback=callback.defaultCallback2)



#Done with calculations for all 9/9 models

print
print 'Done!'
print

quit()
