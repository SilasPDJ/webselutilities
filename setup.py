from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()


setup(

    name='selebutilities',
    version='0.0.3',
    description='Lots of functionalities (methods) for selenium webdriver. Should take a look!',
    py_modules=["selebutilities"],
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
