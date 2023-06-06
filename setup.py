from setuptools import setup, find_packages

VERSION = '1'
DESCRIPTION = 'Hardware Id Authenication'
LONG_DESCRIPTION = 'A package that allows the user to authenicate user over their hwid.'

# Setting up
setup(
    name="pyhwidauth",
    version=VERSION,
    author="seasonal#6835",
    author_email="<unknown@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)