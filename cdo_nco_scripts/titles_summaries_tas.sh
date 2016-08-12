#!/bin/bash

# Executable bash script

# Import ensemble statistics and change title and summary global attributes accordingly
# to match the DRS standards v1.3

# Update list
#
# 09/08/2016 I.S. Created script
# -------------------------------------------------------------------------

# IFS=$'\n'

# Define some pahts
# =========================================================================


### Mean Temperature (TAS)

# Indice category & experiment
# -------------------
TAS_indices="hd17"
experiments="rcp45 rcp85"
statistics=('20p' 'median' '80p')
in_stats=('20th percentile' 'median(50th percentile)' '80th percentile')
gcms=('CCCma-CanESM2, CNRM-CM5, CSIRO-Mk3-6-0, EC-EARTH, IPSL-CM5A-MR, MIROC5, HadGEM2-ES, MPI-ESM-LR, NorESM1-M, GFDL-ESM2M')



for experiment in $experiments; do

	indices_path='/nobackup/users/stepanov/icclim_indices_v4.2.3_seapoint_metadata_fixed/EUR-44/'


	# Ensemble statistics IN & OUT paths
	# =========================================================================

	# Bias corrected files
	path_indices_ens_tas=$indices_path/BC/ens_multiModel_tas
	# Non-Bias corrected files
	path_indices_ens_tas_nobias=$indices_path/No_BC/ens_multiModel_tas_no_bc

	# =========================================================================

	# Take indices parameters from the list above
	for indice in $TAS_indices; do

		# PROJECTIONS
		for k in {0..2}; do  # counts in_stats and statistics lists simultaneously

			echo 'For title:'
			titles="hd17: ensemble ${in_stats[k]} of heating degree days"
			echo
			echo $titles

			# BIAS CORRECTED
			# ===========================================================================================================================================================================================================
			cd $path_indices_ens_tas
			# projections
			ncatted -O -a title,global,o,c,"$titles" -h $path_indices_ens_tas/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-${statistics[k]}-$experiment-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_20060101-20991231.nc
			ncatted -O -a summary,global,o,c,"This is the ensemble ${in_stats[k]} of hd17. The ensemble is constructed by the following models: $gcms. For the definition of hd17 see ECA&D." -h $path_indices_ens_tas/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-${statistics[k]}-$experiment-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_20060101-20991231.nc
			ncatted -O -a invar_rcm_model_driver,global,o,c,' ' -h $path_indices_ens_tas/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-${statistics[k]}-$experiment-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_20060101-20991231.nc

			# historical
			ncatted -O -a title,global,o,c,"$titles" -h $path_indices_ens_tas/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-${statistics[k]}-historical-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_19700101-20051231.nc
			ncatted -O -a summary,global,o,c,"This is the ensemble ${in_stats[k]} of hd17. The ensemble is constructed by the following models: $gcms. For the definition of hd17 see ECA&D." -h $path_indices_ens_tas/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-${statistics[k]}-historical-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_19700101-20051231.nc			
			ncatted -O -a invar_rcm_model_driver,global,o,c,' ' -h $path_indices_ens_tas/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-${statistics[k]}-historical-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_19700101-20051231.nc

			# ===========================================================================================================================================================================================================

			# Non BIAS CORRECTED
			# ===========================================================================================================================================================================================================
			cd $path_indices_ens_tas_nobias

			# projections
			ncatted -O -a title,global,o,c,"$titles" -h $path_indices_ens_tas_nobias/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-${statistics[k]}-$experiment-EUR-44_yr_20060101-20991231.nc
			ncatted -O -a summary,global,o,c,"This is the ensemble ${in_stats[k]} of hd17. The ensemble is constructed by the following models: $gcms. For the definition of hd17 see ECA&D." -h $path_indices_ens_tas_nobias/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-${statistics[k]}-$experiment-EUR-44_yr_20060101-20991231.nc
			ncatted -O -a invar_rcm_model_driver,global,o,c,' ' -h $path_indices_ens_tas_nobias/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-${statistics[k]}-$experiment-EUR-44_yr_20060101-20991231.nc

			# historical
			ncatted -O -a title,global,o,c,"$titles" -h $path_indices_ens_tas_nobias/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-${statistics[k]}-historical-EUR-44_yr_19700101-20051231.nc
			ncatted -O -a summary,global,o,c,"This is the ensemble ${in_stats[k]} of hd17. The ensemble is constructed by the following models: $gcms. For the definition of hd17 see ECA&D." -h $path_indices_ens_tas_nobias/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-${statistics[k]}-historical-EUR-44_yr_19700101-20051231.nc			
			ncatted -O -a invar_rcm_model_driver,global,o,c,' ' -h $path_indices_ens_tas_nobias/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-${statistics[k]}-historical-EUR-44_yr_19700101-20051231.nc

            # ===========================================================================================================================================================================================================



			# Log of changed files
			# ===========================================================================================================================================================================================================
			echo
			echo "Files edited in this step:" 
			echo
			echo $path_indices_ens_tas/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-${statistics[k]}-$experiment-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_20060101-20991231.nc   # projections BC
			echo $path_indices_ens_tas_nobias/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-${statistics[k]}-$experiment-EUR-44_yr_20060101-20991231.nc                              # projections nBC
			echo $path_indices_ens_tas/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-${statistics[k]}-historical-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_19700101-20051231.nc    # historical BC
			echo $path_indices_ens_tas_nobias/$(echo ${indice})_icclim-4-2-3_KNMI_ens-multiModel-${statistics[k]}-historical-EUR-44_yr_19700101-20051231.nc                               # historical nBC

			echo
	 		echo "-----"
	 		echo "NCO patched PROJECTION ensemble statistics for indice $indice, experiment $experiment,statistic ${statistics[k]} and title statistic ${in_stats[k]}"
	 		echo "-----"
	 		echo
	 		# ===========================================================================================================================================================================================================

 		done

	done

done
