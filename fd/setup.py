"""
The setup for the fd package.
"""

import ez_setup
ez_setup.use_setuptools()


from setuptools import setup, find_packages

setup(
      name='fd',
      version='0.1.0',
      packages=find_packages(),

      zip_safe=False,
      author = "Mocv Ksoh",
      author_email = "hoskvcom@gmail.org",
      description = "FD"
      )

