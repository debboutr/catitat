import os
from django.contrib.gis.utils import LayerMapping
from .models import Rivers

# Auto-generated `LayerMapping` dictionary for Counties model
rivers_mapping = {
    'comid': 'COMID',
    'reachcode': 'REACHCODE',
    'flowdir': 'FLOWDIR',
    'wbareacomi': 'WBAREACOMI',
    'ftype': 'FTYPE',
    'streamorde': 'StreamOrde',
    'geom': 'MULTIPOINT',
}


river_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/flow_03N_centroid.shp'))

def run(verbose=True):
    lm = LayerMapping(Rivers,
                        river_shp,
                        rivers_mapping,
                        transform=False, 
                        encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)