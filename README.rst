Introduction
============

A behavior that includes extra fields to describe a job opening in a certain organization. 

Features
===================
- Extra fields based on the schema https://schema.org/JobPosting
- Control panel to document fields that are shared between all job openings
- Renders the fields as structured data optimized for Google: https://developers.google.com/search/docs/advanced/structured-data/job-posting
- Compatible with Python 3 and Plone 5.2.x


Fields used for the schema
===================
- datePosted (uses default Plone publication date)
- validThrough (uses default Plone expiration date)
- title (uses default title)
- description (uses default description)
- employmentType (extra field included via the behavior)
- hiringOrganization (extra field included via the bihavior)
- jobLocation (extra field included via the bihavior)


General fields
===================
- hiringOrganization (can be overriden per job posting if necessary)
- jobLocation (can be overriden per job posting if necessary)


Installation
===================
If you are using zc.buildout and the plone.recipe.zope2instance recipe to manage your project, you can do this:
Add collective.jobposting to the list of eggs to install, e.g.::

	[buildout]
		…
		eggs =
			…
			collective.jobposting


Todo's
===================
- Include non-required extra fields https://developers.google.com/search/docs/advanced/structured-data/job-posting#structured-data-type-definitions
