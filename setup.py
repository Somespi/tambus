import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tambus",
    version="0.2.0",
    author="Someone.",
    author_email="someonegithub@gmail.com",
    description="Bambus Template Engine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/somespi/tambus",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)