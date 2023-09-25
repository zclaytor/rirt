from setuptools import setup, find_packages


setup(
    name="rirt",
    version="1.0.0",
    author="Zachary R. Claytor <zclaytor@ufl.edu>",
    description="Computation of Ca II IRT index from Lanzafame et al. (2023)",
    url="https://github.com/zclaytor/rirt",
    license="MIT",
    python_requires="==3.*",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scipy",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: All",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Astronomy",
    ],
)