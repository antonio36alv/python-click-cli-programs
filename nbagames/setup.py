from setuptools import setup, find_packages

setup(
    name="nbagames",
    version="0.1",
    packages=["nbagames"], 
    include_package_data=True,
    install_requires=[
        "Click",
    ],
    entry_points="""
        [console_scripts]
        nbagames=nbagames.cli:cli
    """,
)
