"""
Created on June 9th, 2019
@author: Lokendra Singh Rathore
@National Institute of Hydrology, Roorkee, India
@email: lokendra.nalu@gmail.com
Use this script for generate soil map (FAO).
Make sure arcpy is installed
"""

import arcpy


# EDIT THE FOLLOWING LINES ### 
############################
arcpy.env.workspace="G:/Rathore/vic_auto6"                  ### Put a folder location (a new folder is suggested)
arcpy.env.overwriteOutput=True
basin="G:\\ARORA\\India_SHP\\INDIA.shp"                 ### Location of shapefile of basin for which soil map will be generated  (in GCS_WGS_1984)

hwsd_excel='G:\\Rathore\\HWSD_RASTER\\HWSD_CLS_DATA.xlsx'   ### Location of hwsd_class data excel file, provided with this code
text_class='G:\\Rathore\\HWSD_RASTER\\text_class.xlsx'      ### Location of text_class data excel file, provided with this code
hwsd="G:\\Rathore\\HWSD_RASTER\\hwsd.bil"                   ### Location of hwsl.bil file, provided with this code
out_name="soil_fao_india.tif"                                   ### Name of the output soil file (should end with tif)
###############################################################################################################

#  DO NOT  EDIT FROM  HERE
arcpy.env.overwriteOutput=True
print "All necessary files have been imported, processing starts.... \n"

out=arcpy.sa.ExtractByMask(hwsd,basin)


arcpy.ExcelToTable_conversion(hwsd_excel,"hwsd_tab")
arcpy.JoinField_management(out,"VALUE","hwsd_tab","MU_GLOBAL")
out_re=arcpy.sa.Reclassify(out,"T_USDA_TEX",arcpy.sa.RemapValue([[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],[10,10],[11,11],[12,12],[13,13]]))
out_re.save(out_name)
arcpy.ExcelToTable_conversion(text_class,"text_class_tab2")
arcpy.JoinField_management(out_name,"VALUE","text_class_tab2","CODE")

print "A soil map for the given basin area has been perpared with the name {0} in the workspace".format(out_name)
