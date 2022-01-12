
# -*- coding: utf-8 -*-
from plone.app.dexterity import _
from plone.app.z3cform.widget import AjaxSelectFieldWidget
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope import schema
from zope.interface import provider
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

import six


def _createEmploymentVocabulary():
    
    for name in ["FULL_TIME","PART_TIME","CONTRACTOR","TEMPORARY","INTERN","VOLUNTEER","PER_DIEM","OTHER"]:
        term = SimpleTerm(value=name, token=str(name), title=name)
        yield term

# Construct SimpleVocabulary objects of log level -> name mappings
employment_vocabulary = SimpleVocabulary(list(_createEmploymentVocabulary()))

@provider(IFormFieldProvider)
class IJobPosting(model.Schema):

    # categorization fieldset
    model.fieldset(
        'jobposting',
        label=_(u'label_schema_jobposting', default=u'Job Posting'),
        fields=['activateJobPosting', 'employmentType', 'hiringOrganization_type', 'hiringOrganization_name', 'hiringOrganization_sameAs', 'hiringOrganization_logo', 'jobLocation_type', 'jobLocation_streetAddress', 'jobLocation_addressLocality', 'jobLocation_addressRegion', 'jobLocation_postalCode', 'jobLocation_addressCountry'],
    )

    activateJobPosting = schema.Bool(title=u"Activate Job Posting structured data", default=False)

    employmentType = schema.Choice(
        vocabulary=employment_vocabulary,
        title=u"Employment type",
        default=u"FULL_TIME",
        required=False
    )

    hiringOrganization_type = schema.TextLine(
        title=u'Organization type (if different from default settings)',
        default=u'Organization',
        required=False
    )

    hiringOrganization_name = schema.TextLine(
        title=u'Organization name (if different from default settings)',
        default=u'',
        required=False
    )

    hiringOrganization_sameAs = schema.TextLine(
        title=u'Organization url (if different from default settings)',
        default=u'',
        required=False
    )

    hiringOrganization_logo = schema.TextLine(
        title=u'Organization logo url (if different from default settings)',
        default=u'',
        required=False
    )

    jobLocation_type = schema.TextLine(
        title=u'Job Location type (if different from default settings)',
        default=u'Place',
        required=False
    )

    jobLocation_streetAddress = schema.TextLine(
        title=u'Job Location street address (if different from default settings)',
        default=u'',
        required=False
    )

    jobLocation_addressLocality = schema.TextLine(
        title=u'Job Location address locality (if different from default settings)',
        default=u'',
        required=False
    )

    jobLocation_addressRegion = schema.TextLine(
        title=u'Job Location address region (if different from default settings)',
        default=u'',
        required=False
    )

    jobLocation_postalCode = schema.TextLine(
        title=u'Job Location postal code (if different from default settings)',
        default=u'',
        required=False
    )

    jobLocation_addressCountry = schema.TextLine(
        title=u'Job Location address country (if different from default settings)',
        default=u'',
        required=False
    )




