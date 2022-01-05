# -*- coding: utf-8 -*-
from datetime import date
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from zope import schema
from zope.interface import Interface

class IJobPostingControlPanel(Interface):

    hiringOrganization_type = schema.TextLine(
        title=u'Organization type',
        default=u'Organization',
        required=False
    )

    hiringOrganization_name = schema.TextLine(
        title=u'Organization name',
        default=u'',
        required=False
    )

    hiringOrganization_sameAs = schema.TextLine(
        title=u'Organization url',
        default=u'',
        required=False
    )

    hiringOrganization_logo = schema.TextLine(
        title=u'Organization logo (url)',
        default=u'',
        required=False
    )

    jobLocation_type = schema.TextLine(
        title=u'Job Location type',
        default=u'Place',
        required=False
    )

    jobLocation_streetAddress = schema.TextLine(
        title=u'Job Location street address',
        default=u'',
        required=False
    )

    jobLocation_addressLocality = schema.TextLine(
        title=u'Job Location address locality',
        default=u'',
        required=False
    )

    jobLocation_addressRegion = schema.TextLine(
        title=u'Job Location address region',
        default=u'',
        required=False
    )

    jobLocation_postalCode = schema.TextLine(
        title=u'Job Location postal code',
        default=u'',
        required=False
    )

    jobLocation_addressCountry = schema.TextLine(
        title=u'Job Location address country',
        default=u'',
        required=False
    )

class JobPostingControlPanelForm(RegistryEditForm):
    schema = IJobPostingControlPanel
    label = u'JobPosting control panel'

class JobPostingPanelView(ControlPanelFormWrapper):
    form = JobPostingControlPanelForm



