from django.db import models


class Collection(models.Model):
    DISPOSITION_CHOICES = (
       (u'RC', u'Vinyl records'),
       (u'8T', u'Eight-tracks'),
       (u'CT', u'Cassette tapes'),
       (u'BK', u'Books'),
       (u'CM', u'Comics'),
       (u'MG', u'Magazines'),
       (u'CD', u'CDs'),
       (u'DV', u'DVDs'),
       (u'BR', u'Blu-rays'),
       (u'CS', u'Custom'),
    )
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    disposition = models.CharField(max_length=2, choices=DISPOSITION_CHOICES)
    owner = models.ForeignKey('auth.User')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Location(models.Model):
    name = models.CharField(max_length=100)


class Item(models.Model):
    owner = models.ForeignKey('auth.User')
    collection = models.ForeignKey('Collection')
    location =  models.ForeignKey('Location')


class VinylRecord(Item):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

