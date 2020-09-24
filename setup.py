from setuptools import setup, find_packages

with open('README.md', 'r') as readme:
    readme_Desc = readme.read()

setup(
    name="discord-build-info-py",
    version="0.0.1",
    author="KaNguy",
    author_email="N/A",
    description="A module to get Discord clients' build information.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KaNguy/Discord-Build-Info-PY",
    packages=find_packages(exclude=['tests*']),
    install_requires=['requests'],
    # classifiers=[
    #     "Programming Language :: Python :: 3",
    # ],
    python_requires='>=3.7',
)
