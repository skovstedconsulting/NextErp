from setuptools import setup, find_packages

setup(
    name="hello_world",
    version="0.0.1",
    description="Minimal Hello World app for ERPNext",
    author="You",
    author_email="you@example.com",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
