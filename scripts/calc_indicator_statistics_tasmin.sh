#!/bin/bash

# Executable bash script

# Import all RCM ensemble members and calculate median/mean 
# with a correct DRS file name

# Update list
#
# 21.06.2016. I.S. Adding new DRS file name output as agreed with Juliane
# 25.07.2016. I.S. Chaged paths for indices calculated with icclim423 and new 
#                  and final indices list for CLIP-C
# 25.07.2016. I.S. Split of script into 4, according to the RCM input variable
# 04.08.2016. I.S. Added the append_rename_vars_nc_nco script part into this one.
# -------------------------------------------------------------------------

# Facets constructing ensemble indices files:
# <rx1day>_<icclim-4-2-3>_<KNMI>_<ens-multiModel-20p-rcp45>_<yr>_<20060101-20991231>.nc


# Define some pahts
# =========================================================================
# According to variable type: TASMIN

# Post-processing file: contains rlat,rlon to put back into ensemble statistics files
file_with_rlon_rlat='/nobackup/users/stepanov/icclim_indices_v4.2.3/EUR-44/rcp45/pr/r95p_icclim-4-2-3_KNMI_HadGEM2-ES_rcp45_r1i1p1_SMHI-RCA4_v1_EUR-44_SMHI-DBS43_EOBS10_bcref-1981-2010_yr_20060101-20991130.nc'


# Indice category & experiment
# -------------------
TASMIN_indices="fd tr tn"
#TASMIN_indices="fd"
experiments="rcp45 rcp85"
statistics="median 20p 80p"

for experiment in $experiments; do

	indices_path='/nobackup/users/stepanov/icclim_indices_v4.2.3_seapoint_metadata_fixed/EUR-44/'

	# Input files
	# =========================================================================

	# Bias corrected files
	path_indices_tasmin=$indices_path/BC/tasmin/
	# non-Bias corrected files
	path_indices_tasmin_nobias=$indices_path/No_BC/tasmin/


	echo
	echo "Bias corrected INPUT paths:"
	echo "TASMIN indice file path is: $path_indices_tasmin"
	echo

	echo
	echo "Non-Bias corrected INPUT paths:"
	echo "TASMIN indice file path is: $path_indices_tasmin_nobias"
	echo
	# =========================================================================


	# Ensemble statistics OUTPUT paths
	# =========================================================================

	# Bias corrected files
	path_indices_ens_tasmin=$indices_path/BC/ens_multiModel_tasmin/
	# non-Bias corrected files
	path_indices_ens_tasmin_nobias=$indices_path/No_BC/ens_multiModel_tasmin_no_bc/


	echo
	echo "Bias corrected OUTPUT paths:"
	echo "TASMIN ensemble indice file path: $path_indices_ens_tasmin"

	echo
	echo "Non-Bias corrected OUTPUT paths:"
	echo "TASMIN ensemble indice file path: $path_indices_ens_tasmin_nobias"
	echo
	# =========================================================================


	# Take indices parameters from the list above
	for indice in $TASMIN_indices

	# --------------------------------------------

	# Facets constructing ensemble indices files, to be confirmed by Ruth
	# <rx1day>_<icclim-4-2-3>_<KNMI>_<ens-multiModel-20p-rcp45>_<yr>_<20060101-20991231>.nc

	# --------------------------------------------
	# Actual calculation

	do

 		echo
 		echo "-----"
 		echo "Calculating ensemble statistics for indice $indice and experiment $experiment"
 		echo "-----"
 		echo
	    
		cd $path_indices_tasmin/

		echo
		echo 'Where am i now? Should be TASMIN Bias Corrected' 
		echo
		pwd

		#TASMIN Bias corrected

		#PROJECTIONS: 2006-2099
		#----------------------------------------------------------
		
 		  # MEDIAN:
		cdo enspctl,50 $(echo ${indice})*$experiment*20060101-2099* \
		$path_indices_ens_tasmin/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-median-$experiment-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_20060101-20991231.nc
	 	  # 20 PERCENTILE:
	 	cdo enspctl,20 $(echo ${indice})*$experiment*20060101-2099* \
	 	$path_indices_ens_tasmin/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-20p-$experiment-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_20060101-20991231.nc
          # 80 PERCENTILE:
	 	cdo enspctl,80 $(echo ${indice})*$experiment*20060101-2099* \
	 	$path_indices_ens_tasmin/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-80p-$experiment-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_20060101-20991231.nc
 

        # HISTORICAL: 1970-2005
        # ----------------------------------------------------------
        
          # MEDIAN:
 		cdo -O enspctl,50 $(echo ${indice})*19700101-2005* \
 		$path_indices_ens_tasmin/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-median-historical-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_19700101-20051231.nc
          # 20 PERCENTILE:
 		cdo -O enspctl,20 $(echo ${indice})*19700101-2005* \
 		$path_indices_ens_tasmin/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-20p-historical-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_19700101-20051231.nc
          # 80 PERCENTILE:
 		cdo -O enspctl,80 $(echo ${indice})*19700101-2005* \
 		$path_indices_ens_tasmin/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-80p-historical-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_19700101-20051231.nc

 		# ----------------------------------------------------------
		
		# Fix rlon,rlat,rot.grid att.
 		for stat in $statistics
 		do

 		echo
 		echo "-----"
 		echo "NCO patching PROJECTIONS ensemble statistics for indice $indice, experiment $experiment and statistic $stat"
 		echo "-----"
 		echo


 		# projections
 		ncks -A -v rlat,rlon,rotated_pole $(echo ${file_with_rlon_rlat}) \
 		$path_indices_ens_tasmin/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-$experiment-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_20060101-20991231.nc
 		# Here a midstep is needed to rename rlon,rlat-->x,y
		ncrename -v rlat,y $path_indices_ens_tasmin/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-$experiment-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_20060101-20991231.nc
		ncrename -v rlon,x $path_indices_ens_tasmin/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-$experiment-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_20060101-20991231.nc
		# Add attribute to the variable
		ncatted -O -h -a grid_mapping,$(echo ${indice}),c,c,"rotated_pole" $path_indices_ens_tasmin/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-$experiment-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_20060101-20991231.nc
		ncatted -O -a source_data_id,global,o,c,"ens-multiModel-"$stat"-"$experiment"-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010" -h $path_indices_ens_tasmin/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-$experiment-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_20060101-20991231.nc
		ncatted -O -a history_of_appended_files,global,d,, -h $path_indices_ens_tasmin/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-$experiment-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_20060101-20991231.nc
		ncatted -O -a NCO,global,d,, -h $path_indices_ens_tasmin/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-$experiment-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_20060101-20991231.nc
		ncatted -O -a CDO,global,d,, -h $path_indices_ens_tasmin/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-$experiment-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_20060101-20991231.nc
		# Make history attribute clean
		ncatted -h -a history,global,d,, $path_indices_ens_tasmin/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-$experiment-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_20060101-20991231.nc          # delete history
		ncatted -O -h -a history,global,c,c,' ' $path_indices_ens_tasmin/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-$experiment-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_20060101-20991231.nc   # create history

		echo
 		echo "-----"
 		echo "NCO patching HISTORICAL ensemble statistics for indice $indice, experiment $experiment and statistic $stat"
 		echo "-----"
 		echo


		# historical 	
 		ncks -A -v rlat,rlon,rotated_pole $(echo ${file_with_rlon_rlat}) \
 		$path_indices_ens_tasmin/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-historical-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_19700101-20051231.nc
 		# Here a midstep is needed to rename rlon,rlat-->x,y
		ncrename -v rlat,y $path_indices_ens_tasmin/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-historical-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_19700101-20051231.nc
		ncrename -v rlon,x $path_indices_ens_tasmin/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-historical-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_19700101-20051231.nc
		# Add attribute to the variable
		ncatted -O -h -a grid_mapping,$(echo ${indice}),c,c,"rotated_pole" $path_indices_ens_tasmin/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-historical-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_19700101-20051231.nc
		ncatted -O -a source_data_id,global,o,c,"ens-multiModel-"$stat"-historical-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010" -h $path_indices_ens_tasmin/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-historical-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_19700101-20051231.nc
		ncatted -O -a history_of_appended_files,global,d,, -h $path_indices_ens_tasmin/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-historical-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_19700101-20051231.nc
		ncatted -O -a NCO,global,d,, -h $path_indices_ens_tasmin/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-historical-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_19700101-20051231.nc
		ncatted -O -a CDO,global,d,, -h $path_indices_ens_tasmin/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-historical-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_19700101-20051231.nc
		# Make history attribute clean
		ncatted -h -a history,global,d,, $path_indices_ens_tasmin/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-historical-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_19700101-20051231.nc          # delete history
		ncatted -O -h -a history,global,c,c,' ' $path_indices_ens_tasmin/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-historical-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_19700101-20051231.nc   # create history
		done

		# ----------------------------------------------------------

 		cd $path_indices_tasmin_nobias/

 		echo
 		echo 'Where am i now? Should be TASMIN NoN-Bias Corrected' 
		echo
		pwd

 		#TASMIN NoN-Bias Corrected

		# PROJECTIONS: 2006-2099
		# ----------------------------------------------------------
		
 		  # MEDIAN:
		cdo enspctl,50 $(echo ${indice})*$experiment*20060101-2099* \
		$path_indices_ens_tasmin_nobias/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-median-$experiment-EUR-44_yr_20060101-20991231.nc
	 	  # 20 PERCENTILE:
	 	cdo enspctl,20 $(echo ${indice})*$experiment*20060101-2099* \
	 	$path_indices_ens_tasmin_nobias/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-20p-$experiment-EUR-44_yr_20060101-20991231.nc
          # 80 PERCENTILE:
	 	cdo enspctl,80 $(echo ${indice})*$experiment*20060101-2099* \
	 	$path_indices_ens_tasmin_nobias/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-80p-$experiment-EUR-44_yr_20060101-20991231.nc
 

        # HISTORICAL: 1970-2005
        # ----------------------------------------------------------
        
          # MEDIAN:
 		cdo -O enspctl,50 $(echo ${indice})*19700101-2005* \
 		$path_indices_ens_tasmin_nobias/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-median-historical-EUR-44_yr_19700101-20051231.nc
          # 20 PERCENTILE:
 		cdo -O enspctl,20 $(echo ${indice})*19700101-2005* \
 		$path_indices_ens_tasmin_nobias/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-20p-historical-EUR-44_yr_19700101-20051231.nc
          # 80 PERCENTILE:
 		cdo -O enspctl,80 $(echo ${indice})*19700101-2005* \
 		$path_indices_ens_tasmin_nobias/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-80p-historical-EUR-44_yr_19700101-20051231.nc

 		# ----------------------------------------------------------



		# Fix rlon,rlat,rot.grid att.
 		for stat in $statistics
 		do

 		echo
 		echo "-----"
 		echo "NCO patching PROJECTIONS ensemble statistics for indice $indice, experiment $experiment and statistic $stat"
 		echo "-----"
 		echo


 		# projections
 		ncks -A -v rlat,rlon,rotated_pole $(echo ${file_with_rlon_rlat}) \
 		$path_indices_ens_tasmin_nobias/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-$experiment-EUR-44_yr_20060101-20991231.nc
 		# Here a midstep is needed to rename rlon,rlat-->x,y
		ncrename -v rlat,y $path_indices_ens_tasmin_nobias/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-$experiment-EUR-44_yr_20060101-20991231.nc
		ncrename -v rlon,x $path_indices_ens_tasmin_nobias/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-$experiment-EUR-44_yr_20060101-20991231.nc
		# Add attribute to the variable
		ncatted -O -h -a grid_mapping,$(echo ${indice}),c,c,"rotated_pole" $path_indices_ens_tasmin_nobias/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-$experiment-EUR-44_yr_20060101-20991231.nc
		ncatted -O -a source_data_id,global,o,c,"ens-multiModel-"$stat"-"$experiment"-EUR-44" -h $path_indices_ens_tasmin_nobias/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-$experiment-EUR-44_yr_20060101-20991231.nc
		ncatted -O -a history_of_appended_files,global,d,, -h $path_indices_ens_tasmin_nobias/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-$experiment-EUR-44_yr_20060101-20991231.nc
		ncatted -O -a NCO,global,d,, -h $path_indices_ens_tasmin_nobias/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-$experiment-EUR-44_yr_20060101-20991231.nc
		ncatted -O -a CDO,global,d,, -h $path_indices_ens_tasmin_nobias/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-$experiment-EUR-44_yr_20060101-20991231.nc
		# Make history attribute clean
		ncatted -h -a history,global,d,, $path_indices_ens_tasmin_nobias/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-$experiment-EUR-44_yr_20060101-20991231.nc          # delete history
		ncatted -O -h -a history,global,c,c,' ' $path_indices_ens_tasmin_nobias/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-$experiment-EUR-44_yr_20060101-20991231.nc   # create history

		echo
 		echo "-----"
 		echo "NCO patching HISTORICAL ensemble statistics for indice $indice, experiment $experiment and statistic $stat"
 		echo "-----"
 		echo


		# historical 	
 		ncks -A -v rlat,rlon,rotated_pole $(echo ${file_with_rlon_rlat}) \
 		$path_indices_ens_tasmin_nobias/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-historical-EUR-44_yr_19700101-20051231.nc
 		# Here a midstep is needed to rename rlon,rlat-->x,y
		ncrename -v rlat,y $path_indices_ens_tasmin_nobias/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-historical-EUR-44_yr_19700101-20051231.nc
		ncrename -v rlon,x $path_indices_ens_tasmin_nobias/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-historical-EUR-44_yr_19700101-20051231.nc
		# Add attribute to the variable
		ncatted -O -h -a grid_mapping,$(echo ${indice}),c,c,"rotated_pole" $path_indices_ens_tasmin_nobias/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-historical-EUR-44_yr_19700101-20051231.nc
		ncatted -O -a source_data_id,global,o,c,"ens-multiModel-"$stat"-historical-EUR-44" -h $path_indices_ens_tasmin_nobias/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-historical-EUR-44_yr_19700101-20051231.nc
		ncatted -O -a history_of_appended_files,global,d,, -h $path_indices_ens_tasmin_nobias/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-historical-EUR-44_yr_19700101-20051231.nc
		ncatted -O -a NCO,global,d,, -h $path_indices_ens_tasmin_nobias/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-historical-EUR-44_yr_19700101-20051231.nc
		ncatted -O -a CDO,global,d,, -h $path_indices_ens_tasmin_nobias/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-historical-EUR-44_yr_19700101-20051231.nc
		# Make history attribute clean
		ncatted -h -a history,global,d,, $path_indices_ens_tasmin_nobias/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-historical-EUR-44_yr_19700101-20051231.nc          # delete history
		ncatted -O -h -a history,global,c,c,' ' $path_indices_ens_tasmin_nobias/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-$stat-historical-EUR-44_yr_19700101-20051231.nc   # create history
		done


 		echo
 		echo "-----"
 		echo "Done calculating ensemble statistics for indice $indice"
 		echo "-----"
 		echo

	done
done
# # --------------------------------------------

# END

