import io
import os
from setuptools import setup, find_packages

# Read the long description from README.md
here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="nowcasting-toolbox-py",
    version="0.1.0",
    description="Implementación en Python de la Nowcasting Toolbox",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Carmen Pelayo Fernández",
    author_email="carmen.pelayo@bbva.com",
    url="https://github.com/tu-usuario/nowcasting_toolbox_py",
    license="MIT",
    python_requires=">=3.8",
    packages=find_packages(exclude=["tests*", "docs*"]),
    include_package_data=True,
    install_requires=[
        "pandas>=1.5",
        "numpy>=1.23",
        "scikit-learn>=1.2",
        "statsmodels>=0.14",
        "matplotlib>=3.6",
        "python-dateutil>=2.8",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    project_urls={
        "Documentation": "https://github.com/tu-usuario/nowcasting_toolbox_py#readme",
        "Source": "https://github.com/tu-usuario/nowcasting_toolbox_py",
        "Tracker": "https://github.com/tu-usuario/nowcasting_toolbox_py/issues",
    },
)
