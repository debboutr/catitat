from django.contrib.gis.db import models

class Rivers(models.Model):
    '''
    -- command below will produce the mapping here --
    mng ogrinspect reporter/data/flow_03N_centroid.shp Rivers --multi
    '''
    comid = models.BigIntegerField()
    fdate = models.CharField(max_length=80)
    resolution = models.CharField(max_length=80)
    gnis_id = models.CharField(max_length=80)
    gnis_name = models.CharField(max_length=80)
    lengthkm = models.FloatField()
    reachcode = models.CharField(max_length=80)
    flowdir = models.CharField(max_length=80)
    wbareacomi = models.BigIntegerField()
    ftype = models.CharField(max_length=80)
    fcode = models.BigIntegerField()
    shape_leng = models.FloatField()
    enabled = models.CharField(max_length=80)
    gnis_nbr = models.BigIntegerField()
    geom = models.MultiPointField(srid=4326)

    class Meta:
        verbose_name_plural = 'Rivers'
