# Make python script executable
#!/usr/bin/python

# Script to calculate temperature min/max indices from EOBS temperature data sets

import netCDF4
import ctypes
import icclim
import datetime
import icclim.util.callback as callback
#cb = callback.defaultCallback


print
print '<<Loaded modules>>'
print


# Define some paths

#in_path="/Users/istepanov/PostDoc/EOBS_data"         # local MBP
#in_path="/usr/people/stepanov/EOBS_data/"            # home folder
in_path="/nobackup/users/stepanov/EOBS_data/"         # nobackup
out_path="/nobackup/users/stepanov/icclim_indices/"   # nobackup


# ECA&D files
file_ave_temp = [in_path+'tg_0.25deg_reg_v12.0.nc']  # Average temperature
file_max_temp = [in_path+'tx_0.25deg_reg_v12.0.nc']  # Max temperature
file_min_temp = [in_path+'tn_0.25deg_reg_v12.0.nc']  # Min temperature
file_precip   = [in_path+'rr_0.25deg_reg_v12.0.nc']  # Precipitation


#files = [file_ave_temp]
#files = [file_max_temp]
#files = [file_min_temp]
#files = [file_precip]


# Define base period for percentile indices
base_dt1 = datetime.datetime(1951,01,01)
base_dt2 = datetime.datetime(1955,12,31)


# Define time ranges
dt1 = datetime.datetime(1988,1,1)
dt2 = datetime.datetime(2005,12,31)


# Output file name construction
# Alternative way for this dependent on indice parameter written below in for loop


#if files==[file_precip]:
#	calc_indice = out_path+'precip_out_1998-2005.nc'
#elif files==[file_ave_temp]:
#	calc_indice = out_path+'temperature_out.nc'
#elif files==[file_max_temp]:
#	calc_indice = out_path+'temperature_max_out.nc'
#elif files==[file_min_temp]:
#	calc_indice = out_path+'temperature_min_out.nc'
#elif files==[file_max_temp, file_min_temp]:
#	calc_indice = out_path+'temperature_max_min_out.nc'
#else:
#	calc_indice = out_path+'generic_name.nc'


# Time range
tr = [datetime.datetime(1981,01,01), datetime.datetime(1985,12,31)]


# Declare which indices you want to calculate
indice_list_ave_temp = ['TG10p','TG90p']
indice_list_max_temp = ['TX10p','TX90p']



# -------------------------------------------------------------------------
# Calculate actual indices
# -------------------------------------------------------------------------


#icclim.indice(indice_name='SU',
#               in_files=files,
#               var_name='tasmax',
#               time_range=[dt1, dt2],
#               slice_mode='JJA',
#               out_file=out_f)

#icclim.indice(indice_name='ERT',
#               in_files=files,
#               var_name=['tx','tn'],
#               time_range=tr,
#               out_file=out_f)

#icclim.indice(indice_name='SU',
#               in_files=files,
#               var_name=['tg'],
#               time_range=[dt1,dt2],
#               out_file=calc_indice,
#               callback=callback.defaultCallback2)



# Percentile based (out_unit="%" or "days")
for indice_ave_temp in indice_list_ave_temp:
	print
	print 'Now calculating indice', indice_ave_temp,':'
	print


# Build output file name construction phase
	calc_indice_ave_temp = out_path+indice_ave_temp+'_temp_ave.nc'
	print 'Going into output file:', calc_indice_ave_temp
	print

#quit()
	
	icclim.indice(indice_name=indice_ave_temp, in_files=file_ave_temp, var_name=['tg'], 
                                           slice_mode='AMJJAS', 
                                           time_range=[dt1,dt2], 
                                           base_period_time_range=[base_dt1, base_dt2],
                                           out_unit="%", 
                                           out_file=calc_indice_ave_temp, 
                                           callback=callback.defaultCallback2)


for indice_max_temp in indice_list_max_temp:
	print
	print 'Now calculating indice', indice_max_temp,':'
	print


# Build output file name construction phase
	calc_indice_max_temp = out_path+indice_max_temp+'_temp_max.nc'
	print 'Going into output file:', calc_indice_max_temp
	print

	
	icclim.indice(indice_name=indice_max_temp, in_files=file_max_temp, var_name=['tx'], 
                                          slice_mode='AMJJAS', 
                                          time_range=[dt1,dt2], 
                                          base_period_time_range=[base_dt1, base_dt2],
                                          out_file=calc_indice_max_temp, 
                                          callback=callback.defaultCallback2)




# Done with calculations

print
print 'Done!'
print

quit()


