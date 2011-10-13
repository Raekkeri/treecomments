from setuptools import setup, find_packages

setup(name='treecomments',
    version='0.01',
    description='Django tree-like comments',
    author='Teemu Husso',
    author_email='teemu.husso@gmail.com',
    url='',
    packages=find_packages(exclude=['ez_setup']),
    package_dir={
        '': 'src',
        },
    install_requires=[
        'setuptools',
        'django-mptt',
        ],
)
