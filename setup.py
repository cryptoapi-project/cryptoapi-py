from typing import List

from setuptools import find_packages, setup  # type: ignore

VERSION: str = '0.1.0'
packages: List[str] = find_packages(exclude=['tests'])

readme: str = open('README.md').read()
long_description: str = readme[readme.find('Cryptoapi-py library can be used'):readme.rfind("To see `Api's")]

setup(
    name='cryptoapi-py',
    version=VERSION,
    description='Python library for CryptoAPI.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    download_url='https://pypi.python.org/pypi/cryptoapi-py',
    license='MIT',
    author='PixelPlex inc',
    author_email='dev@pixelplex.io',
    url='https://apikey.io/',
    keywords=['blockchain',
              'api',
              'rpc'],
    packages=packages,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
    ],
    install_requires=open('requirements.txt').readlines(),
    include_package_data=True,
)
