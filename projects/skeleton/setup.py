try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'hardwayproj',
    'author': 'Arianaz',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'arianazarkaman@yahoo.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'hardwayproj'
}

setup(**config)
