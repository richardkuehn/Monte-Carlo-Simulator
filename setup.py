from setuptools import setup, find_packages

setup(
    name = 'montecarlo',
    version = '0.1',
    author = 'Richard "Ricky" Kuehn',
    author_email = 'fmt2tg@virginia.edu',
    packages = find_packages(),
    url = 'https://github.com/richardkuehn/DS5100-finalproject-fmt2tg',
    license = open('LICENSE').read(),
    description = "package to keep track of readers' name, email, favorite genre, books read, and rating",
    long_description = open('README.md').read(),
    install_requires = ("Pandas >= 2.2.2", "Numpy >= 1.26.4")
    )