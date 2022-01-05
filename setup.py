from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='collective.jobposting',
      version=version,
      description="A behavior that includes extra fields to describe a job opening in a certain organization.",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.rst")).read(),
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='Plone',
      author='Andre Goncalves',
      author_email='andre@intk.com',
      url='https://github.com/intk/collective.jobposting',
      download_url='https://github.com/intk/collective.jobposting/tarball/0.1',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
