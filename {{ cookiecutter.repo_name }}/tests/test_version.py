"""
A dummy test
"""
import {{ cookiecutter.package_name }}


def test_version():
    """ A simple dummy test """
    version = {{ cookiecutter.package_name }}.__version__
    assert version == "0.1.0"
