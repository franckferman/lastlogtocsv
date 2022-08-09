from setuptools import setup, find_packages

VERSION = '2.0.7' 
DESCRIPTION = 'lastlog to csv.'
LONG_DESCRIPTION = 'Convert lastlog Linux file to csv.'

setup(
        name="lastlogtocsv",
        version=VERSION,
        packages=find_packages(),
        author="Franck FERMAN",
        author_email="<fferman@protonmail.ch>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION, 
        keywords=['franckferman', 'lastlog'],
        classifiers=[
            'Programming Language :: Python :: 3'
            ]
)
