# Make python script executable
#!/usr/bin/python

# Script copies variable from one NetCDF file 
# to another (needed for EUR-11 indices)
# placed on ADAGUC climate4impact portal

# It should copy from the RCM files on EUR-11 grid the following vars:

# rlon          --> x
# rlat          --> y
# rotated_pole  --> rotated_pole

# and the global attribute:

# prAdjust: grid mapping="rotated pole"

# ==========================================
# Author: I.Stepanov (igor.stepanov@knmi.nl)
# 02.05.2016 @KNMI
# ============================================================================================
# Updates list
# 
# 12.05.2016. Updated the header here with list of vars/atts to be copied
# ============================================================================================

# -*- coding: utf-8 -*-
from netCDF4 import Dataset

in_path = "/nobackup/users/stepanov/NC_header/"

#input file
dsin = Dataset \
(in_path+"prAdjust_EUR-11_CNRM-CERFACS-CNRM-CM5_rcp45_r1i1p1_SMHI-RCA4_v1-SMHI-DBS43-MESAN-1989-2010_day_20460101-20501231.nc")

#output file
dsout = Dataset(in_path+"test_out.nc", "w", format="NETCDF4")

#Copy dimensions
for dname, the_dim in dsin.dimensions.iteritems():

	 # take out the variable you don't want
    if dname == 'prAdjust': 
    	continue

    print dname, len(the_dim)
    dsout.createDimension(dname, len(the_dim) if not the_dim.isunlimited() else None)


# Copy variables
for v_name, varin in dsin.variables.iteritems():
    outVar = dsout.createVariable(v_name, varin.datatype, varin.dimensions)
    print varin.datatype
    
    # Copy variable attributes
    outVar.setncatts({k: varin.getncattr(k) for k in varin.ncattrs()})
    
    outVar[:] = varin[:]
# close the output file
dsout.close()

print 'Done!'


# Andrej

# copy existing netcdf to new file with name
#
# def copyNetCDF(name, nc_fid , des ):
#   w_nc_fid = netCDF4.Dataset(name, 'w', format='NETCDF4')

#   #PROVENANCE ADDED!!!!

#   w_nc_fid.description = des

#   for var_name, dimension in nc_fid.dimensions.iteritems():
#     w_nc_fid.createDimension(var_name, len(dimension) if not dimension.isunlimited() else None)

#   for var_name, ncvar in nc_fid.variables.iteritems():

#     outVar = w_nc_fid.createVariable(var_name, ncvar.datatype, ncvar.dimensions )
  
#     ad = dict((k , ncvar.getncattr(k) ) for k in ncvar.ncattrs() )

#     outVar.setncatts(  ad  )

#     outVar[:] = ncvar[:]

#   global_vars = dict((k , nc_fid.getncattr(k) ) for k in nc_fid.ncattrs() )
  
#   for k in sorted(global_vars.keys()):
#     w_nc_fid.setncattr(  k , global_vars[k]  )

#   return w_nc_fid
# # end copy