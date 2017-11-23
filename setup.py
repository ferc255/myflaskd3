'''
Setup file for the project.
'''

from setuptools import setup


setup(
    name='myflaskd3',
    packages=['myflaskd3'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    entry_points={
        'console_scripts': ['myflaskd3_server=myflaskd3.__init__:main'],
    }
)
