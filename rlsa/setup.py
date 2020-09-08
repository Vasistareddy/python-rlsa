from setuptools import setup, Extension
import numpy

ext = Extension("pythonRLSA", ["src/rlsa_c_extension.c"])

setup(
    name = "pythonRLSA",
    version = "0.0.2",
    ext_modules = [ext],
    include_dirs = [numpy.get_include()]
)
