from setuptools import setup, find_packages


def read_file(path: str) -> str:
    with open(path, "r") as f:
        res = f.read()
    return res


description = "algpy is a python based implementation of data structures and algorithms library"
long_description = read_file("README.md")
install_requires = read_file("requirements.txt").splitlines(False)
classifiers = [
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    'Programming Language :: Python',
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
]
setup(
    name="algpy",
    version="0.1.0",
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT",
    url="https://github.com/Jintao-Huang/algpy",
    author="Jintao Huang",
    author_email="huangjintao@mail.ustc.edu.cn",
    packages=[p for p in find_packages() if p.startswith("algpy")],
    install_requires=install_requires,
    classifiers=classifiers,
    python_requires=">=3.8"
)