from setuptools import setup, find_packages
setup

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["astropy"]

setup(
    name="zeroflux",
    version="0.0.1",
    author="Adam McCarron",
    author_email="adam.mcc.astro@gmail.com",
    packages=["zeroflux",
              "zeroflux.ioastro",
              "zeroflux.astromath",
              "zeroflux.photometry",
              "zeroflux.spectroscopy",
              "zeroflux.plotting"],
    description="A utility belt for day-to-day astronomy coding",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/apm5587/zeroflux",
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
