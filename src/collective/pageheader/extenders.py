# -*- coding: utf-8 -*-

from zope.component import adapts
from zope.interface import implements

from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import ISchemaExtender

from Products.Archetypes import atapi
from plone.app.blob.field import ImageField
# from plone.app.blob.field import BlobField

from collective.pageheader.interfaces import IPageHeaderEnabled
from collective.pageheader import _

PAGEHEADER_FIELDNAME = 'pageheader_image'


class PageHeaderImageField(ExtensionField, ImageField):
    """ image field """


class BaseExtender(object):

    implements(ISchemaExtender)

    fields = []

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields


class Extender(BaseExtender):
    adapts(IPageHeaderEnabled)

    fields = [
        PageHeaderImageField(
            PAGEHEADER_FIELDNAME,
            widget=atapi.ImageWidget(
                label=_(u"Page Header"),
            ),
            validators=('isNonEmptyFile'),
            sizes={
                'large'   : (768, 768),
                'preview' : (400, 400),
                'mini'    : (200, 200),
                'thumb'   : (128, 128),
                'tile'    :  (64, 64),
                'icon'    :  (32, 32),
                'listing' :  (16, 16),
            },
        ),
    ]