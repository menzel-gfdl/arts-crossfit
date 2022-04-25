from setuptools import find_packages, setup


setup(
    name="arts_crossfit",
    version="1.0.0",
    author="O. Lemke, M. Brath, S. Buehler",
    author_email="",
    description="Absorption cross section model.",
    url="",
    python_requires=">=3.6",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "matplotlib",
        "numpy",
        "scipy",
        "xarray",
    ],
)
