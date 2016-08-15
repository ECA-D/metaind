#!/bin/bash
#
#==========================================================================================================================================
# correct variable attributes for precipitation indices
#==========================================================================================================================================
#
#C.Photiadou 2016/07/25
# Directories
dir_in='/nobackup/users/photiado/icclim_indices_v4.2.3_seapoint_metadata_fixed/EUR-44/BC/tas/'
dir_sc='/nobackup/users/photiado/icclim_indices_v4.2.3_seapoint_metadata_fixed/scripts/'
path_ic_inst='icclim-4-2-3_KNMI'
path_real_bc='r1i1p1_SMHI-RCA4_v1_EUR-44_SMHI-DBS43_EOBS10_bcref-1981-2010_yr'
#=====================
# Variables
#=====================
IFS=$'\n'
gcms=('CCCma-CanESM2' 'CNRM-CM5' 'CSIRO-Mk3-6-0' 'EC-EARTH' 'IPSL-CM5A-MR' 'MIROC5' 'HadGEM2-ES' 'MPI-ESM-LR' 'NorESM1-M' 'GFDL-ESM2M')
ind='HD17'
indices='hd17'
invar_vari='tasAdjust' #'pr' #'tasminAdjust' 'tasmaxAdjust' 'tasAdjust' #tas(nobc)
exper=('rcp45' 'rcp85' 'historical')
time_cov_start=('20060101' '20060101' '19700101')
time_cov_end=('20991231' '20991231' '20051231')


#========================================================================
### Fix issue for EC_EARTH and HadGem but remember to bringit back at the end!
#========================================================================

gcm_ec='EC-EARTH'
gcm_ha='HadGEM2-ES'
had_time_end=('20991130' '20991230' '20051230')

	for i in {0..2}; do #exper
	echo
	echo "Rename EC-EARTH & HadGEM"
	echo
		echo ${exper[i]}
	echo
		mv ${dir_in}${indices}_${path_ic_inst}_${gcm_ec}_${exper[i]}_r12i1p1_SMHI-RCA4_v1_EUR-44_SMHI-DBS43_EOBS10_bcref-1981-2010_yr_${time_cov_start[i]}-${time_cov_end[i]}.nc ${dir_in}${indices}_${path_ic_inst}_${gcm_ec}_${exper[i]}_${path_real_bc}_${time_cov_start[i]}-${time_cov_end[i]}.nc
		
		mv ${dir_in}${indices}_${path_ic_inst}_${gcm_ha}_${exper[i]}_${path_real_bc}_${time_cov_start[i]}-${had_time_end[i]}.nc ${dir_in}${indices}_${path_ic_inst}_${gcm_ha}_${exper[i]}_${path_real_bc}_${time_cov_start[i]}-${time_cov_end[i]}.nc
			   
	done

#========================================================================
### Make the sea NAs again (maybe put this into a seperate script)
#========================================================================
 for k in {0..2}; do #indices & exper
		###############
	echo
	echo "Sea Mask"
	echo
		echo ${indices}
		echo ${exper[k]}
	echo
		###############
  for j in {0..9}; do  
  echo              
		echo ${gcms[j]}
  echo
		#make nas the sea!
		cdo div ${dir_in}${indices}_${path_ic_inst}_${gcms[j]}_${exper[k]}_${path_real_bc}_${time_cov_start[k]}-${time_cov_end[k]}.nc \
		        ${dir_sc}mask_file_clipc.nc \
		        ${dir_in}${indices}_${path_ic_inst}_${gcms[j]}_${exper[k]}_${path_real_bc}_${time_cov_start[k]}-${time_cov_end[k]}_sm.nc
	
		#add back the rlat rlon
		ncks -A -v rlat,rlon,rotated_pole ${dir_in}${indices}_${path_ic_inst}_${gcms[j]}_${exper[k]}_${path_real_bc}_${time_cov_start[k]}-${time_cov_end[k]}.nc \
										  ${dir_in}${indices}_${path_ic_inst}_${gcms[j]}_${exper[k]}_${path_real_bc}_${time_cov_start[k]}-${time_cov_end[k]}_sm.nc
	
	 # Here a midstep is needed to rename rlon,rlat-->x,y
        ncrename -v rlat,y ${dir_in}${indices}_${path_ic_inst}_${gcms[j]}_${exper[k]}_${path_real_bc}_${time_cov_start[k]}-${time_cov_end[k]}_sm.nc
        ncrename -v rlon,x ${dir_in}${indices}_${path_ic_inst}_${gcms[j]}_${exper[k]}_${path_real_bc}_${time_cov_start[k]}-${time_cov_end[k]}_sm.nc

        # Add attribute to the variable
        ncatted -O -h -a grid_mapping,${ind[k]},c,c,"rotated_pole" ${dir_in}${indices}_${path_ic_inst}_${gcms[j]}_${exper[k]}_${path_real_bc}_${time_cov_start[k]}-${time_cov_end[k]}_sm.nc
		
		#remove the _sm in the name
		mv ${dir_in}${indices}_${path_ic_inst}_${gcms[j]}_${exper[k]}_${path_real_bc}_${time_cov_start[k]}-${time_cov_end[k]}_sm.nc ${dir_in}${indices}_${path_ic_inst}_${gcms[j]}_${exper[k]}_${path_real_bc}_${time_cov_start[k]}-${time_cov_end[k]}.nc
	done 
done

#========================================================================
### Correct filename for EC-EARTH & HadGem!
#========================================================================

for i in {0..2}; do #exper & indices
	echo
		echo "Rename back EC-EARTH & HadGEM"
	echo
		echo ${indices}
		echo ${exper[i]}
	echo
		mv ${dir_in}${indices}_${path_ic_inst}_${gcm_ec}_${exper[i]}_${path_real_bc}_${time_cov_start[i]}-${time_cov_end[i]}.nc ${dir_in}${indices}_${path_ic_inst}_${gcm_ec}_${exper[i]}_r12i1p1_SMHI-RCA4_v1_EUR-44_SMHI-DBS43_EOBS10_bcref-1981-2010_yr_${time_cov_start[i]}-${time_cov_end[i]}.nc

		mv ${dir_in}${indices}_${path_ic_inst}_${gcm_ha}_${exper[i]}_${path_real_bc}_${time_cov_start[i]}-${time_cov_end[i]}.nc ${dir_in}${indices}_${path_ic_inst}_${gcm_ha}_${exper[i]}_${path_real_bc}_${time_cov_start[i]}-${had_time_end[i]}.nc
done

