from setuptools import find_packages, setup


setup(
    name="arts_crossfit",
    version="1.0.0",
    author="O. Lemke, M. Brath, S. Buehler",
    author_email="",
    description="",
    url="",
    python_requires=">=3.6",
    package=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "matplotlib",
        "numpy",
        "scipy",
        "xarray",
    ],
)
