import setuptools
from Cython.Build import cythonize

setuptools.setup(
    name="hello_world",
    version="0.0.1",
    package_dir={"": "src"},
    packages=["hello_world"],
    ext_modules=cythonize(
        [
            setuptools.Extension(
                "hello_world._impl",
                sources=["src/hello_world/_impl.pyx"],
                incude_dirs=["src"],
                define_macros=[("CYTHON_TRACE_NOGIL", "1")],
            ),
        ],
    ),
    zip_safe=False,
)
