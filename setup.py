from setuptools import setup
from os import path
here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="rwafaker",
    version='2.0.6',
    url="https://github.com/knowbee/py-rwafaker.git",
    description="This package generates massive amounts of realistic fake data in Rwanda native language (Ikinyarwanda)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["rwafake"],
    package_dir={'': 'rwafake'},
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Development Status :: 4 - Beta",
            "Environment :: Other Environment",
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "License :: OSI Approved :: GNU General Public License (GPL)",
            "Operating System :: OS Independent",
            "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    keywords='hi',
    author='Igwaneza Bruce',
    author_email='knowbeeinc@gmail.com',
    license='MIT',
    zip_safe=False,

)
