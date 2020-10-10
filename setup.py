import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Zepel", # Replace with your own username
    version="0.0.2",
    author="Stephan Meijer",
    author_email="zepelpy@stephanmeijer.com",
    description="A client for Zepel.io",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/StephanMeijer/Zepel",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP"
    ],
    python_requires='>=3.7',
)
