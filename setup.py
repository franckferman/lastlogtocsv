from setuptools import setup, find_packages

VERSION='3.0.0' 
DESCRIPTION='lastlog to CSV converter.'
LONG_DESCRIPTION='Convert lastlog Linux file to CSV file, with Python 3.'

setup(
        name="lastlogtocsv",
        version=VERSION,
        packages=find_packages(),
        install_requires=[
        'typing_extensions'],
        author="Franck FERMAN",
        author_email="<fferman@protonmail.ch>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION, 
        keywords=['franckferman','lastlog','Linux'],
        classifiers=[
            'Programming Language :: Python :: 3'
            ]
)
