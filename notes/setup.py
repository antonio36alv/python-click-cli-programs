from setuptools import setup, find_packages

setup(
    name="notes",
    version="0.1",
    py_modules=["notes"], 
    include_package_data=True,
    install_requires=[
        "Click",
    ],
    entry_points="""
        [console_scripts]
        notes=notes:cli
    """,
)
