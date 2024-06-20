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

Last Updated: Jun 20 00:44  2024 UTC.

| Package | Description |
| :------ | :---------- |
   [.github](https://github.com/stactools-packages/.github)|None
   [aafc-landuse](https://github.com/stactools-packages/aafc-landuse)|stactools package for working with Agriculture and Agri-Food Canada Land Use data
   [alos-dem](https://github.com/stactools-packages/alos-dem)|stactools package for working with the ALOS Global Digital Surface Model
   [amazonia-1](https://github.com/stactools-packages/amazonia-1)|Amazonia-1 stactools package
   [aster](https://github.com/stactools-packages/aster)|stactools package for data from the Advanced Spaceborne Thermal Emission and Reflection Radiometer (ASTER)
   [bc-dem](https://github.com/stactools-packages/bc-dem)|None
   [browse](https://github.com/stactools-packages/browse)|stactools package for opening a STAC catalog with stac-browser
   [can-flood](https://github.com/stactools-packages/can-flood)|None
   [canelevation](https://github.com/stactools-packages/canelevation)|Create STACs from point clouds from various airborne LiDAR acquisition projects conducted in Canada. The LiDAR point cloud data is licensed under an open government license (Canada) and has been incorporated into the National Elevation Data Strategy.
   [cgls_lc100](https://github.com/stactools-packages/cgls_lc100)|stactools package for working with Copernicus Global Land Cover Layers data.
   [chesapeake-lulc](https://github.com/stactools-packages/chesapeake-lulc)|Chesapeake Conservancy Land Cover
   [cop-dem](https://github.com/stactools-packages/cop-dem)|stactools package for working with Copernicus DEM data
   [corine](https://github.com/stactools-packages/corine)|stactools package for working with CORINE data.
   [datacube](https://github.com/stactools-packages/datacube)|None
   [drcog-lulc](https://github.com/stactools-packages/drcog-lulc)|Denver Regional Council of Governments Land Use Land Cover dataset
   [ecmwf-forecast](https://github.com/stactools-packages/ecmwf-forecast)|stactools package for ECMWF Open Data - Real Time
   [esa-cci-lc](https://github.com/stactools-packages/esa-cci-lc)|stactools package for ESA's Climate Change Initiative (CCI) Land Cover (LC) product
   [esa-worldcover](https://github.com/stactools-packages/esa-worldcover)|stactools package for ESA's 10m resolution global land cover product
   [fws-nwi](https://github.com/stactools-packages/fws-nwi)|stactools package for the National Wetlands Inventory (NWI) product provided by the U.S. Fish and Wildlife Service (FWS)
   [ga-dlcd](https://github.com/stactools-packages/ga-dlcd)|stactools package for Geoscience Australia's Dynamic Land Cover Dataset (DLCD)
   [gap](https://github.com/stactools-packages/gap)|stactools package for working with USGS Gap Analysis Project (GAP) data
   [geoparquet-items](https://github.com/stactools-packages/geoparquet-items)|Uses stac-geoparquet to generate a geoparquet for a list of STAC items
   [ghcnd](https://github.com/stactools-packages/ghcnd)|stactools package for the Global Historical Climatology Network daily (GHCNd) dataset
   [gnatsgo](https://github.com/stactools-packages/gnatsgo)|stactools package for the USDA's Gridded National Soil Survey Geographic Database (gNATSGO)
   [goes](https://github.com/stactools-packages/goes)|stactools package for working with NOAA's GOES data
   [goes-glm](https://github.com/stactools-packages/goes-glm)|stactools package for the Geostationary Lightning Mapper (GLM) on the GOES satellites
   [gpw](https://github.com/stactools-packages/gpw)|stactools package for handling the Gridded Population of the World dataset
   [hls](https://github.com/stactools-packages/hls)|stactools package for Harmonized Landsat Sentinel-2 (HLS) data
   [hwsd](https://github.com/stactools-packages/hwsd)|The Harmonized World Soil Database
   [jrc-gsw](https://github.com/stactools-packages/jrc-gsw)|stactools package for working with the European Commission's Joint Research Centre Global Surface Water data
   [landsat](https://github.com/stactools-packages/landsat)|stactools package for working with LANDSAT data
   [lila-hkh-glacier](https://github.com/stactools-packages/lila-hkh-glacier)|stactools package for the Hindu Kush Himalayas (HKH) glacier mapping dataset
   [modis](https://github.com/stactools-packages/modis)|stactools package for working with MODIS data
   [msbuildings](https://github.com/stactools-packages/msbuildings)|None
   [naip](https://github.com/stactools-packages/naip)|stactools package for working with the USDA's National Agriculture Imagery Program data
   [nalcms](https://github.com/stactools-packages/nalcms)|stactools package for the North American Land Change Monitoring System
   [nisar-sim](https://github.com/stactools-packages/nisar-sim)|Simulated NISAR derived from UAVSAR data
   [noaa-c-cap](https://github.com/stactools-packages/noaa-c-cap)|Create STAC Items and Collections for NOAA's Coastal Change Analysis Program (C-CAP)
   [noaa-cdr](https://github.com/stactools-packages/noaa-cdr)|NOAA Climate Data Records (CDR) stactools package
   [noaa-climate-normals](https://github.com/stactools-packages/noaa-climate-normals)|NOAA US Climate Normals stactools package
   [noaa-gefs](https://github.com/stactools-packages/noaa-gefs)|WIP: stactools package for a variety of NOAA's Global Ensemble Forecast System (GEFS) products 
   [noaa-mrms-qpe](https://github.com/stactools-packages/noaa-mrms-qpe)|stactools package for NOAA's Multi-Radar Multi-Sensor Quantitative Precipitation Estimation dataset 
   [noaa-nclimgrid](https://github.com/stactools-packages/noaa-nclimgrid)|NOAA NClimGrid stactools package
   [noaa-nwm](https://github.com/stactools-packages/noaa-nwm)|None
   [noaa-sst](https://github.com/stactools-packages/noaa-sst)|stactools package for the NOAA Sea Surface Temperature (SST) product
   [nrcan-landcover](https://github.com/stactools-packages/nrcan-landcover)|Collection of Land Cover products for Canada as produced by NRCan
   [nrcan-radarsat1](https://github.com/stactools-packages/nrcan-radarsat1)|stactools packages for the NRCAN Radarsat 1 project
   [nrcan-spot-ortho](https://github.com/stactools-packages/nrcan-spot-ortho)|stactools package for working with SPOT data
   [palsar](https://github.com/stactools-packages/palsar)|stactools package for working with PALSAR data 
   [palsar2-scansar](https://github.com/stactools-packages/palsar2-scansar)|stactools package for working with PALSAR-2 ScanSAR data
   [planet](https://github.com/stactools-packages/planet)|stactools package for working with Planet data
   [pointcloud](https://github.com/stactools-packages/pointcloud)|stactools package for working with pointcloud files
   [seabed-2030](https://github.com/stactools-packages/seabed-2030)|stactools package for data from the Seabed 2030 project
   [sentinel1](https://github.com/stactools-packages/sentinel1)|stactools package for working with sentinel1 data
   [sentinel1-grd](https://github.com/stactools-packages/sentinel1-grd)|stactools package for Sentinel-1 Level-1 Ground Range Detected (GRD) products
   [sentinel2](https://github.com/stactools-packages/sentinel2)|stactools package for Sentinel-2
   [sentinel3](https://github.com/stactools-packages/sentinel3)|stactools package for Sentinel-3 data
   [sentinel5p](https://github.com/stactools-packages/sentinel5p)|Stactools package for Sentinel 5P
   [soilgrids](https://github.com/stactools-packages/soilgrids)|stactools package for the SoilGrids dataset
   [stactools-packages.github.io](https://github.com/stactools-packages/stactools-packages.github.io)|Dashboard website for the stactools-packages organization
   [template](https://github.com/stactools-packages/template)|Template repository for stactools packages
   [threedep](https://github.com/stactools-packages/threedep)|stactools package for working with elevation data from the USGS 3DEP program (formerly known as NED)
   [ukcp18](https://github.com/stactools-packages/ukcp18)|stactools package for UKCP18
   [usda-cdl](https://github.com/stactools-packages/usda-cdl)|USDA Cropland Data Layer
   [usgs-lcmap](https://github.com/stactools-packages/usgs-lcmap)|USGS Land Change Monitoring, Assesment, and Projection (LCMAP) stactools package
   [usgs-nlcd](https://github.com/stactools-packages/usgs-nlcd)|stactools package for the United States Geological Survey - National Land Cover Database (USGS-NLCD)
   [viirs](https://github.com/stactools-packages/viirs)|stactools package for data from the Visible Infrared Imaging Radiometer Suite (VIIRS)
   [worldclim](https://github.com/stactools-packages/worldclim)|stactools package for the WorldClim dataset
   [worldhistclim](https://github.com/stactools-packages/worldhistclim)|stactools package for the WorldClim dataset
   [worldpop](https://github.com/stactools-packages/worldpop)|stactools package for working with WorldPop data