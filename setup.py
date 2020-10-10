from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()


setup(

    name='web',
    version='0.0.1',
    description='Say hello!',
    py_modules=["helloworldpdjsilsz"],
    package_dir={'': 'src'},

    long_description=long_description,
    long_description_content_type="text/markdown",

    url=None,
    author='Silas BF',
    author_email='oesksbfserver@gmail.com',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
