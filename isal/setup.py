from setuptools import setup, find_packages

setup(
    name="isal",
    version="0.1",
    py_modules=["isal"],
    include_package_data=True,
    install_requires=[
        "click"
    ],
    entry_points="""
        [console_scripts]
        isal=cli:cli
    """,
)
