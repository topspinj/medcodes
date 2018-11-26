from setuptools import setup, find_packages

setup(
    name="icd",
    version="0.1",
    url="https://github.com/mark-hoffmann/icd",

    author="Jill Cates",
    author_email="jill@biosymetrics.com",

    description="Tools for working with medical codes such as ICD and CPT",

    packages=find_packages(),

    install_requires=['pandas'],

    classifiers=[
        'Programming Language :: Python :: 3.6'
    ],
)