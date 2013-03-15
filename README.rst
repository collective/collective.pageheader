.. contents::

Introduction
============

A Plone package for adding an image header to your contents.

If an header is found on the context this will be used as header image, otherwise the machinery will look up into parents to find one. In this way we can have a section header and override it per-content.

The image field is inject using archetypes.schemaextender, of course.
