'''
Setup file for the project.
'''

from setuptools import setup


setup(
    name='myflaskd3',
    packages=['myflaskd3', ],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
