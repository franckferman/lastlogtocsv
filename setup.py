from setuptools import setup, find_packages

VERSION = '2.0.2' 
DESCRIPTION = 'lastlog file to csv'
LONG_DESCRIPTION = 'Convert lastlog Linux file to csv.'

# Setting up
setup(
       # the name must match the folder name 'lastlogtocsv'
        name="lastlogtocsv", 
        version=VERSION,
        author="Franck FERMAN",
        author_email="<fferman@protonmail.ch>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        
        keywords=['python', 'lastlog'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3",
        ]
)
