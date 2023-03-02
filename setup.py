from setuptools import setup, find_packages


def read_file(path: str) -> str:
    with open(path, "r") as f:
        res = f.read()
    return res


description = "`leetcode-alg`是针对leetcode解题的数据结构和算法库, 其设计准则是: 以通用性为核心, 并以最大可能进行性能优化. "
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
    name="leetcode_alg",
    version="0.1.0.dev0",
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT",
    url="https://github.com/Jintao-Huang/LeetCode-Py",
    author="Jintao Huang",
    author_email="huangjintao@mail.ustc.edu.cn",
    packages=[p for p in find_packages() if p.startswith("leetcode_alg")],
    install_requires=install_requires,
    classifiers=classifiers,
    python_requires=">=3.8"
)
