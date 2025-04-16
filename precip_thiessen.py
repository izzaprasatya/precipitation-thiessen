import grass.script as gs

gs.run_command("v.import",
    input="C:\Geog-Project\Hydrology\Precipitation\Serayu_Catchment.shp",
    output="Catchment")

gs.run_command("v.import",
    input="C:\Geog-Project\Hydrology\Precipitation\Precipitation-Data\P_JAN.shp",
    output="Stations")

gs.run_command("r.import",
    input="C:\Geog-Project\Hydrology\Precipitation\SRTM30m.tif",
    output="DEM")

gs.run_command("g.region",
    raster="DEM")

gs.run_command("v.to.db",
    map="Catchment",
    option="area",
    columns="luas_km2",
    units="kilometers")

gs.run_command("v.voronoi",
    input="Stations",
    output="Thiessen")

gs.run_command("v.clip",
    input="Thiessen",
    clip="Catchment",
    output="P_Polygons")

gs.run_command("v.to.db",
    map="P_Polygons",
    option="area",
    columns="AREA_km2",
    units="kilometers")

"""
Spatially average rainfall calculation

r1 = 16.2129032258064
r2 = 14.6451612903226
r3 = 7.90645161290323

a1 = 125.978426
a2 = 2427.6661
a3 = 1101.110037

p = ((r1*a1)+(r2*a2)+(r3*a3))/(a1+a2+a3)

print(round(p, 2))
"""