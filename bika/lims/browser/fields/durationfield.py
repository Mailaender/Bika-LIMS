from AccessControl import ClassSecurityInfo
from Products.ATExtensions.Extensions.utils import makeDisplayList
from Products.ATExtensions.ateapi import RecordField, RecordsField
from Products.Archetypes.Registry import registerField
from Products.Archetypes.public import *
from Products.CMFCore.utils import getToolByName
from Products.validation import validation
from Products.validation.validators.RegexValidator import RegexValidator
import sys
from bika.lims import bikaMessageFactory as _

class DurationField(RecordField):
    """ Stores duration in Days/Hours/Minutes """
    security = ClassSecurityInfo()
    _properties = RecordField._properties.copy()
    _properties.update({
        'type' : 'duration',
        'subfields' : ('days', 'hours', 'minutes'),
        'subfield_labels':{'days':_('Days'),
                           'hours':_('Hours'),
                           'minutes':_('Minutes')},
        'subfield_sizes': {'days':2,
                           'hours':2,
                           'minutes':2},
        })

registerField(DurationField,
              title = "Duration",
              description = "Used for storing durations",
              )

