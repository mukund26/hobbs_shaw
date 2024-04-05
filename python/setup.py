from setuptools import setup, find_packages

VERSION = '1.0.0' 
DESCRIPTION = 'SHA algorithms'
LONG_DESCRIPTION = 'SHA256 and SHA512 algorithm for strings and file'

setup(
        name="hasher", 
        version=VERSION,
        author="Mukund Agarwal",
        author_email="m.agarwalhp@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)