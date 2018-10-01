from setuptools import setup, find_packages
import os

setup(
    name='uperations-base',
    version='0.0.8',
    packages=find_packages(),
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'README.rst')).read(),
    author='Brice Aminou',
    author_email='brice.aminou@gmail.com',
    keywords='workflow tool',
    url='https://github.com/baminou/Uperations-Base',
    install_requires=['jsonschema==2.6.0','uperations_kernel==0.0.6','tabulate==0.8.2','termcolor==1.1.0',
                      'setuptools==40.0.0','PyContracts==1.8.3','python-dotenv==0.9.1','PyYAML==3.13']
)