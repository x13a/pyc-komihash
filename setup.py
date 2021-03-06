from setuptools import Extension, setup
from Cython.Build import cythonize

setup(
    name='komihash',
    version='4.1',
    ext_modules=cythonize([Extension('komihash', ['komihash/komihash.py'])], language_level=3),
    zip_safe=False,
)
