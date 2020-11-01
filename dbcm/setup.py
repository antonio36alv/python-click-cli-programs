from setuptools import setup, find_packages

setup(
    name="dbcm",
    version="0.1",
    packages=["dbcm"], 
    include_package_data=True,
    install_requires=[
        "click", "mongoengine"
    ],
    entry_points="""
        [console_scripts]
        dbcm=dbcm.cli:cli
    """,
)
