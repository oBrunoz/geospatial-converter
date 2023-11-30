import rasterio
from rasterio.features import shapes
from rasterio.warp import transform_geom
from rasterio.plot import show
from matplotlib import pyplot

url_ = r'C:\Users\bruno.ferreira\Desktop\GEOtiff_arquivos\arquivos_processados\processado2.tif'

def geoJSON_shapes(file_path=url_):
    with rasterio.open(file_path) as dataset:
        mask = dataset.dataset_mask()

        for geom, val in shapes(mask, transform=dataset.transform):
            geom = transform_geom(dataset.crs, 'EPSG:4326', geom, precision=6)
            
        return geom

def open_dataset_file_info(file_path=url_):
    try:
        with rasterio.open(file_path) as dataset:
            raster_shapes_list = geoJSON_shapes()

            dataset_info = {
                'name': dataset.name, # It returns file name
                'count': dataset.count, # It returns number of bands
                'bounds': dataset.bounds, # It returns bounderings of the raster
                'crs_info': dataset.crs.to_dict() if dataset.crs else None, #It returns crs information in WKT
                'geo_shapes': raster_shapes_list, #It returns raster shapes as list
            }
        return dataset_info
    
    except Exception as e:
        print(e)

    return None

def view_raster(raster_path=url_):
    try:
        with rasterio.open(raster_path) as src:
            band = src.read(1)

    except Exception as e:
        print(e)

# show(result_band1)
