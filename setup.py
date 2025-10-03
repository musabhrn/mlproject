from setuptools import setup, find_packages

try:
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
except FileNotFoundError:
    requirements = []

try:
    with open('README.md', encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ''

setup(
    name='mlproject',
    version='0.01',
    packages=find_packages(),
    install_requires=requirements,  # Use the list from requirements.txt
    author='Musa',
    author_email='musaharon07@gmail.com',
    description='A machine learning project',
    url='https://github.com/musabhrn/mlproject.git',
)