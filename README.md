# generate-soil-map
This python script generates soil map for any place in the world. 

It takes basin shapefile as an input and generate soil map using hwsd provided by FAO. More about hwsd can be found on the following link:

http://www.fao.org/soils-portal/soil-survey/soil-maps-and-databases/harmonized-world-soil-database-v12/en/

HOW TO USE:

1. It uses arcpy to generate soil map, make sure arcpy is installed.

2. Open the "soil_hwsd.py" and put the paths of required data (mentioned in the script)

3. Extract the ZIP file and provide the path of 'hwsd.bil' file from there

4. All the required files (hwsd.bi, hwsd class data, soil class) are provided with the code. Edit the path of these file in 'soil_hwsd.py' file.
