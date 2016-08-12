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

### Maximum Temperature (TASMAX)

# Indice category & experiment
# -------------------
TASMAX_indices=('id' 'su' 'tx')
experiment=('rcp45' 'rcp85')
statistics=('20p' 'median' '80p')


indices_path='/nobackup/users/stepanov/icclim_indices_v4.2.3_seapoint_metadata_fixed/EUR-44/'

	# Ensemble statistics IN & OUT paths
# =========================================================================

# Bias corrected files
path_indices_ens_tasmax=$indices_path/BC/ens_multiModel_tasmax
# Non-Bias corrected files
path_indices_ens_tasmax_nobias=$indices_path/No_BC/ens_multiModel_tasmax_no_bc

# =========================================================================


for k in {0..2}; do           # counts statistics
	for j in {0..2}; do       # counts indices variables


		# BIAS CORRECTED
		# ===================================================================================================================================================================================
		cd $path_indices_ens_tasmax

		for l in {0..1}; do   # counts experiments
			# projections
			proj_bc_file=$path_indices_ens_tasmax/${TASMAX_indices[j]}_icclim-4-2-3_KNMI_ens-multiModel-${statistics[k]}-${experiment[l]}-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_20060101-20991231.nc
			echo 
			echo "Going for file:"
			echo $proj_bc_file
			echo
			# delete invar_tracking_id
			ncatted -h -a invar_tracking_id,global,d,, $proj_bc_file
			# rename tracking_id --> invar_tracking_id
			ncrename -h -a .tracking_id,invar_tracking_id $proj_bc_file
			# generate new unique tracking_id
			ncatted -O -h -a tracking_id,global,o,c,$(uuidgen) $proj_bc_file
		done


		# historical
		hist_bc_file=$path_indices_ens_tasmax/${TASMAX_indices[j]}_icclim-4-2-3_KNMI_ens-multiModel-${statistics[k]}-historical-EUR-44-SMHI-DBS43-EOBS10-bcref-1981-2010_yr_19700101-20051231.nc
		echo 
		echo "Going for file:"
		echo $hist_bc_file
		echo
		# delete invar_tracking_id
		ncatted -h -a invar_tracking_id,global,d,, $hist_bc_file
		# rename tracking_id --> invar_tracking_id
		ncrename -h -a .tracking_id,invar_tracking_id $hist_bc_file
		# generate new unique tracking_id
		ncatted -O -h -a tracking_id,global,o,c,$(uuidgen) $hist_bc_file

		# ===================================================================================================================================================================================
		# Non BIAS CORRECTED
		# ===================================================================================================================================================================================
		cd $path_indices_ens_tasmax_nobias

		# projections
		for l in {0..1}; do   # counts experiments
			proj_no_bc_file=$path_indices_ens_tasmax_nobias/${TASMAX_indices[j]}_icclim-4-2-3_KNMI_ens-multiModel-${statistics[k]}-${experiment[l]}-EUR-44_yr_20060101-20991231.nc
			echo 
			echo "Going for file:"
			echo $proj_no_bc_file
			echo
			# delete invar_tracking_id
			ncatted -h -a invar_tracking_id,global,d,, $proj_no_bc_file
			# rename tracking_id --> invar_tracking_id
			ncrename -h -a .tracking_id,invar_tracking_id $proj_no_bc_file
			# generate new unique tracking_id
			ncatted -O -h -a tracking_id,global,o,c,$(uuidgen) $proj_no_bc_file
		done

		# historical
		hist_no_bc_file=$path_indices_ens_tasmax_nobias/${TASMAX_indices[j]}_icclim-4-2-3_KNMI_ens-multiModel-${statistics[k]}-historical-EUR-44_yr_19700101-20051231.nc
		echo 
		echo "Going for file:"
		echo $hist_no_bc_file
		echo
		# delete invar_tracking_id
		ncatted -h -a invar_tracking_id,global,d,, $hist_no_bc_file
		# rename tracking_id --> invar_tracking_id
		ncrename -h -a .tracking_id,invar_tracking_id $hist_no_bc_file
		# # generate new unique tracking_id
		ncatted -O -h -a tracking_id,global,o,c,$(uuidgen) $hist_no_bc_file
		
	    # ===================================================================================================================================================================================

	done

done
