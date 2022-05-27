# STAC Packages

The [stactools-packages](https://github.com/stactools-packages/) github organization is a home for datasets and tool packages using the
[SpatioTemporal Asset Catalog (STAC)](https://github.com/radiantearth/stac-spec) specification.

Please use the template described below to add your data and tools.

## Adding a new Package

Clone the [template repository](https://github.com/stactools-packages/template) as your package name, e.g. `landsat`.
This name should be short, memorable, and a valid Python package name.
It can include a hyphen, in which case the name for Python imports will be the underscored version, e.g. `landsat-8` goes to `stactools.landsat_8`.
Your name will be used on PyPI to publish the package in the stactools namespace, e.g. `stactools-landsat`.

To learn about how to create a STAC, first read the [Best Practices document](https://github.com/radiantearth/stac-spec/blob/master/best-practices.md#stac-best-practices) 
to get a sense of what has emerged from other people using the specification. 


[STAC extensions](https://github.com/stac-extensions/) may have additional methods to describe your data and are **STRONGLY** encouraged.

## List of STAC Packages

The definitive list of STAC Packages are the repositories in the [Organization](https://github.com/stactools-packages). This list is automagically populated once a day.

Last Updated: May 27 00:52  2022 UTC.

| Package | Description |
| :------ | :---------- |
   [aafc-landuse](https://github.com/stactools-packages/aafc-landuse)|stactools package for working with Agriculture and Agri-Food Canada Land Use data
   [alos-dem](https://github.com/stactools-packages/alos-dem)|stactools package for working with the ALOS Global Digital Surface Model
   [aster](https://github.com/stactools-packages/aster)|None
   [bc-dem](https://github.com/stactools-packages/bc-dem)|None
   [browse](https://github.com/stactools-packages/browse)|stactools package for opening a STAC catalog with stac-browser
   [can-flood](https://github.com/stactools-packages/can-flood)|None
   [cgls_lc100](https://github.com/stactools-packages/cgls_lc100)|stactools package for working with Copernicus Global Land Cover Layers data.
   [chesapeake-lulc](https://github.com/stactools-packages/chesapeake-lulc)|Chesapeake Conservancy Land Cover
   [cop-dem](https://github.com/stactools-packages/cop-dem)|stactools package for working with Copernicus DEM data
   [corine](https://github.com/stactools-packages/corine)|stactools package for working with CORINE data.
   [drcog-lulc](https://github.com/stactools-packages/drcog-lulc)|Denver Regional Council of Governments Land Use Land Cover dataset
   [ecmwf-forecast](https://github.com/stactools-packages/ecmwf-forecast)|None
   [esa-worldcover](https://github.com/stactools-packages/esa-worldcover)|None
   [ga-dlcd](https://github.com/stactools-packages/ga-dlcd)|None
   [gap](https://github.com/stactools-packages/gap)|stactools package for working with USGS Gap Analysis Project (GAP) data
   [ghcnd](https://github.com/stactools-packages/ghcnd)|None
   [gnatsgo](https://github.com/stactools-packages/gnatsgo)|None
   [goes](https://github.com/stactools-packages/goes)|stactools package for working with NOAA's GOES data
   [gpw](https://github.com/stactools-packages/gpw)|stactools package for handling the Gridded Population of the World dataset
   [hwsd](https://github.com/stactools-packages/hwsd)|The Harmonized World Soil Database
   [jrc-gsw](https://github.com/stactools-packages/jrc-gsw)|stactools package for working with the European Commission's Joint Research Centre Global Surface Water data
   [landsat](https://github.com/stactools-packages/landsat)|stactools package for working with LANDSAT data
   [lila-hkh-glacier](https://github.com/stactools-packages/lila-hkh-glacier)|None
   [modis](https://github.com/stactools-packages/modis)|stactools package for working with MODIS data
   [naip](https://github.com/stactools-packages/naip)|stactools package for working with the USDA's National Airborne Imagery Program data
   [nalcms](https://github.com/stactools-packages/nalcms)|None
   [noaa-c-cap](https://github.com/stactools-packages/noaa-c-cap)|Create STAC Items and Collections for NOAA's Coastal Change Analysis Program (C-CAP)
   [noaa-climate-normals](https://github.com/stactools-packages/noaa-climate-normals)|stactools package for NOAA's climate normals dataset
   [noaa-sst](https://github.com/stactools-packages/noaa-sst)|None
   [nrcan-landcover](https://github.com/stactools-packages/nrcan-landcover)|Collection of Land Cover products for Canada as produced by NRCan
   [nrcan-radarsat1](https://github.com/stactools-packages/nrcan-radarsat1)|None
   [nrcan-spot-ortho](https://github.com/stactools-packages/nrcan-spot-ortho)|stactools package for working with SPOT data
   [palsar](https://github.com/stactools-packages/palsar)|stactools package for working with PALSAR data 
   [planet](https://github.com/stactools-packages/planet)|stactools package for working with Planet data
   [pointcloud](https://github.com/stactools-packages/pointcloud)|stactools package for working with pointcloud files
   [seabed-2030](https://github.com/stactools-packages/seabed-2030)|None
   [sentinel1](https://github.com/stactools-packages/sentinel1)|stactools package for working with sentinel1 data
   [sentinel1-grd](https://github.com/stactools-packages/sentinel1-grd)|None
   [sentinel2](https://github.com/stactools-packages/sentinel2)|stactools package for Sentinel-2
   [sentinel3](https://github.com/stactools-packages/sentinel3)|None
   [sentinel5p](https://github.com/stactools-packages/sentinel5p)|Stactools package for Sentinel 5P
   [soilgrids](https://github.com/stactools-packages/soilgrids)|None
   [stactools-packages.github.io](https://github.com/stactools-packages/stactools-packages.github.io)|None
   [template](https://github.com/stactools-packages/template)|Template repository for stactools packages
   [threedep](https://github.com/stactools-packages/threedep)|stactools package for working with elevation data from the USGS 3DEP program (formerly known as NED)
   [ukcp18](https://github.com/stactools-packages/ukcp18)|None
   [usgs-nlcd](https://github.com/stactools-packages/usgs-nlcd)|None
   [worldclim](https://github.com/stactools-packages/worldclim)|None
   [worldhistclim](https://github.com/stactools-packages/worldhistclim)|None
   [worldpop](https://github.com/stactools-packages/worldpop)|stactools package for working with WorldPop data