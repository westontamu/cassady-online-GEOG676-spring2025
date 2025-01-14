import arcpy

# Assign bands
source = r"C:\\Users\\cassadyw\\Desktop\\Grad School\\GEOG676\\cassady-online-GEOG676-spring2025\\Lab_7"
band1 = arcpy.sa.Raster(source + r"\band1.tif") #blue
band2 = arcpy.sa.Raster(source + r"\band1.tif") #green
band3 = arcpy.sa.Raster(source + r"\band1.tif") #red
band4 = arcpy.sa.Raster(source + r"\band1.tif") #NIR
combined = arcpy.CompositeBands_management([band1, band2, band3, band4], source + r"\output_combined.tif")

# Hillshade
azimuth = 315
altitude = 45
shadows = 'NO_SHADOWS'
z_factor = 1
arcpy.ddd.HillShade(source + r"\DEM.tif", source + r"\output_Hillshade.tif", azimuth, altitude, shadows, z_factor)

# Slope
output_measurement = "DEGREE"
z_factor = 1
arcpy.ddd.Slope(source + r"\DEM.tif", source + r"\output_Slope.tif", output_measurement, z_factor)
print("success!")