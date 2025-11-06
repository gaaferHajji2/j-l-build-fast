from setuptools import setup, Extension
from Cython.Build import cythonize

# define c extension
ext_modules = [
    Extension(
        'add_wrapper',
        sources=['add_ex_with_c/add_wrapper.pyx', 'add_ex_with_c/add.c'],
        language='c'
    )
]

setup(
    ext_modules=cythonize(ext_modules, compiler_directives={'language_level': '3'})
)