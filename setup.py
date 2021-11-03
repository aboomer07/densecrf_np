from distutils.extension import Extension
from Cython.Build import cythonize
import numpy as np
from setuptools import find_packages, setup

setup(
    name='densecrf_np',
    version="0.0.1",
    author="Sadeep Jayasumana",
    author_email="sadeep@apache.org",
    url='https://github.com/aboomer07/densecrf_np',
    platforms=["any"],
    packages=find_packages(exclude=["test"]),
    entry_points={
            'console_scripts': [
                  'densecrf_np = densecrf_np.__main__:main'
            ]
    },
    ext_modules=cythonize(
        Extension(
            "densecrf_np.py_permutohedral",
            sources=["densecrf_np/py_permutohedral.pyx"],
            include_dirs=[np.get_include()]
        ),
    ),
)
