from django.contrib.gis.db import models

        
class Rivers(models.Model):
    '''
    -- command below will produce the mapping here --
    mng ogrinspect delivery/data/flow_03N_centroid.shp Rivers --srid=4326 --mapping --multi
    '''    
    comid = models.BigIntegerField()
    reachcode = models.CharField(max_length=80)
    flowdir = models.CharField(max_length=80)
    wbareacomi = models.BigIntegerField()
    ftype = models.CharField(max_length=80)
    streamorde = models.FloatField()
    geom = models.MultiPointField(srid=4326)

    class Meta:
        verbose_name_plural = 'Rivers'

class States(models.Model):
    code = models.CharField(max_length=2)
    geom = models.MultiPolygonField(srid=4326)

    class Meta:
        verbose_name_plural = 'States'