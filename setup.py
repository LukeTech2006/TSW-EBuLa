# Run/Used from command -> pip install -e .
from setuptools import setup, find_packages
# from toml import load

# #PEP 735 – Dependency Groups in pyproject.toml
# pyproject = load('pyproject.toml')

# base_dependencies = pyproject.get('dependency-groups', {}).get('base', [])
# optional_dependencies = pyproject.get('dependency-groups', {}).get('dev', [])

setup(
    name='your_package_name',
    version='0.1.0',
    packages=find_packages(),
    # install_requires=base_dependencies,
    # extras_require={
    #     'dev': optional_dependencies,
    # },
)