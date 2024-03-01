from setuptools import setup, find_packages

setup(
    name="PipeFunc",
    version="1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    author="Joel Castro",
    description="A powerful Function Chaining wrapper of python functtools.",
    install_requires=["numpy", "pandas"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)