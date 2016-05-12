from __future__ import unicode_literals
from datetime import date

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext as _


# Comment
class ShoppingList(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False)
    label = models.CharField(max_length=255)
    _date = models.DateField(default=date.today, verbose_name=_("date"))
    items = models.ManyToManyField('ListItem', blank=True,
                                    related_name='items')
    
    class Meta:
        ordering = ( '_date', 'label', )
    
    def __unicode__(self):
        return "%s - %s" %(self.label, self._date)

class ListItem(models.Model):
    name = models.CharField(max_length=255)
    purchased = models.BooleanField(default=False)
    
    class Meta:
        ordering = ( 'purchased', 'name', )
    
    def __unicode__(self):
        return self.name
