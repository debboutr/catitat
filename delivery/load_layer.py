import os
from django.contrib.gis.utils import LayerMapping
from .models import Rivers, States

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

def run_rivers(verbose=True):
    lm = LayerMapping(Rivers,
                        river_shp,
                        rivers_mapping,
                        transform=False, 
                        encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

states_mapping = {
    'code': 'CODE',
    'geom': 'MULTIPOLYGON',
}

state_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/raw_states/clean_states.shp'))

def run_states(verbose=True):
    print (state_shp)
    lm = LayerMapping(States,
                        state_shp,
                        states_mapping,
                        transform=False, 
                        encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)