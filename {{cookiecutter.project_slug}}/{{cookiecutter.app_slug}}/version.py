from setuptools_scm import get_version

__version__ = get_version(root='..', relative_to=__file__)
print('Application Version: ' + __version__)