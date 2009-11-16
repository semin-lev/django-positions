from django.db import models, transaction

from positions.fields import PositionField


class List(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Item(models.Model):
    list = models.ForeignKey('list', related_name='items', db_index=True)
    name = models.CharField(max_length=50)

    # Intentionally use the deprecated `unique_for_field` argument.
    position = PositionField(unique_for_field='list')

    def __unicode__(self):
        return self.name
