Routine to calculate icclim [CLIP-C] indices using the icclim python module for EUR-44 domain.
==
- includes both bias corrected and non-bias corrected RCM data
- up to date with DRS ClipC metadata compliance v1.3 - July 2016
- calculate 15 climate extreme indices:
	+ precipitation: PRCPTOT,R1MM,RX1DAY,R95P,R10MM,R20MM,CWD,CDD
	+ tmax: ID,TX,SU
	+ tmin: FD,TR,TN
	+ tmean: HD17

Input files:
--
RMC bias corrected files used as input are provided by http://exporter.nsc.liu.se/e4ba1c00373c4b548b12c30b269a1c98/

Non-bias corrected files are on http://esgf.llnl.gov/

Step by step procedure of RCM variable tasmax/tasmaxAdjust (example)
--
- producing climate extreme indices ID (icing days), SU (summer days) and TX (mean of daily maximum temperature):


1. Calculate indices using .py script:

Beforehand install icclim module from https://github.com/cerfacs-globc/icclim

Then run:

	* calc_indices_icclim_RCM_TMAX_EUR_44.py -for bias corrected RCM output

- prereq modules to run this script:

```python
import netCDF4
import ctypes
import icclim
import datetime
import icclim.util.callback as callback

```
  
2. Filter out zeroes on sea points (sea mask):
	+ sea_mask_tasmax.sh
    
3. Import RCM tracking_id as invar_tracking_id and create unique indice tracking_id: 
	+ get_put_invar_tracking_id_python_TMAX.py

4. Create metadata global entries fields and fill them in
	+ meta_var_attr_tasmax.sh
    
5. Calculate ensemble statistics
    + calc_indicator_statistics_tasmax.sh

6. Append rlat,rlon as variables to statistics indices files produces in the previous step with:
    + append_rename_vars_nc_nco.sh

7. Change global metadata fields "title" and "summary" for ensemble indices:
    + titles_summaries_tasmax.sh

8. Rename tracking_id to invar_tracking_id and create unique tracking_id entry and value for ensemble indices files
    + rename_tracking_id2invar_tracking_id_and_gen_new_tracking_id_tasmax.sh
    





