
from setuptools import find_packages, setup

requirements = ["fastapi",
                "pydantic"]

setup(name="common_http", version="0.0.1",
      url='https://github.com/Ourinvest/common-http.git',
      packages=find_packages(),
      install_requires=requirements)
