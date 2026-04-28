from setuptools import setup

setup(
    name="csrf-poc-gen",
    version="1.0.0",
    description="Burp-compatible CSRF PoC generator from raw HTTP requests",
    py_modules=["csrf_poc_gen"],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "csrf-poc-gen=csrf_poc_gen:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Security",
        "Environment :: Console",
    ],
)