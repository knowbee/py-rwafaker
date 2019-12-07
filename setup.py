from setuptools import setup
from os import path
here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name="rwa-faker",
  version='1.0.1',
  description="generate massive amounts of realistic fake data",
  long_description=long_description,
  py_modules=["rwafake"],
  package_dir={'': 'src'},
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
      keywords= 'hi',
      author='Igwaneza Bruce',
      author_email='knowbeeinc@gmail.com',
      license='MIT',
      zip_safe=False,

)
