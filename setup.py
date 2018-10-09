# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

import io
import os
import re
from setuptools import setup, find_packages


def open_relative(*path):
    """
    Opens files in read-only with a fixed utf-8 encoding.

    All locations are relative to this setup.py file.
    """
    here = os.path.abspath(os.path.dirname(__file__))
    filename = os.path.join(here, *path)
    return io.open(filename, mode="r", encoding="utf-8")

with open_relative("src", "oci_cli", "version.py") as fd:
    version = re.search(
        r"^__version__\s*=\s*['\"]([^'\"]*)['\"]",
        fd.read(), re.MULTILINE).group(1)
    if not version:
        raise RuntimeError("Cannot find version information")

with open_relative("README.rst") as f:
    readme = f.read()

requires = [
    'oci',
    'arrow',
    'certifi',
    'click',
    'configparser',
    'cryptography',
    'httpsig_cffi',
    'jmespath',
    'python-dateutil',
    'pytz',
    'retrying',
    'six',
    'terminaltables',
    'idna'
]

fips_libcrypto_file = os.getenv("OCI_CLI_FIPS_LIBCRYPTO_FILE")
if fips_libcrypto_file:
    from setuptools.command.easy_install import ScriptWriter
    with open('src/oci_cli/oci_template.py', 'r') as template_file:
        template = template_file.read()
        ScriptWriter.template = template

setup(
    name='oci-cli',
    url='https://docs.us-phoenix-1.oraclecloud.com/Content/API/SDKDocs/cli.htm',
    version=version,
    author='Oracle',
    author_email='joe.levy@oracle.com',
    description='Oracle Cloud Infrastructure CLI',
    long_description=readme,
    entry_points={
        'console_scripts': ["bmcs=oci_cli.cli:cli", "oci=oci_cli.cli:cli"]
    },
    install_requires=requires,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    license="Universal Permissive License 1.0 or Apache License 2.0",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "License :: OSI Approved :: Universal Permissive License (UPL)",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
    ]
)
