

# Import the old tracking id from the RCM file for period 19660101-19701231,
# as it is the first used file to create historical indices:
# (e.g. tasmin_EUR-44_IPSL-IPSL-CM5A-MR_historical_r1i1p1_SMHI-RCA4_v1_day_19660101-19701231.nc)

#track_GCM_indice=$(


import netCDF4
from netCDF4 import Dataset
import ctypes
import icclim
import datetime
import icclim.util.callback as callback
#cb = callback.defaultCallback
import fnmatch
import os



print
#print '<<Loaded python modules>>'
print

# =====================================================================================================
# Define some paths

experiments_list = ['rcp45','rcp85']

for experiment in experiments_list:

	# RCM output data and output of calculated indices
	nobackup='/net/pc150394/nobackup/users/stepanov/'

	# TMAX (non-bas corrected)

	in_path_RCM_tasmax_nbc_50km=nobackup+"CLIPC/Model_data/no_bias_corr/EUR-44/"+experiment+"/day/tasmax/SMHI/all_models/"
	out_path_RCM_tasmax_nbc_50km=nobackup+"icclim_indices_v4.2.3_seapoint_fixed/EUR-44/"+experiment+"/tasmax_no_bc/"
	# output path still for test only

	# =====================================================================================================

	# Every RCM output file has predictable root name (specific to resolution!)
	# ==> Construct data file names


	#8/10 models. 2 more below in separate FOR loops.
	models_list_50km = ['CCCma-CanESM2','CNRM-CERFACS-CNRM-CM5','NCC-NorESM1-M',
	                    'MPI-M-MPI-ESM-LR','IPSL-IPSL-CM5A-MR','MIROC-MIROC5',
	                    'NOAA-GFDL-GFDL-ESM2M','CSIRO-QCCCE-CSIRO-Mk3-6-0']

	#models_list_50km = ['CCCma-CanESM2']
	#models_list_50km = ['CNRM-CERFACS-CNRM-CM5']
	                    


	for model in models_list_50km:


		# CONSTRUCT RCM FILE NAMES
		#  New root for non-bias corrected (!nbc!) files:
		tasmax_nbc_file_root_hist = "tasmax_EUR-44_"+model+"_historical_r1i1p1_SMHI-RCA4_v1_day_"
		tasmax_nbc_file_root_proj = "tasmax_EUR-44_"+model+"_"+experiment+"_r1i1p1_SMHI-RCA4_v1_day_"


		# Explicit list
		files_tasmax_nbc_50km_hist = in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_hist+"19660101-19701231.nc"
		files_tasmax_nbc_50km_proj = in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20060101-20101231.nc"


		# Tell me which files you imported
		print 'Historical input Model files:', files_tasmax_nbc_50km_hist   # sep='\n'
		print 'Projection input Model files:', files_tasmax_nbc_50km_proj   # sep='\n'


		# CONSTRUCT INDICES FILE NAMES

		# Create datasets from netCDF files
		nc_in_hist = Dataset(files_tasmax_nbc_50km_hist,'r')
		nc_in_proj = Dataset(files_tasmax_nbc_50km_proj,'r')


		# Print current GCM tracking id

	# Historical
		print
		print
		print "For historical model:", model
		print "Historical tracking id", nc_in_hist.tracking_id
		print

		for file_hist in os.listdir(out_path_RCM_tasmax_nbc_50km):

	        # ----------------------------------------------------------------
	        # Pre-change of 
	        # model name in output file for models:
	        # indice into r1m when writing output file:
	        #
	        # NCC-NorESM1-M --> NorESM1-M
	        # MIROC-MIROC5 --> MIROC5

			model_fout=model
			#print "input model_fout is: ",model

			if model == 'NCC-NorESM1-M': model_fout='NorESM1-M' 
	    		elif model == 'MIROC-MIROC5': model_fout='MIROC5'
	    		elif model == 'CNRM-CERFACS-CNRM-CM5': model_fout='CNRM-CM5'
	    		elif model == 'MPI-M-MPI-ESM-LR': model_fout='MPI-ESM-LR'
	    		elif model == 'IPSL-IPSL-CM5A-MR': model_fout='IPSL-CM5A-MR'
	    		elif model == 'NOAA-GFDL-GFDL-ESM2M': model_fout='GFDL-ESM2M'
	    		elif model == 'CSIRO-QCCCE-CSIRO-Mk3-6-0': model_fout='CSIRO-Mk3-6-0'
	    		else: model_fout=model
			#print "new model_fout is: ",model_fout 

			#if fnmatch.fnmatch(file_hist, '*CCCma-CanESM2_historical*'):
			if fnmatch.fnmatch(file_hist, "*"+model_fout+"_historical*"):
			#if fnmatch.fnmatch(file_hist, "*historical*"):
				print "Indice where new historical invar_tracking_id goes is:", file_hist
				#print
				#print '%s' % (model)

				# Create Dataset from these files
				nc_indice_tasmax_hist = Dataset(out_path_RCM_tasmax_nbc_50km+file_hist,'a')
				# Insert invar_tracking_id global attributed with value on the right
				# (imported RCM tracking id from the single RCM file above)
				#nc_indice_tasmax_hist.comment='fun'
				nc_indice_tasmax_hist.invar_tracking_id=nc_in_hist.tracking_id
				#nc_in_hist.comment = 'test'  
				#nc_in_hist.invar_tracking_id_test = 'test'  


	# Projections
		print
		print
		print "For projections model:", model
		print "Projection tracking id", nc_in_proj.tracking_id
		print
		print


		for file_proj in os.listdir(out_path_RCM_tasmax_nbc_50km):

	        # ----------------------------------------------------------------
	        # Pre-change of 
	        # model name in output file for models:
	        # indice into r1m when writing output file:
	        #
	        # NCC-NorESM1-M --> NorESM1-M
	        # MIROC-MIROC5 --> MIROC5

			model_fout=model
			#print "input model_fout is: ",model

			if model == 'NCC-NorESM1-M': model_fout='NorESM1-M' 
	    		elif model == 'MIROC-MIROC5': model_fout='MIROC5'
	    		elif model == 'CNRM-CERFACS-CNRM-CM5': model_fout='CNRM-CM5'
	    		elif model == 'MPI-M-MPI-ESM-LR': model_fout='MPI-ESM-LR'
	    		elif model == 'IPSL-IPSL-CM5A-MR': model_fout='IPSL-CM5A-MR'
	    		elif model == 'NOAA-GFDL-GFDL-ESM2M': model_fout='GFDL-ESM2M'
	    		elif model == 'CSIRO-QCCCE-CSIRO-Mk3-6-0': model_fout='CSIRO-Mk3-6-0'
	    		else: model_fout=model
			#print "new model_fout is: ",model_fout 


			if fnmatch.fnmatch(file_proj, "*"+model_fout+"_"+experiment+"*"):
				print "Indice where new projection invar_tracking_id goes is:", file_proj
				print
				# Create Dataset from these files
				nc_indice_tasmax_proj = Dataset(out_path_RCM_tasmax_nbc_50km+file_proj,'a')
				# Insert invar_tracking_id global attributed with value on the right
				# (imported RCM tracking id from the single RCM file above)
				#nc_indice_tasmax_hist.comment='fun'
				nc_indice_tasmax_proj.invar_tracking_id=nc_in_proj.tracking_id




	# Had-GEM

	models_list_50km_HadGEM = ['MOHC-HadGEM2-ES']

	for model in models_list_50km_HadGEM:


		# CONSTRUCT RCM FILE NAMES
		#  New root for non-bias corrected (!nbc!) files:
		tasmax_nbc_file_root_hist = "tasmax_EUR-44_"+model+"_historical_r1i1p1_SMHI-RCA4_v1_day_"
		tasmax_nbc_file_root_proj = "tasmax_EUR-44_"+model+"_"+experiment+"_r1i1p1_SMHI-RCA4_v1_day_"


		# Explicit list
		files_tasmax_nbc_50km_hist = in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_hist+"19660101-19701230.nc"
		files_tasmax_nbc_50km_proj = in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20060101-20101230.nc"


		# Tell me which files you imported
		print 'Historical input Model files:', files_tasmax_nbc_50km_hist   # sep='\n'
		print 'Projection input Model files:', files_tasmax_nbc_50km_proj   # sep='\n'


		# CONSTRUCT INDICES FILE NAMES

		# Create datasets from netCDF files
		nc_in_hist = Dataset(files_tasmax_nbc_50km_hist,'r')
		nc_in_proj = Dataset(files_tasmax_nbc_50km_proj,'r')


		# Print current GCM tracking id

	# Historical
		print
		print
		print "For historical model:", model
		print "Historical tracking id", nc_in_hist.tracking_id
		print

		for file_hist in os.listdir(out_path_RCM_tasmax_nbc_50km):

			#if fnmatch.fnmatch(file_hist, '*CCCma-CanESM2_historical*'):
			if fnmatch.fnmatch(file_hist, "*"+model[5:15]+"_historical*"):
			#if fnmatch.fnmatch(file_hist, "*historical*"):
				print "Indice where new historical invar_tracking_id goes is:", file_hist
				#print
				#print '%s' % (model)

				# Create Dataset from these files
				nc_indice_tasmax_hist = Dataset(out_path_RCM_tasmax_nbc_50km+file_hist,'a')
				# Insert invar_tracking_id global attributed with value on the right
				# (imported RCM tracking id from the single RCM file above)
				#nc_indice_tasmax_hist.comment='fun'
				nc_indice_tasmax_hist.invar_tracking_id=nc_in_hist.tracking_id
				#nc_in_hist.comment = 'test'  
				#nc_in_hist.invar_tracking_id_test = 'test'  


	# Projections
		print
		print
		print "For projections model:", model
		print "Projection tracking id", nc_in_proj.tracking_id
		print
		print


		for file_proj in os.listdir(out_path_RCM_tasmax_nbc_50km):

			if fnmatch.fnmatch(file_proj, "*"+model[5:15]+"_"+experiment+"*"):
				print "Indice where new projection invar_tracking_id goes is:", file_proj
				# Create Dataset from these files
				nc_indice_tasmax_proj = Dataset(out_path_RCM_tasmax_nbc_50km+file_proj,'a')
				# Insert invar_tracking_id global attributed with value on the right
				# (imported RCM tracking id from the single RCM file above)
				#nc_indice_tasmax_hist.comment='fun'
				nc_indice_tasmax_proj.invar_tracking_id=nc_in_proj.tracking_id


	EC-EARTH

	models_list_50km_EC_EARTH = ['ICHEC-EC-EARTH']

	for model in models_list_50km_EC_EARTH:


		# CONSTRUCT RCM FILE NAMES
		#  New root for non-bias corrected (!nbc!) files:
		tasmax_nbc_file_root_hist = "tasmax_EUR-44_"+model+"_historical_r12i1p1_SMHI-RCA4_v1_day_"
		tasmax_nbc_file_root_proj = "tasmax_EUR-44_"+model+"_"+experiment+"_r12i1p1_SMHI-RCA4_v1_day_"


		# Explicit list
		files_tasmax_nbc_50km_hist = in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_hist+"19660101-19701231.nc"
		files_tasmax_nbc_50km_proj = in_path_RCM_tasmax_nbc_50km+tasmax_nbc_file_root_proj+"20060101-20101231.nc"


		# Tell me which files you imported
		print 'Historical input Model files:', files_tasmax_nbc_50km_hist   # sep='\n'
		print 'Projection input Model files:', files_tasmax_nbc_50km_proj   # sep='\n'


		# CONSTRUCT INDICES FILE NAMES

		# Create datasets from netCDF files
		nc_in_hist = Dataset(files_tasmax_nbc_50km_hist,'r')
		nc_in_proj = Dataset(files_tasmax_nbc_50km_proj,'r')


		# Print current GCM tracking id

	# Historical
		print
		print
		print "For historical model:", model
		print "Historical tracking id", nc_in_hist.tracking_id
		print

		for file_hist in os.listdir(out_path_RCM_tasmax_nbc_50km):

			#if fnmatch.fnmatch(file_hist, '*CCCma-CanESM2_historical*'):
			if fnmatch.fnmatch(file_hist, "*"+model[6:14]+"_historical*"):
			#if fnmatch.fnmatch(file_hist, "*historical*"):
				print "Indice where new historical invar_tracking_id goes is:", file_hist
				#print
				#print '%s' % (model)

				# Create Dataset from these files
				nc_indice_tasmax_hist = Dataset(out_path_RCM_tasmax_nbc_50km+file_hist,'a')
				# Insert invar_tracking_id global attributed with value on the right
				# (imported RCM tracking id from the single RCM file above)
				#nc_indice_tasmax_hist.comment='fun'
				nc_indice_tasmax_hist.invar_tracking_id=nc_in_hist.tracking_id
				#nc_in_hist.comment = 'test'  
				#nc_in_hist.invar_tracking_id_test = 'test'  


	# Projections
		print
		print
		print "For projections model:", model
		print "Projection tracking id", nc_in_proj.tracking_id
		print
		print


		for file_proj in os.listdir(out_path_RCM_tasmax_nbc_50km):

			if fnmatch.fnmatch(file_proj, "*"+model[6:14]+"_"+experiment+"*"):
				print "Indice where new projection invar_tracking_id goes is:", file_proj
				# Create Dataset from these files
				nc_indice_tasmax_proj = Dataset(out_path_RCM_tasmax_nbc_50km+file_proj,'a')
				# Insert invar_tracking_id global attributed with value on the right
				# (imported RCM tracking id from the single RCM file above)
				#nc_indice_tasmax_hist.comment='fun'
				nc_indice_tasmax_proj.invar_tracking_id=nc_in_proj.tracking_id



quit()