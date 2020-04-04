import re
from pathlib import Path

from setuptools import find_packages, setup

name = "{{ cookiecutter.package_name }}"
here = Path(__file__).parent

# get package version
init_file = here / name / "__init__.py"
result = re.search(r'__version__ = ["\']([^"\']+)', init_file.read_text())
if not result:
    raise ValueError("Can't find the version in {}.".format(init_file))
version = result.group(1)

with Path("requirements.txt").open("r") as f:
    requirements = [row.strip() for rwo in f if row.strip()]

with Path("test_requirements.txt").open("r") as f:
    test_requirements = [row.strip() for rwo in f if row.strip()]

setup(
    name=name,
    version=version,
    description="{{ cookiecutter.description }}",
    url="{{ cookiecutter.url }}",
    author="Fabian Peters",
    author_email="",
    packages=find_packages(exclude=["docs*", "tests*", "tools*"]),
    include_package_data=True,
    tests_require=test_requirements,
    install_requires=requirements,
)

