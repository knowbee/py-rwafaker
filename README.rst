rwafaker
===========

This is a simple python package that generates massive amounts of realistic fake data in Rwanda native language (Ikinyarwanda)

Installation
------------

The distribution is hosted on pypi at: https://pypi.org/project/rwafaker/. To directly install the package from pypi, run from your terminal::

    $ pip install rwafaker

Usage
----------- 

Single Outputs
===============

.. code-block :: python

   from rwafake import rwafaker
   
   fname = rwafaker.firstName() # 'Bisamaza'

   lname = rwafaker.lastName() # 'Smith'

   fullName = rwafaker.fullName() # 'Bisamaza Smith'

   email = rwafaker.email() # 'bisamaza_sm@gmail.com'

Multiple Outputs
=================

.. code-block :: python

   from rwafake import rwafaker
   
   fname = rwafaker.firstName(2) # ['Ngarambe', 'Rwigema']

   lname = rwafaker.lastName(2) # ['Barker', 'Fuller']

   fullName = rwafaker.fullName(2) # ['Kandekwe Galloway', 'Buhigiro Byers']

   email = rwafaker.email(2) # ['banganirora.suarez@ur.ac.rw', 'umugaba.cox@yahoo.com']

