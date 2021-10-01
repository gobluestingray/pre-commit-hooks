# forbid-set-trace: off
from setuptools import find_packages, setup

setup(
    name="pre-commit-hooks",
    description="Hooks for pre-commit",
    url="https://github.com/traviswaelbro/pre-commit-hooks",
    version="0.0.1",
    author="Travis Waelbroeck",
    author_email="twaelbroeck@gmail.com",
    platforms="linux",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    packages=find_packages("."),
    entry_points={
        "console_scripts": [
            "forbid_git_conflicts = hooks.forbid_git_conflicts:main",
            "forbid_set_trace = hooks.forbid_set_trace:main",
        ],
    },
)
