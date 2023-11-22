from setuptools import find_packages,setup
from typing import List


HYPHEN_E_DOT = "-e ." 

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines() # each line from requirements.txt file will be read
        requirements = [req.replace("\n"," ") for req in requirements] # replacing "\n" after each packages in requirements.txt with a space " " 
        
        
        # list will return -e . form reuirements.txt, so to avoid it we will write this condition:
        if HYPHEN_E_DOT in requirements: 
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements


setup(   
    name = 'ML_deployment',
    version ='0.0.1',
    author = 'Mohit Kumar',
    author_email = 'mkr9395@gmail.com',
    packages = find_packages(),
    # install_requires = ['pandas','numpy','seaborn']  --> not feasible to write packages this way
    install_requires = get_requirements('requirements.txt') # this function takes all the packages from requirements.txt and installs it.
)