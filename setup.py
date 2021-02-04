from os import path

import setuptools

INSTALL_REQUIRES = ["eth-hash", "pyzil"]


def read(file_name: str) -> str:
    """Helper to read README."""
    this_directory = path.abspath(path.dirname(__file__))
    with open(path.join(this_directory, file_name), encoding="utf-8") as f:
        return f.read()


setuptools.setup(
    name="zilliqavanity",
    version="0.1.0",
    author="Fred Tarasevicius",
    author_email="zilliqafred@gmail.com",
    description="Tool to create custom zilliqa addresses.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/frog357/zilliqa-vanity/",
    keywords="zilliqa blockchain zil cryptocurrency address generator vanity",
    zip_safe=False,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=INSTALL_REQUIRES,
    entry_points={"console_scripts": ["zilliqavanity = zilliqavanity.__main__:main"]},
)