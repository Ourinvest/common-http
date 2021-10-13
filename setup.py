from setuptools import find_packages, setup

requirements = [
    "flask-restplus==0.13.0",
    "flask==1.1.1",
    "marshmallow==3.3.0",
    "simplejson==3.17.0",
    "werkzeug==0.16.0",
]

setup(name="common-http", version="1.2.7", packages=find_packages(), install_requires=requirements)
