#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import common as base
from collective.jobposting.utils import get_general_fields
import json 

class JobPostingViewlet(base.ViewletBase):

    def getStructuredData(self):

        activate_structured_data = getattr(self.context, 'activateJobPosting', False)

        if activate_structured_data:
            general_fields = get_general_fields()

            structured_data = {
                "@context" : "https://schema.org/",
                "@type" : "JobPosting",
                "title" : getattr(self.context, 'title', None),
                "description" : getattr(self.context, 'description', None),
                "datePosted" : "2020-10-20",
                "validThrough": "",
                "employmentType" : getattr(self.context, 'employmentType', None),
                "hiringOrganization" : general_fields.get('hiringOrganization', ""),
                "jobLocation": general_fields.get('jobLocation', ""),
            }

            publication_date = self.context.effective()
            if publication_date:
                publication_date = publication_date.strftime("%Y-%m-%d")
                structured_data['datePosted'] = publication_date

            expiration_date = self.context.expires()
            if expiration_date:
                expiration_date = expiration_date.strftime("%Y-%m-%d")
                structured_data['validThrough'] = expiration_date

            return json.dumps(structured_data, indent=4)
        else:
            return None


