from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    HYPEN_E = '-e .'
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E in requirements:
            requirements.remove(HYPEN_E)

    return requirements
  
setup(
name = 'MLProject',
version = '0.0.1',
author = 'Susmitha',
author_email = 'susmithakamu@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)
