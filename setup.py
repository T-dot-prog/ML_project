from setuptools import setup, find_packages

hyphen_e_dot= '-e.'

def get_requirements(file_path:str):

    with open(file_path) as file_obj:
        lines= []
        lines= file_obj.readlines()
        lines= [i.replace('\n','') for i in lines]

    if hyphen_e_dot in lines:
        lines.remove(hyphen_e_dot)
        


setup(
    name='Ml_project',
    version= '0.0.1',
    author='T-dot-prog',
    author_email='tahasinahoni2gmail.com',
    packages= find_packages(),
    package_requireds= get_requirements('requirements.txt')
    
    )
