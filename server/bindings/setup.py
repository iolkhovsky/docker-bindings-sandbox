from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import sys
import setuptools

class CustomBuildExt(build_ext):
    def build_extensions(self):
        if sys.platform == 'darwin':
            self.compiler.compiler_so.append('-std=c++11')
        else:
            self.compiler.compiler_so.extend(['-std=c++11', '-fPIC'])
        super().build_extensions()

ext_modules = [
    Extension(
        'img_proc_lib',
        sources=['pythonic.cpp'],
        libraries=[
            'boost_python310',
            'boost_numpy310',
            'opencv_core',
            'img_processor_lib',
        ],
        include_dirs=[
            '/repos/sandbox/server',
        ],
        library_dirs=[
            '/repos/sandbox/bazel-bin/server/core',
        ],
        extra_compile_args=[
            '-std=c++11',
            '-I/usr/local/include/opencv4',
        ],
    )
]

setup(
    name='ProcessingBindings',
    version='0.1',
    author='My Name',
    description='Bindings for img_processor_lib',
    ext_modules=ext_modules,
    cmdclass={
        'build_ext': CustomBuildExt
    }
)

# python3 setup.py build
# python3 setup.py install
