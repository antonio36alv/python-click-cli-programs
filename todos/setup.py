from setuptools import setup, find_packages

setup(
    name="todos",
    version="0.1",
    packages=["todos"],
    include_package_data=True,
    install_requires=[
        "click", "mongoengine", "PyInquirer"
    ],
    entry_points="""
        [console_scripts]
        todos=todos.cli:cli
    """,
)
