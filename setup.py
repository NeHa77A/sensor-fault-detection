from setuptools import find_packages    ## it will search module or package in root directory
from setuptools import setup   
from typing import List

Name = "sensor"
Version = "0.0.1"
Author ="Neha Vishwakarma"
Email ="nehavishwakarma7777@gmail.com"

# This function return list of requirements
def get_all_requirements() -> List[str]:
    requirements_list: List[str] = []

    # Open the requirements.txt file for reading
    with open('requirements.txt', 'r') as file:
        for line in file:
            # Remove leading and trailing whitespace and append to the list
            requirement = line.strip()
            if requirement:
                requirements_list.append(requirement)

    return requirements_list

setup(
    name= Name,
    version=Version,
    author=Author,
    author_email= Email,
    packages= find_packages(),
    install_requires =get_all_requirements(),
)

if __name__ == "__main__":
    requirements = get_all_requirements()
    print(requirements)