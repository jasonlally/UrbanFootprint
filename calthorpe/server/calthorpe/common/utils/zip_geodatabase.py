# UrbanFootprint-California, Scenario Planning Model
# 
# Copyright (C) 2012-2013 Calthorpe Associates
# 
# This program is free software: you can redistribute it and/or modify it under the terms of the
# GNU General Public License as published by the Free Software Foundation, version 3 of the License.
# 
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.
# 
# Contact: Calthorpe Associates (urbanfootprint@calthorpe.com)
# Firm contact: 2095 Rose Street Suite 201, Berkeley CA 94709.
# Phone: (510) 548-6800.      Web: www.calthorpe.com
# 


'''Script: Sample_Zip_Geodatabase.py

Purpose: The purpose of this script is to show the basics of using python to zip up an ESRI file geodatabase.
The

Original Post: http://nodedangles.wordpress.com/2011/02/08/zipping-a-file-geodatabase-using-python/
'''

import os
import zipfile
import glob


def zip_file_gdb(path_to_file_gdb, path_to_zip=None, overwrite=True):
    if not (os.path.exists(path_to_file_gdb)):
        return False

    if not path_to_zip:
        path_to_zip = path_to_file_gdb + ".zip"

    if os.path.exists(path_to_zip):
        if overwrite:
            os.remove(path_to_zip)
        else:
            raise Exception(path_to_zip + " exists, and you specified overwrite=False")


    zipobj = zipfile.ZipFile(path_to_zip, 'w')

    for infile in glob.glob(path_to_file_gdb+"/*"):
        zipobj.write(infile, os.path.basename(path_to_file_gdb)+"/"+os.path.basename(infile), zipfile.ZIP_DEFLATED)
        print ("Zipping: "+infile)

    zipobj.close()

    return path_to_zip
