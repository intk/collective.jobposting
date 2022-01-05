#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from collective.jobposting.controlpanel.controlpanel import IJobPostingControlPanel

from zope.component import getUtility
from zope.component import getUtility

def get_general_fields():
    registry = getUtility(IRegistry)
    settings = registry.forInterface(IJobPostingControlPanel)
        
    jobposting_settings = {
        'hiringOrganization': {
            "type": getattr(settings, 'hiringOrganization_type', None),
            "name": getattr(settings, 'hiringOrganization_name', None),
            "sameAs": getattr(settings, 'hiringOrganization_sameAs', None),
            "logo": getattr(settings, 'hiringOrganization_logo', None),
        }, 
        'jobLocation': {
            "@type": "Place",
            "address": {
                "streetAddress": getattr(settings, 'jobLocation_streetAddress', None),
                "addressLocality": getattr(settings, 'jobLocation_addressLocality', None),
                "addressRegion": getattr(settings, 'jobLocation_addressRegion', None),
                "postalCode": getattr(settings, 'jobLocation_postalCode', None),
                "addressCountry": getattr(settings, 'jobLocation_addressCountry', None),
            }
        }
    }   
    
    return jobposting_settings
    


