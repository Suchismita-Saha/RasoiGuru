from setuptools import find_packages,setup
from typing import List

# Define the string '-e .' for later use
HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []

    # Open the requirements file and read its contents
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()

        # Remove newline characters from each requirement and store them in a list
        requirements = [req.replace('\n', '') for req in requirements]

        # If '-e .' is present in the requirements, remove it
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

# Setup configuration for the package
setup(
    name='RasoiGuru',
    version='0.0.1',
    description="RasoiGuru is your ultimate cooking assistant chatbot, offering detailed cooking instructions, ingredient substitutions, and personalized culinary tips to elevate your kitchen skills.",
    author='Suchismita Saha',
    author_email='suchismitasaha183@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)