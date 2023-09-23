from setuptools import find_packages    ## it will search module or package in root directory
from setuptools import setup   
from typing import List

Name = "sensor"
Version = "0.0.1"
Author ="Neha Vishwakarma"
Email ="nehavishwakarma7777@gmail.com"

# This function return list of requirements
def get_all_requirements()->List[str]:
    requirements_list:List[str] =[]
    return requirements_list

setup(
    name= Name,
    version=Version,
    author=Author,
    author_email= Email,
    packages= find_packages(),
    install_requires =get_all_requirements(),
)
