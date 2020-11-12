from setuptools import setup, find_packages

setup(
    name="svg-code-editor",
    version="0.1",
    py_modules=["svg-code-editor"],
    include_package_data=True,
    install_requires=[
        "click"
    ],
    entry_points="""
        [console_scripts]
        svg-code-editor=cli:cli
    """,
)
